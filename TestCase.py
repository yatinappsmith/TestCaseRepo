

class TestCase:
    def __init__(self):
        self.test_case_title = ""
        self.test_case_steps = ""
        self.test_case_expected_result = ""
        self.test_case_labels = []

    def set_test_case_title(self, test_case_title):
        self.test_case_title = test_case_title

    def add_test_case_steps(self, test_case_steps):
        self.test_case_steps = self.test_case_steps + test_case_steps

    def add_test_case_expected_result(self, test_case_expected_result):
        self.test_case_expected_result = self.test_case_expected_result + test_case_expected_result

    def add_test_case_labels(self, test_case_labels):
        self.test_case_labels.append(test_case_labels)



if __name__ == "__main__":
    test_case = TestCase()
    test_case.set_test_case_title("Test Case Title")
    test_case.add_test_case_steps("Test Case Steps")
    test_case.add_test_case_expected_result("Test Case Expected Result")
    test_case.add_test_case_labels("Button Widget")
    test_case.add_test_case_labels("Entity Explorer")
    print(test_case.test_case_title)
    print(test_case.test_case_steps)
    print(test_case.test_case_expected_result)
    print(test_case.test_case_labels)
