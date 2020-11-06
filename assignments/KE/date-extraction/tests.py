from constants import year_pattern, date_pattern, verbose_pattern, days_verbose_pattern
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
            print('PASSED', '................', f.__name__)
            return r
        except AssertionError:
            failed += 1
            print('FAILED', '................', f.__name__)
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
        m = year_pattern.match(valid)
        assert m, f'{valid} is a valid year'

    for invalid in invalid_years:
        assert not year_pattern.match(invalid), f'{invalid} is an invalid year'


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
    ]
    for date in valid_dates:
        assert date_pattern.match(date.lower()), f'{date} is a valid format'


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
        verbose_pattern.match(v.lower()), f'{v} is a valid verbose date'


@log_pass_fail
def test_days_verbose():
    days = [
        'Sunday', ' Monday', 'last wednesday', 'next Saturday', 'This thursday',
        'friday', 'Thursday'
    ]

    for d in days:
        assert days_verbose_pattern.match(d.lower()), f'{d} is a valid verbose day'


def main():
    test_year_formats()
    test_date_formats()
    test_extra_dates()
    test_days_verbose()
    print()
    print('TOTAL', total)
    print('PASSED', passed)
    print('FAILED', failed)

    print()
    print('----------------------------')
    print('FAILS DETAIL')
    print('----------------------------')
    print()
    for fname, trace in failed_logs:
        print('FAILING', fname)
        print('.................')
        print(trace)
        print()


if __name__ == '__main__':
    main()
