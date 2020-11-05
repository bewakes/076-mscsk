import re

from typing import List

months: List[str] = [
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december']

months_short: List[str] = [x[:3] for x in months]

year_format: str = r'(19)|(20)\d{2}'
