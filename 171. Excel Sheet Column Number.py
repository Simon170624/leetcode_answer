class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        sum = 0
        for exp, char in enumerate(columnTitle):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum