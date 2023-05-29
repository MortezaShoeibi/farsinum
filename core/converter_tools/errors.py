"""
Number to text converter error messages
"""

from rest_framework import status


NONE_NUMERICAL_DATA_ERROR: dict = {
    'status': status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    'error': 'Unsupported media type',
    'description': 'Your entered data is not a number'
}

NUMBER_TOO_LARGE_ERROR: dict = {
    'status': status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
    'error': 'Entity Too Large',
    'description': 'Your entered data is too large'
}

NO_DATA_SENT_ERROR: dict = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': 'Bad request',
    'description': 'No data were sent'
}

INVALID_DATA_ERROR: dict = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': 'Bad request',
    'description': 'Invalid data'
}
