"""
Converter tools pack which includes:\n
1-Data casting functions and tools\n
2-Validators
"""


def number_grouper(number: int) -> list:
    """
    Splits a number into groups of 3 digits
    """

    number_str, groups = str(number), list()

    while number_str:
        groups.append(number_str[-3:])
        number_str = number_str[:-3]
    
    groups.reverse()
    return groups


# * * Validators * *

def number_validator(number: str | int | float) -> bool:
    """
    Validates a number digits
    """

    if number == '':
        return False

    stringed_number: str = str(number)
    valid_chars: list = list('-0.123456789')

    for char in stringed_number:
        if char not in valid_chars:
            return False
        
    if '-' in number:
        if number.index('-') != 0:
            return False
        
    return False if (len(number.split('.')) - 1) > 1 else True
