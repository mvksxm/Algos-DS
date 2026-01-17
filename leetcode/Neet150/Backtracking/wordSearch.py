class Solution:
    def exist(board: list, word: str) -> bool:

        word_len = len(word)

        def dfs(row, col, st:set, word_idx:int):

            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False

            if (row, col) in st:
                return False

            if board[row][col] != word[word_idx]:
                return False

            st.add((row, col))
            if board[row][col] == word[word_idx] and word_idx == word_len-1:
                st.remove((row, col))
                return True


            res = (dfs(row + 1, col,st, word_idx + 1) or
                   dfs(row - 1, col,st, word_idx + 1) or
                   dfs(row, col + 1,st, word_idx + 1) or
                   dfs(row, col - 1, st, word_idx + 1))

            st.remove((row, col))
            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, set(), 0):
                    return True

        return False


if __name__ == "__main__":
    print(Solution.exist([["a","b"],["c","d"]],"acdb" ))

