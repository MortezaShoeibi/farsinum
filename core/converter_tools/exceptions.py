"""
Number to text converter exceptions
"""

from rest_framework import status

from .numerical_units import ONES


ZERO_NUMBER_EXCEPTION: dict = {
    'status': status.HTTP_200_OK,
    'number': 0,
    'integers': 0,
    'decimals': f'0.{0}',
    'text': ONES[0]
}

NEGATIVE_ONLY_EXCEPTION: dict = {
    'status': status.HTTP_200_OK,
    'number': '-',
    'integers': None,
    'decimals': None,
    'text': 'منفی'
}
