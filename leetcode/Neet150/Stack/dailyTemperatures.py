
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach
# Iterate through temperatures and add their indexes to the stack, in case, if stack is empty or value under the current
# index is smaller than the value under the index that is located on top of the stack. Otherwise, in case, if value under
# the current idx is bigger than the value under the index on top of the stack - iterate through the stack backwards and
# pop values that are smaller. On each pop - update the temperatures array by executing the following formula -
# tempertatures[smaller_idx] = i - smaller_idx. Once the index was reached in the stack, whose value is bigger than of
# the value under the current idx - add current idx on top of the stack.
# In the end, in case, if any values were left in the stack, we can assume that they left unaddressed during the main iteration,
# so we should pop all the indexes and set values under them to 0.

class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:

        stack = []

        for i in range(len(temperatures)):
            if (stack and temperatures[stack[-1]] >= temperatures[i]) or not stack:
                stack.append(i)
            elif stack and temperatures[stack[-1]] < temperatures[i]:
                greater_value = temperatures[i]
                while stack and temperatures[stack[-1]] < greater_value:
                    smaller_idx = stack.pop()
                    temperatures[smaller_idx] = i - smaller_idx
                stack.append(i)

        while stack:
            left_idx = stack.pop()
            temperatures[left_idx] = 0

        return temperatures



if __name__ == "__main__":
    sln = Solution()
    print(sln.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

# print(Solution.dailyTemperatures([30,38,30,36,35,40,28]))
# print(Solution.dailyTemperatures([22,21,20]))