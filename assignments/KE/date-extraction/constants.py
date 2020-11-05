import re

months = [
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december'
]

months_short = [m[:3] for m in months]

year_pattern = re.compile(r'\b((1[1-9]|(2[0-9]))\d{2})(\b|[^0-9])')

date_pattern = re.compile('')
