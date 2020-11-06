import re
from functools import reduce


def add_this_last_next(times):
    return reduce(
        lambda a, x: [*a, *[f'({y} )? *{x}' for y in ['this', 'last', 'next']]],
        times,
        []
    )


months = [
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december'
]

days = [
    'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
]
days_regex = '|'.join(days) + '|'.join(add_this_last_next(days))

days_short = [d[:3] for d in days]
days_short_regex = '|'.join(days)

days_verbose_pattern = re.compile(f'{days_regex}|{days_short_regex}')

days_numbered = [f'{x:02}' for x in range(1, 33)] + [str(x) for x in range(1, 10)]
days_numbered_regex = '|'.join(days_numbered)

months_numbered = [f'{x:02}' for x in range(1, 13)] + [str(x) for x in range(1, 10)]
months_numbered_regex = '|'.join(months_numbered)


months_regex = '|'.join(months)

months_short = [m[:3] for m in months]
months_short_regex = '|'.join(months_short)

all_months_regex = f'{months_regex}|{months_short_regex}|{months_numbered_regex}'

year_regex = r'((1[1-9])|(2[0-9]))\d{2}'
year_pattern = re.compile(year_regex)

date_regex_ymd = f'({year_regex})[- /]+({all_months_regex})[- /]+({days_numbered_regex})'
date_regex_mdy = f'({all_months_regex})[- /]+({days_numbered_regex})[- /]+({year_regex})'
date_regex_dmy = f'({days_numbered_regex})[- /]+({all_months_regex})[- /]+({year_regex})'
date_regex_d_th_my = f'((1|2)?(1st|2nd|3rd|[4-9]th))[- /]+({all_months_regex})[- /]+({year_regex})'

all_date_regex = f'({date_regex_ymd})|({date_regex_mdy})|({date_regex_dmy})|({date_regex_d_th_my})'

verbose_dates = [
    'today', 'yesterday', 'tomorrow',
    *add_this_last_next(['year', 'month', 'decade', 'century', 'week', 'millenium'])
]
verbose_dates_regex = '|'.join(verbose_dates)

verbose_pattern = re.compile(verbose_dates_regex)

date_pattern = re.compile(all_date_regex)
