import json
import requests
import pandas as pd

#Read token from file
def read_token():
    token = ''
    with open('../token', 'r') as f:
        token = f.read()
    return token

#Read repo from file
def read_repo():
    repo = ''
    with open('../repourl', 'r') as f:
        repo = f.read()
    return repo

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
        #url = "https://api.github.com/repos/yatinappsmith/TestCaseRepo/issues"
        url = read_repo()
        headers = {'Content-Type': 'application/vnd.github.VERSION.raw+json', 'Authorization': 'token ' + token}
        data = {'title': self.test_case_title, 'body': "### Steps\n" + self.test_case_steps + '\n### Expected behaviour\n'
                        + self.test_case_expected_result, 'labels': self.test_case_labels}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.text)



if __name__ == "__main__":
    print("Complete")
    test_case = TestCase()
    df = pd.read_csv ('FE pod - JS Editor enhancement.csv')
    #loop through each line in the csv file
    for index, row in df.iterrows():
        test_case = TestCase()
        test_case.set_test_case_title(row['Steps'])
        test_case.add_test_case_steps(row['Steps'])
        test_case.add_test_case_expected_result(row['Expected Result'])
        test_case.add_test_case_labels(row['Type of test case'])
        test_case.add_test_case_labels("Manual")
        test_case.add_test_case_labels("JS Editor")
        print(test_case.test_case_title)
        test_case.add_test_case_to_github()
        dbg = 1
