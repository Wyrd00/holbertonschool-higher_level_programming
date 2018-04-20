#!/usr/bin/python3
def roman_to_int(roman_string):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        if isinstance(roman_string, str) is False or roman_string is None:
                return 0

        temp = dic.get(roman_string[0])
        for i in range(1, len(roman_string)):
                if temp >= dic.get(roman_string[i]):
                        total += temp
                        temp = dic.get(roman_string[i])
                else:
                        total -= temp
                        temp = dic.get(roman_string[i])
        total += dic.get(roman_string[-1])
        return total
