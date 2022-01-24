"""
Homework: Roman Kata Assignment
"""
# Part I

numerals = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
            "XL": 40, "L": 50, "XC": 90, "C": 100, "D": 500, "M": 1000}

# for k,v in numerals.items()
# print(k,v)


def convert_numerals(input_number):
    range_flag = None
    for symbol, integer in numerals.items():
        if integer == input_number:
            return symbol
        if input_number > integer:
            range_flag = symbol

    remaining = input_number - numerals[range_flag]
    return range_flag + convert_numerals(remaining)


print(convert_numerals(484))


# Part II
num_symbol = input("Write a roman numeral: ")
x = input()

digits = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
          "XL": 40, "L": 50, "XC": 90, "C": 100, "D": 500, "M": 1000}
answer = 0


for i in range(len(num_symbol)):
    if i+1 != len(num_symbol) and digits[num_symbol[i]] < digits[num_symbol[i+1]]:
        answer = answer - digits[num_symbol[i]]

    else:
        answer = answer + digits[num_symbol[i]]


print(num_symbol)
print("This is:", answer)
