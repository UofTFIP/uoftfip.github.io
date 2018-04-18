from __future__ import unicode_literals

import csv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

def get_sheet(year=2018):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    docid = "1LHBdI-izqp4rTBMz3ZnKLhyS6KKGSKdMvX0v53j5Hsw"

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key(docid)

    #spreadsheet = client.open('38th Annual FIP Registration (Responses)')

    a = spreadsheet.get_worksheet(index=0)
    df = pd.DataFrame(a.get_all_values()[1:], columns=a.get_all_values()[0])
    new_names = ['Status', 'Session_ID', 'Timestamp', 'Email', 'Last Name',
       'First Name', 'Supervisor', 'Co-Supervisor', 'Position', 'Platform', 'Restrictions',
       'Submitting', 'Authors', 'Affiliations', 'Abstract Title', 'Abstract', 'Preference', 'Required', 'Fip Comm', 'na', 'na', 'na', 'na']
    df.columns = new_names
    df.replace('', np.nan, inplace=True)
    df.dropna(axis=0,how='all', inplace=True)
    df = df.reset_index()
    return df

def make_entry(row):
    #makes an attendee or abstract
    if row['Submitting'] == 'Yes':
        attendee = Abstract(row['First Name'], row['Last Name'], row['Email'],
            row['Status'], row['Platform'], row['Short_Platform'], row['Position'],
            row['Session_ID'], row['Authors'], row['Affiliations'], row['Abstract Title'], row['Abstract'],row['Fip Comm'], row['Preference'], row['Required'])
    else:
        attendee = Attendee(row['First Name'], row['Last Name'], row['Email'],
            row['Status'], row['Platform'], row['Short_Platform'], row['Position'], row['Fip Comm'])
    return attendee


class Attendee(object):
    def __init__(self, first, last, email, status, platform, platform_code, position, comm):
        self.first = first
        self.last = last
        self.email = email
        if type(status) == float:
            self.status = 'Pending'
        else:
            self.status = status
        self.platform = platform
        self.platform_code = platform_code
        self.position = position
        self.committee = unicode(comm)
        if self.committee in ['GASP VP, Co-Organizer', 'FIP Committee']:
            self.img = 'http://sites.utoronto.ca/gasp/images/{}.jpg'.format(self.first.lower())
            self.blurb = '''- name: "{} {}, {}"
  type: "Planning Committee"
  platform: "{}"

'''.format(
                self.first, self.last, self.committee, self.platform)
        elif self.status.lower() in ['poster', 'oral']:
            self.blurb = '''- name: "{} {}"
  type: "Presenters"
  platform: "{}"

'''.format(self.first, self.last, self.platform)


class Abstract(Attendee):
    def __init__(self, first, last, email, status, platform, platform_code, position,
                    session, authors, affiliations, title, abstract, comm, pref, req):
        Attendee.__init__(self, first, last, email, status, platform, platform_code, position, comm)
        #false set to visible is false, true if visible true
        self.pending = self.status.lower() != 'pending'
        self.session = session
        #presentation preference
        self.pref = 'oral' if 'poster only' not in pref.lower() else 'poster'
        self.req = True if 'yes' in req.lower() else False

        if self.pending:
            self.tags = ' '.join([self.status.lower(), self.platform_code])
        else:
            self.tags = ''
        #parse authors/affiliations
        try:
            authors = authors.replace("*", "\*").replace(", ", ",")
            self.authors = [i.strip().split(',') for i in authors.split(';')]
            self.affiliations = [i.strip().rstrip(';') for i in affiliations.replace("*", "\*").split(";")]

        except AttributeError:
            print 'No Authors'
            self.authors = ['Empty']
            self.affiliations = ['empty']
        self.title = title
        self.abstract = abstract
        authors_parsed = []
        for ix,i in enumerate(self.authors):
            if ix == 0:
                # bold first author
                author = '**<sup>{}</sup>{}**'.format(','.join(i[1:]).strip(), i[0])
            else:
                author = '<sup>{}</sup>{}'.format(','.join(i[1:]).strip(), i[0])
                author_only = '**{}**'.format(i[0])
            authors_parsed.append(author)
        self.authors_parsed = ", ".join(authors_parsed)
        self.just_authors_poster = ', '.join([i[0] for i in self.authors])
        self.authors[0][0] = "**" + self.authors[0][0] + "**"
        self.just_authors = ', '.join([i[0] for i in self.authors])
        self.affiliations_parsed = u"__{}__\n".format(u"; ".join(self.affiliations))
        self.header = '''---
layout: post
title: "{}"
header-img: "img/banner.jpg"
category: abstracts
platform: "{}"
subtitle: "{}"
tags: {}
session_id: {}
visible: {}
---
'''.format(self.title, self.platform_code, self.just_authors_poster, self.tags, self.session, str(self.pending).lower())
        self.post = self.header + self.authors_parsed + "\n\n" + self.affiliations_parsed + "\n" + self.abstract
        self.post = unicode(self.post)
        self.short = '**{}. {}**'.format(self.session, self.title) + "  \n" + self.just_authors + "\n\n\n"
        self.short = unicode(self.short)
        self.just_abstract = '### ' + self.title + "\n\n" + self.authors_parsed + "\n\n" + self.affiliations_parsed + "\n" + self.abstract
        self.just_abstract = unicode(self.just_abstract)


a = True

str(a).lower()

def parse_sheet(df):
    #recode all platforms into shortform
    platforms = {"B.R.A.I.N.": "neuro","Endocrine and Diabetes Research Group": 'endo',
                "Cardiovascular and Respiratory Research Group": 'cardio', "Reproduction and Development Research Group": "repro"}
    df['Short_Platform'] = df['Platform'].map(platforms)
    attendees = []
    print df.index
    for i in df.index:
        attendee = make_entry(df.iloc[i])
        attendees.append(attendee)
    abstracts = [i for i in attendees if type(i) == Abstract]
    abstracts = sorted(abstracts, key=lambda x: (x.session, x.last), reverse=True)
    return attendees, abstracts


def remove_abstract(abstract):
    '''
    for situation where student is no longer able to present but will still be attending
    '''
    if abstract.status.lower() == 'removed':
        os.remove('_posts/2018-01-01-{}-{}.md'.format(abstract.last, abstract.first))


def main():
    sheet = get_sheet()
    attendees, abstracts = parse_sheet(sheet)
    #make postings for abstracts
    for poster in abstracts:
        with open("_posts/2018-01-01-{}-{}.md".format(poster.last, poster.first), 'w') as text_file:
            text_file.write(poster.post.encode('utf-8'))
        remove_abstract(poster)
    #make attendee list
    blurbs = [i.blurb for i in attendees if hasattr(i, 'blurb')]
    members = ''.join(blurbs)
    #with open("_data/members.yml", 'w') as f:
    #    f.write(members)
    print "# of abstracts:", len(abstracts)


if __name__ == '__main__':
    main()
