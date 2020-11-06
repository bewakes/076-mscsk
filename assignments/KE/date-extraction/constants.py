import re
from functools import reduce


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def compile_with_boundary(regexp):
    return re.compile(r'\b('+regexp+r')\b')


def add_this_last_next(times):
    return reduce(
        lambda a, x: [*a, *[f'{y} *{x}' for y in ['this', 'last', 'next']]],
        times,
        []
    )


def with_boundary(regexp):
    return r'\b'+regexp+r'\b'


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

verbose_days_regex = f'{days_regex}|{days_short_regex}'
verbose_days_pattern = compile_with_boundary(verbose_days_regex)

days_numbered = [f'{x:02}' for x in range(1, 33)] + [str(x) for x in range(1, 10)]
days_numbered_regex = '|'.join(days_numbered)

months_numbered = [f'{x:02}' for x in range(1, 13)] + [str(x) for x in range(1, 10)]
months_numbered_regex = '|'.join(months_numbered)

number_ordered_regex = '(1|2|3)?(1st|2nd|3rd|[4-9]th)'

months_regex = '|'.join(months)

months_short = [m[:3] for m in months]
months_short_regex = '|'.join(months_short)

all_months_regex = f'{months_regex}|{months_short_regex}|{months_numbered_regex}'

day_month_regex = '|'.join([
    f'(({months_regex}) *(({number_ordered_regex})|({days_numbered_regex})))',
    f'(({days_numbered_regex}) *({months_regex}))',
    f'(({days_numbered_regex})|({number_ordered_regex})) (of | *)({months_regex})',
])

day_month_pattern = compile_with_boundary(day_month_regex)

verbose_years_regex = '|'.join([f'{x}s' for x in range(10, 100, 10)])
verbose_years_pattern = compile_with_boundary(verbose_years_regex)

year_regex = r'((1[1-9])|(2[0-9]))\d{2}'
year_pattern = compile_with_boundary(year_regex)

date_regex_ymd = f'({year_regex})[- /]+({all_months_regex})[- /]+({days_numbered_regex})'
date_regex_mdy = f'({all_months_regex})[- /]+({days_numbered_regex})[- ,/]+({year_regex})'
date_regex_dmy = f'({days_numbered_regex})[- /]+({all_months_regex})[- /]+({year_regex})'
date_regex_d_th_my = f'({number_ordered_regex})[- /]+({all_months_regex})[- /]+({year_regex})'

all_date_regex = f'({date_regex_ymd})|({date_regex_mdy})|({date_regex_dmy})|({date_regex_d_th_my})'

verbose_dates = [
    'today', 'yesterday', 'tomorrow',
    *add_this_last_next(['year', 'month', 'decade', 'century', 'week', 'millenium'])
]
verbose_dates_regex = '|'.join(verbose_dates)

verbose_pattern = compile_with_boundary(verbose_dates_regex)

date_pattern = compile_with_boundary(all_date_regex)

all_date_regex = '|'.join(
    [f'({x})' for x in [
        all_date_regex,
        verbose_dates_regex,
        verbose_days_regex,
        verbose_years_regex,
        year_regex,
        day_month_regex,
    ]
    ])

all_date_pattern = compile_with_boundary(all_date_regex)
