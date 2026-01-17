class Solution:
    def dailyTemperatures(temperatures: list) -> list:
        stack = []
        output_arr = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stack:
                for j in range(len(stack)-1, -1, -1):
                    stack_elem = stack[j]

                    if stack_elem[1] < temperatures[i]:
                        stack.pop(j)
                        output_arr[stack_elem[0]] = i - stack_elem[0]
                    else:
                        break

            stack.append((i, temperatures[i]))

        return output_arr




print(Solution.dailyTemperatures([30,38,30,36,35,40,28]))
print(Solution.dailyTemperatures([22,21,20]))