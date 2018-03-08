from update_abstracts import *

def main():
    sheet = get_sheet()
    attendees, abstracts = parse_sheet(sheet)

    #sort attendees alphabetically by last name
    abstracts.sort(key=lambda x: x.last)

    # For All Abstracts
    with open("./_abstracts/all_abstracts.md", 'w') as text_file:
        text_file.write("# Abstracts\n")
        text_file.write("## B.R.A.I.N. Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'neuro':
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')

        text_file.write("\n\n## Cardiovascular and Respiratory Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'cardio':
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')

        text_file.write("\n\n## Endocrine and Diabetes Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'endo':
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')

        text_file.write("\n\n## Reproduction and Development Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'repro':
                text_file.write('\n' + poster.just_abstract.encode('utf-8')  + '\n')


    # For Oral Presentation Judging
    with open("./_abstracts/orals_only.md", 'w') as text_file:
        text_file.write("# Oral Submissions \n")
        text_file.write("## B.R.A.I.N. Research Group\n")
        for poster in abstracts:
            if (poster.platform_code == 'neuro') and (poster.pref == 'oral'):
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')
                if poster.req:
                    text_file.write('\n*This student needs an oral presentation to complete degree requirements* \n')

        text_file.write("\n\n## Cardiovascular and Respiratory Research Group\n")
        for poster in abstracts:
            if (poster.platform_code == 'cardio') and (poster.pref == 'oral'):
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')
                if poster.req:
                    text_file.write('\n*This student needs an oral presentation to complete degree requirements* \n')

        text_file.write("\n\n## Endocrine and Diabetes Research Group\n")
        for poster in abstracts:
            if (poster.platform_code == 'endo') and (poster.pref == 'oral'):
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')
                if poster.req:
                    text_file.write('\n*This student needs an oral presentation to complete degree requirements* \n')

        text_file.write("\n\n## Reproduction and Development Research Group\n")
        for poster in abstracts:
            if (poster.platform_code == 'repro') and (poster.pref == 'oral'):
                text_file.write('\n' + poster.just_abstract.encode('utf-8') + '\n')
                if poster.req:
                    text_file.write('\n*This student needs an oral presentation to complete degree requirements* \n')


if __name__ == '__main__':
    main()
