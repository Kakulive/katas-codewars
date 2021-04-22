# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:
# solution(1000) # should return 'M'
# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.
# More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

#Działa, ale toporne
# def solution(n):
    # roman = []
    # if n >= 1000:
    #     roman.append(n//1000*"M")
    #     n = n % 1000
    # if n >= 900:
    #     roman.append("CM")
    #     n = n - 900
    # if n >= 500:
    #     roman.append(n//500*"D")
    #     n = n % 500
    # if n >= 400:
    #     roman.append("CD")
    #     n = n - 400
    # if n >= 100:
    #     roman.append(n//100*"C")
    #     n = n % 100
    # if n >= 90:
    #     roman.append("XC")
    #     n = n - 90
    # if n >= 50:
    #     roman.append(n//50*"L")
    #     n = n % 50
    # if n >= 40:
    #     roman.append("XL")
    #     n = n - 40
    # if n >= 10:
    #     roman.append(n//10*"X")
    #     n = n % 10
    # if n >= 9:
    #     roman.append("IX")
    #     n = n - 9
    # if n >= 5:
    #     roman.append(n//5*"V")
    #     n = n % 5
    # if n >= 4:
    #     roman.append("IV")
    #     n = n - 4
    # if n >= 1:
    #     roman.append(n//1*"I")
    # print("".join(roman))


roman_numbers = {'M':1000, 'CM':900, 'D':500, 'CD':400,'C':100, 'XC' :90, 'L':50, 'XL':40,'X':10, 'IX' :9, 'V':5, 'IV':4, 'I':1}
def solution(n):
    output = ''
    for roman in roman_numbers:
        r = n // roman_numbers[roman]
        output += roman*r
        n = n % roman_numbers[roman]
    return output





