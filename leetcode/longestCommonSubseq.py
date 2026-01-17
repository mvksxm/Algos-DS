
# MY attmept
def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text1) >= len(text2):
        iterator_string = text1
        idle_string = text2
    else:
        iterator_string = text2
        idle_string = text1

    p2 = 0
    max_cnt = 0

    # for i in range(len(iterator_string)):
    #     if iterator_string[i] == idle_string[p]:
    # apache
    # chapa

    # nigga 5
    # ggnig
    while p2 < len(idle_string):  # len(5) += 1 +=1
        local_cnt = 0  # 2
        # print(p2)
        for i in range(len(iterator_string)):
            if idle_string[p2] == iterator_string[i]:
                # print(idle_string[p2])
                # print(iterator_string[i])
                local_cnt += 1
                p2 += 1

            if p2 == len(idle_string):
                break

        if local_cnt == 0: p2+=1
        max_cnt = max(local_cnt, max_cnt)

    return max_cnt

# Optimal Solution


if __name__ == "__main__":
    text1 = "hofubmnylkra"
    text2 = "pqhgxgdofcvmr"
    print(longestCommonSubsequence(text1, text2))
