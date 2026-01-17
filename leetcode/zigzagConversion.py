class Solution:

    @staticmethod
    def convert(s: str, numRows: int) -> str:
        middle_amount = numRows - 2
        final_string = ""

        if numRows == 1:
            return s

        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    final_string += s[j]
                    j = j + numRows + middle_amount

            else:
                j = i
                while j < len(s):
                    string_in_column = s[j]
                    string_middle_index = j - (i * 2)

                    if string_middle_index > 0:
                        final_string += s[string_middle_index]

                    final_string += string_in_column
                    j = j + numRows + middle_amount

                # Last condition here
                string_middle_index = j - (i * 2)

                if string_middle_index < len(s):
                    final_string += s[string_middle_index]

        return final_string


if __name__ == "__main__":
    text = "A"
    cols = 1
    print(Solution.convert(text, cols))
