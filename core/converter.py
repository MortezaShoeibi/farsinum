"""
Numbers to Persian text based format
"""

from rest_framework import status

from .converter_tools.numerical_units import (
    ONES,
    TENS,
    HUNDREDS,
    THOUSANDS
)
from .converter_tools.tools import (
    number_validator,
    number_grouper
)
from .converter_tools.errors import (
    NONE_NUMERICAL_DATA_ERROR,
    NUMBER_TOO_LARGE_ERROR,
    INVALID_DATA_ERROR
)
from .converter_tools.exceptions import  (
    ZERO_NUMBER_EXCEPTION,
    NEGATIVE_ONLY_EXCEPTION
)


class StringedNumber(str):
    """
    StringedNumber mixed number and string data
    """

    def __init__(self, number: str):
        
        if type(number).__name__ != 'str':
            number: str = str(number)
        
        if not number_validator(number):
            return INVALID_DATA_ERROR

        self.is_negative: bool = '-' in number
        
        self.group: list = number.split('.')
        
        self.integers, self.decimals = (self.group[0], '0') if len(self.group) == 1 else self.group



class ConvertNumberToText():
    """
    Converts numbers to Persian text.
    """

    def __init__(self):
        # define arrays for number to text converter
        self.ones: dict = ONES
        self.tens: dict = TENS
        self.hundreds: dict = HUNDREDS
        self.thousands: dict = THOUSANDS
    

    def convert_number_to_text(self, number: str) -> dict:
        """Main converter"""

        if (number == '-'):
            return NEGATIVE_ONLY_EXCEPTION
        
        if (number == '.'):
            return NONE_NUMERICAL_DATA_ERROR

        result: dict = dict()
        number: StringedNumber = StringedNumber(number)
        is_negative: bool = number.is_negative
        integers: int = int(number.integers)
        decimals: str = number.decimals

        # check the decimal isn't too long.
        if len(decimals) > 12:
            decimals = decimals[:12]
        
        decimals = decimals.rstrip('0')
        if decimals == '':
            decimals = '0'

        # absolute value: |number|
        if is_negative:
            integers *= -1
        
        if integers >= (10 ** 36) :
            return NUMBER_TOO_LARGE_ERROR

        if (integers + int(decimals)) == 0:
            return ZERO_NUMBER_EXCEPTION

        # split number into groups of 3 digits
        integer_groups = number_grouper(integers)
        integer_groups_len = len(integer_groups)

        # convert each group of 3 digits to text
        text = ''

        if is_negative:
            text += 'منفی '
        
        for group in integer_groups:

            group = int(group)

            group_text = ''

            integer_groups_len -= 1

            jump = group == 0

            if group >= 100:
                hundreds_digit = int(group // 100)
                group_text += self.hundreds[hundreds_digit]
                group = group % 100
                if group != 0:
                    group_text += ' و '

            if group >= 20 or group == 10:
                tens_digit = int(group // 10)
                group_text += self.tens[tens_digit]
                group = group % 10
                if group != 0 :
                    group_text += ' و '

            if group >= 1 and group <= 19 :
                group_text += self.ones[group]
                
            text += group_text

            if not jump:
                text += ' ' + self.thousands[integer_groups_len]
                if integer_groups_len != 0:
                    text += ' و '
        
        if int(decimals) != 0:

            text += ' ' if integers == 0 else ' و '

            # split number into groups of 3 digits
            decimals_groups = number_grouper(decimals)
            decimals_groups_len = dgl = len(decimals_groups)

            for group in decimals_groups:

                group = int(group)

                group_text = ''

                decimals_groups_len -= 1

                jump: bool = group == 0

                if group >= 100:
                    hundreds_digit = int(group // 100)
                    group_text += self.hundreds[hundreds_digit]
                    group = group % 100
                    if group != 0:
                        group_text += ' و '

                if group >= 20 or group == 10:
                    tens_digit = int(group // 10)
                    group_text += self.tens[tens_digit]
                    group = group % 10
                    if group != 0:
                        group_text += ' و '

                if group >= 1 and group <= 19:
                    group_text += self.ones[group]
                    
                text += group_text

                if not jump:
                    text += ' ' + self.thousands[decimals_groups_len]
                    if decimals_groups_len != 0:
                        text += ' و '
            
            # ZERO WIDTH NON-JOINER - Codepoint: U+200C
            zwnj: str = '‌'  

            if dgl == 1:
                zwnj = ''

            if len(str(decimals_groups[0])) == 1:
                text += self.tens[1] + zwnj

            if len(str(decimals_groups[0])) == 2:
                text += self.hundreds[1] + zwnj

            if len(str(decimals_groups[0])) == 3:
                dgl += 1
            
            text += self.thousands[dgl - 1] + 'م'

        # Clean up text by removing any extra spaces
        text = text.strip(' ')

        if text[-1] == 'و' and text[-2] == 'د':
            _text = text.replace('  ', ' ').strip(' ')
        else:
            _text = text.replace('  ', ' ').strip(' و ').strip(' ')

        result = {
            'status': status.HTTP_200_OK,
            'number': number,
            'integers': integers,
            'decimals': f'0.{decimals}',
            'text': _text
        }

        return result


def converter(number: str) -> dict:
    """
    Validates and converts a number
    to Persian text based format.\n
    returns an NONE_NUMERICAL_DATA_ERROR
    dictionary if the number is invalid.
    """

    if number_validator(number):
        model = ConvertNumberToText()
        response: dict = model.convert_number_to_text(number)
        return response
    
    return NONE_NUMERICAL_DATA_ERROR
