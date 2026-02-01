from typing import Callable

class Tester:

    def array_test(self, test_list: list, func_to_test: Callable) -> bool:

        results = []
        for case in test_list:
            res = func_to_test(*case[0])
            is_success = res == case[1]
            results.append([is_success, res])

        failed_cnt = 0
        for i in range(len(results)):
            if not results[i][0]:
                failed_cnt += 1
                print(f"Failed Test Case -> Test Data: {test_list[i][0]}; Intended Result: {test_list[i][1]}; Returned Result: {results[i][1]}")

        if failed_cnt > 0:
            print(f"{failed_cnt} out of {len(test_list)} tests failed!")
            return False

        print("All Test Cases passed!")
        return True
