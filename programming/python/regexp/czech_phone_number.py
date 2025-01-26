import re
import pytest

pattern = r"""
    ^                # Začátek řetězce
    ((\+|00)420)?    # Mezinárodní předvolba, volitelně: + nebo 00
    \s*              # Libovolný počet mezer
    (\d{3})          # První trojčíslí
    \s*              # Libovolný počet mezer
    (\d{3})          # Druhé trojčíslí
    \s*              # Libovolný počet mezer
    (\d{3})          # Třetí trojčíslí
    $                # Konec řetězce
"""
pattern_inline = r"^((\+|00)420)?(\s*(\d{3})){3}$"

czech_phone_regex = re.compile(pattern, re.VERBOSE)
czech_phone_regex_inline = re.compile(pattern_inline, re.VERBOSE)


def is_valid_czech_phone_number(phone_number):
    return bool(czech_phone_regex.match(phone_number))


def is_valid_czech_phone_number_inline(phone_number):
    return bool(czech_phone_regex_inline.match(phone_number))


def test_valid_czech_phone_numbers():
    valid_numbers = [
        "123456789",
        "123 456 789",
        "+420123456789",
        "+420 123 456 789",
        "00420 123 456 789"
    ]
    for number in valid_numbers:
        assert is_valid_czech_phone_number(number), f"Should match: {number}"
        assert is_valid_czech_phone_number_inline(number), f"Should match: {number}"


def test_invalid_czech_phone_numbers():
    invalid_numbers = [
        "1234567890",             # Nesprávná délka
        "+42012345",              # Příliš krátké
        "+421 123 456 789",       # Špatná mezinárodní předvolba
        "+420 123 456 789 123",   # Více trojic
        "1234567891a",            # Obsahuje písmeno
        "123-456-789",            # Nepovolené znaky
        "+ 123 456 789"           # Nepovolené znaky
    ]
    for number in invalid_numbers:
        assert not is_valid_czech_phone_number(
            number), f"Should not match: {number}"
        assert not is_valid_czech_phone_number_inline(
                number), f"Should not match: {number}"

if __name__ == "__main__":
    pytest.main()
