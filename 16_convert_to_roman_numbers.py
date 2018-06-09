# Convert a nubmers to a roman

rnt = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
]


def convert_to_roman(number):

    roman_numerals = ''
    for roman, num in rnt:
        if number >= num:
            count = number // num
            number -= count * num
            roman_numerals += roman * count
    return roman_numerals


print convert_to_roman(2159)

