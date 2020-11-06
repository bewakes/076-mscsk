from constants import (
    bcolors,
    year_pattern,
    date_pattern,
    verbose_pattern,
    verbose_days_pattern,
    verbose_years_pattern,
    day_month_pattern,
    all_date_pattern,
)
import traceback

passed = 0
failed = 0
total = 0

failed_logs = []


def log_pass_fail(f):
    global total
    total += 1

    def wrapped(*args, **kwargs):
        global passed, failed
        try:
            r = f(*args, **kwargs)
            passed += 1
            print(bcolors.OKGREEN+f.__name__, '................ PASSED', bcolors.ENDC)
            return r
        except AssertionError:
            failed += 1
            print(bcolors.FAIL+f.__name__, '................ FAILED', bcolors.ENDC)
            failed_logs.append((f.__name__, traceback.format_exc()))
    return wrapped


@log_pass_fail
def test_year_formats():
    valid_years = [
        '1700', '1123', '1500', '1643', '1809', '1888', '1999', '1994', '1543',
        '2020', '2021', '2000', '2111', '2100'
    ]

    invalid_years = [
        '1', '', '000', '9900', '9999', '0000', '4500',
        '3402', '3111'
    ]
    for valid in valid_years:
        assert year_pattern.search(valid), f'{valid} is a valid year'
        assert all_date_pattern.search(valid), f'{valid} is a valid year'

    for invalid in invalid_years:
        assert not year_pattern.search(invalid), f'{invalid} is an invalid year'
        assert not all_date_pattern.search(invalid), f'{invalid} is an invalid year'


@log_pass_fail
def test_date_formats():
    valid_dates = [
        # %Y-%m-%d
        '1994-12-29',
        # %Y-%M-%d
        '1994-December-29',
        # %Y-%B-%d
        '1994-Dec-29',

        # %B-%d-%Y
        'Dec-29-1994',

        # %d-%B-%Y
        '29-Dec-1994',

        '29th December 1994',
        '1st March 1999',
        '2nd July 2000',
        '3rd May 2000',
        'November 29, 1971',
        'Mar 29, 1971'
    ]
    for date in valid_dates:
        assert date_pattern.search(date.lower()), f'{date} is a valid format'
        assert all_date_pattern.search(date.lower()), f'{date} is a valid format'


@log_pass_fail
def test_extra_dates():
    verbose_dates = [
        'today', 'yesterday', 'tomorrow', 'Today',
        'year', 'month', 'decade', 'century', 'week', 'millenium',
        'Last year',
        'Next  month',
        'this   Century',
        'next millEnium',
    ]

    for v in verbose_dates:
        verbose_pattern.search(v.lower()), f'{v} is a valid verbose date'
        all_date_pattern.search(v.lower()), f'{v} is a valid verbose date'


@log_pass_fail
def test_days_verbose():
    days = [
        ' Sunday ', ' Monday', 'last wednesday', 'next Saturday', 'This thursday',
        'friday', 'Thursday'
    ]

    for d in days:
        assert verbose_days_pattern.search(d.lower()), f'{d} is a valid verbose day'
        assert all_date_pattern.search(d.lower()), f'{d} is a valid verbose day'


@log_pass_fail
def test_bc_year():
    assert False, "not implemented"


@log_pass_fail
def test_x0s_years():
    years = [
        '90s', '80s', '70s'
    ]
    for y in years:
        assert verbose_years_pattern.search(y), f'{y} is valid'
        assert all_date_pattern.search(y), f'{y} is valid'


@log_pass_fail
def test_day_month():
    cases = [
        '29th of December', 'December 29', '29 December', '29th December', 'December 29th'
    ]
    for case in cases:
        assert day_month_pattern.search(case.lower()), f'{case} is valid'
        assert all_date_pattern.search(case.lower()), f'{case} is valid'

    invalids = [
        '214 November', '00 November', '00th November', '22rd January',
        '3th February', 'september 00', '2st march', '1rd Dec', '3nd April',
        'may 3nd',
        'june 2th',
        'july 1th',
    ]

    for inv in invalids:
        assert not day_month_pattern.search(inv.lower()), f'{inv} is invalid'
        assert not all_date_pattern.search(inv.lower()), f'{inv} is invalid'


@log_pass_fail
def test_misc():
    dates = [
        '213 BC', '7th Century', '5th century B.C.', '29th December',
    ]
    for d in dates:
        assert all_date_pattern.search(d.lower()), f'{d} should be valid'
    assert False, 'not implemented'


def main():
    test_year_formats()
    test_date_formats()
    test_extra_dates()
    test_days_verbose()
    test_day_month()
    test_misc()
    test_bc_year()
    test_x0s_years()
    print()
    print(f'{bcolors.BOLD}{total} TOTAL', bcolors.ENDC)
    print(f'{bcolors.OKGREEN}{passed} PASSED', bcolors.ENDC)
    print(f'{bcolors.FAIL}{failed} FAILED', bcolors.ENDC)

    print()
    if not failed_logs:
        return
    print('----------------------------')
    print('FAILS DETAIL')
    print('----------------------------')
    print()
    for fname, trace in failed_logs:
        print(bcolors.FAIL+'FAILED', fname, bcolors.ENDC)
        print('.................')
        print(trace)
        print()


if __name__ == '__main__':
    main()
