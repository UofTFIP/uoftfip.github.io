from update_abstracts import *

def main():
    sheet = get_sheet()
    attendees, abstracts = parse_sheet(sheet)

    #sort attendees alphabetically by last name
    abstracts.sort(key=lambda x: x.last)

    with open("./_abstracts/all_abstracts.md", 'w') as text_file:
        text_file.write("# Abstracts\n")
        text_file.write("## B.R.A.I.N. Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'neuro':
                text_file.write('\n' + poster.just_abstract + '\n')

        text_file.write("## Cardiovascular and Respiratory Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'cardio':
                text_file.write('\n' + poster.just_abstract + '\n')

        text_file.write("## Endocrine and Diabetes Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'endo':
                text_file.write('\n' + poster.just_abstract + '\n')

        text_file.write("## Reproduction and Development Research Group\n")
        for poster in abstracts:
            if poster.platform_code == 'repro':
                text_file.write('\n' + poster.just_abstract + '\n')


if __name__ == '__main__':
    main()
