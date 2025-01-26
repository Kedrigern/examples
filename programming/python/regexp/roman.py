"""
Roman number module. Convert number from int to roman, or from roman to in. Check if string is correct roman number
Greatly inspired by awesome book Divide into Python 3
"""

import re

roman_numeral_map = (
    ('M',  1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC', 90),
    ('L',  50),
    ('XL', 40),
    ('X',  10),
    ('IX', 9),
    ('V',  5),
    ('IV', 4),
    ('I',  1))

def is_roman_number(roman: str) -> bool:
    reg = """
        ^
        M{0,3}                   # thousands
        (CM|CD|C{0,3}|D?C{0,3})  # hundreds
        (XC|XL|L?X{0,3})         # dozens
        (IX|IV|V?I{0,3}|)
        $
        """
    if re.search(reg, roman, re.VERBOSE):
        return True
    else:
        return False

def to_roman(number: int, verbose: bool = False) -> str:
    """Return roman number (string) from integer.

    >>> [to_roman(s) for s in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)]
    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
    >>> to_roman(3999)
    'MMMCMXCIX'
    >>> to_roman(-1)
    Traceback (most recent call last):
        ...
    ValueError: Roman number cannot be negative.
    """
    if number < 0:
        raise ValueError("Roman number cannot be negative.")
    if number == 0:
        raise ValueError("Roman number cannot be 0.")
    if number > 3999:
        raise ValueError("Roman number cannot be higher than 3999.")

    result: str = ""
    n: int = number

    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            if verbose:
                print(f"Substracting {integer} from input, adding {numeral} to output")

    if verbose:
        print(f"{number} = {result}")
    return result

def from_roman(roman: str, verbose: bool = False) -> int:
    """Return integer from roman number.

    >>> [from_roman(s) for s in ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI")]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    >>> from_roman("MMMCMXCIX")
    3999
    >>> from_roman("i")
    Traceback (most recent call last):
        ...
    ValueError: String '' does not match any roman number
    """
    if not is_roman_number(roman):
        raise ValueError(f"String '' does not match any roman number")

    result: int = 0
    index: int = 0
    for numeral, integer in roman_numeral_map:
        while roman[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            if verbose:
                print(f"Found {numeral} of length {len(numeral)} adding {integer}")
    if verbose:
        print(f"{roman} = {result}")
    return result

if __name__ == "__main__":
    to_roman(98)
    to_roman(1234, True)
    from_roman("MMCD", True)
    from_roman("MMCMLIX", True)
    from_roman("MMCMLIIi")
