from constants import all_date_pattern, bcolors


def extract_dates(text):
    matches = all_date_pattern.finditer(text.lower())
    return [m.span() for m in matches]


if __name__ == '__main__':
    text = input('Enter the text in a single line: ')
    print()
    print('------------ RESULTS ------------')
    print()
    for s, e in extract_dates(text):
        print(f'Found {bcolors.BOLD}{text[s:e]}{bcolors.ENDC} at {bcolors.BOLD}position {s}{bcolors.ENDC}')
    print()
