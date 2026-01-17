class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sus = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        # "MCMXCIV" 1000 + 900 + 90 +
        # "III"
        # "LVIII" # 50 +
        i = 0
        summa = 0
        while i < len(s):
            if i != len(s) - 1 and s[i] in sus and s[i + 1] in sus[s[i]]:
                summa = summa + (hashMap[s[i + 1]] - hashMap[s[i]])
                i += 2
            else:
                summa += hashMap[s[i]]
                i += 1

        return summa
