from typing import Callable

class Tester:

    def array_test(self, test_list: list, func_to_test: Callable) -> bool:

        results = [func_to_test(case[0]) == case[1] for case in test_list]

        if not all(results):
            print("Testing failed!")
            failed_cnt = 0
            for i in range(len(results)):
                if not results[i]:
                    failed_cnt += 1
                    print(f"Failed Test Case -> Test Data: {test_list[i][0]}; Intended Result: {test_list[i][1]}")

            print(f"{failed_cnt} out of {len(test_list)} tests failed!")
            return False

        print("All Test Cases passed!")
        return True
