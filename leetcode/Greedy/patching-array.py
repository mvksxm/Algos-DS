# Personal Solution
from airflow.utils.timezone import convert_to_utc


def minPatches(nums: list, n: int) -> int:
    number_cnt = {}
    last_value = None
    solutions = set()
    nums_added = 0





    # Populate a dictionary with indexes
    for num in nums:
        if num in number_cnt:
            number_cnt[num] += 1
        else:
            number_cnt[num] = 1

    for range_num in range(1, n+1):
        if range_num in number_cnt:
            last_value = range_num

        if range_num not in number_cnt and not last_value:
            nums_added += 1
            last_value = range_num
            number_cnt[range_num] = 1

        if range_num not in number_cnt and last_value:
            range_num_subs = range_num - last_value

            if range_num_subs in number_cnt:
                if range_num_subs == last_value and number_cnt[last_value] == 1:
                    nums_added += 1
                    last_value = range_num
                    number_cnt[range_num] = 1
                    continue

                solutions.add(range_num)
            elif range_num_subs not in solutions:
                nums_added += 1
                last_value = range_num
                number_cnt[range_num] = 1


    return nums_added


if __name__ == "__main__":
    test_arr1 = [1,3]
    n1 = 6
    print(minPatches(test_arr1, n1))

    test_arr2 = [1,5,10]
    n2 = 20
    print(minPatches(test_arr2, n2))










