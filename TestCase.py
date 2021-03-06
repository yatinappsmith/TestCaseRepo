import json
import requests

#Read token from file
def read_token():
    token = ''
    with open('token', 'r') as f:
        token = f.read()
    return token

class TestCase:
    def __init__(self):
        self.test_case_title = ""
        self.test_case_steps = ""
        self.test_case_expected_result = ""
        self.test_case_labels = []

    def set_test_case_title(self, test_case_title):
        self.test_case_title = "[TestCase] " + test_case_title

    def add_test_case_steps(self, test_case_steps):
        self.test_case_steps = self.test_case_steps + test_case_steps

    def add_test_case_expected_result(self, test_case_expected_result):
        self.test_case_expected_result = self.test_case_expected_result + test_case_expected_result

    def add_test_case_labels(self, test_case_labels):
        self.test_case_labels.append(test_case_labels)

    def add_test_case_to_github(self):
        token = read_token()
        #url = 'https://api.github.com/repos/' + token + '/' + self.test_case_title + '/issues'
        url = "https://api.github.com/repos/yatinappsmith/TestCaseRepo/issues"
        headers = {'Content-Type': 'application/vnd.github.VERSION.raw+json', 'Authorization': 'token ' + token}
        data = {'title': self.test_case_title, 'body': "### Steps\n" + self.test_case_steps + '\n### Expected behaviour\n'
                        + self.test_case_expected_result, 'labels': self.test_case_labels}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.text)



if __name__ == "__main__":
    test_case = TestCase()
    test_case.set_test_case_title("Python Test Case Title")
    test_case.add_test_case_steps("Python Test Case Steps")
    test_case.add_test_case_expected_result("Test Case Expected Result")
    test_case.add_test_case_labels("Button Widget")
    test_case.add_test_case_labels("Entity Explorer")
    print(test_case.test_case_title)
    print(test_case.test_case_steps)
    print(test_case.test_case_expected_result)
    print(test_case.test_case_labels)
    #test_case.add_test_case_to_github()


