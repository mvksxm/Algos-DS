# Approach
# Use SET as the Data Structure
# Space Complexity O(n), Time Complexity O(n)

def hasDuplicate(nums: list) -> bool:
    s = set()

    for n in nums:

        if n in s:
            return True

        s.add(n)

    return False


assert hasDuplicate([1, 2, 2]) == True
assert hasDuplicate([1, 2]) == False
assert hasDuplicate([1,3,2,0,3]) == True







