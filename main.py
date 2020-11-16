class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        arabic = 0
        for digit in range(len(s)):
            if digit > 0 and roman[s[digit]] > roman[s[digit - 1]]:
                arabic += roman[s[digit]] - 2 * roman[s[digit - 1]]
            else:
                arabic += roman[s[digit]]
        return arabic
