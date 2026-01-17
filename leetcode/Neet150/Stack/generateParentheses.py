class Solution:
    def generateParenthesis(n: int) -> set:

        pairs = set()

        def dfs(cnt_open, cnt_closed, string):
            if (cnt_open - cnt_closed) == (n*2 - (cnt_open + cnt_closed)):
                to_close = (n*2 - (cnt_open + cnt_closed))
                for i in range(to_close):
                    string += ")"
                pairs.add(string)
                return

            if cnt_closed > cnt_open:
                return

            dfs(cnt_open + 1, cnt_closed, string + "(") # ()(())
            dfs(cnt_open,  cnt_closed + 1, string + ")")

        dfs(1,0, "(")


        return list(pairs)

print(Solution.generateParenthesis(1))


#              3
#         /    |     \
#        1     2     3
#       /  \   |
#      1    2  1
#      |
#      1


#                  (
#                /    \
#                )     (
#               /       \
#              (         (
#              / \         \
#             )  (         )
#             /   \         \
#            (     )         )
#           /       \         \
#          )        )          )