from constants import year_pattern, date_pattern
from functools import reduce
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
        '1700', '1123', '1500\'s', '1643', '1809', '1888', '1999', '1994', '1543',
        '2020', '2021', '2000s', '2111', '2100'
    ]

    invalid_years = [
        '1', '', '000', '111111', '121121212', '9900', '9999', '0000', '4500',
        '3402', '3111'
    ]
    for valid in valid_years:
        m = year_pattern.match(valid)
        assert m, f'{valid} is a valid year'
        assert m.group(1) == valid[:5]

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
        '1st March 1994',
        '2nd July 2000',
        '3rd May 2000',
    ]
    for date in valid_dates:
        date_pattern.match(date), f'{date} is a valid format'


def add_this_last_next(times):
    return reduce(
        lambda a, x: [*a, *[f'{y} {x}' for y in ['this', 'last', 'next']]],
        times,
        []
    )


@log_pass_fail
def test_extra_dates():
    dates = [
        'today', 'yesterday', 'tomorrow',
        *add_this_last_next([
            'year', 'month', 'decade', 'century', 'week', 'millenium'
        ]),
    ]
    assert False, "not implemented test"


def main():
    test_year_formats()
    test_date_formats()
    test_extra_dates()
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
