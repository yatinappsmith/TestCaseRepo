import json
import requests
import pandas as pd
import time

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
        #exit(0)
        while True:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            print(response.text)
            responsetext = response.text
            #if responsetext == "You have exceeded a secondary rate limit and have been temporarily blocked from content creation. Please retry your request again later.":
            if "rate limit" in responsetext:
                time.sleep(60)
            else:
                break

        #dbg =1



if __name__ == "__main__":
    test_case = TestCase()
    df = pd.read_csv ('TeamManagers_pod - Generate SSH.csv')
    #loop through each line in the csv file
    for index, row in df.iterrows():
        test_case = TestCase()
        test_case.set_test_case_title(row['Test Case Number'] + " - " + row['Steps'])
        test_case.add_test_case_steps(row['Steps'])
        test_case.add_test_case_expected_result(row['Expected Result'])
        test_case.add_test_case_labels(row['Type (Negative / Positive)'])
        test_case.add_test_case_labels("Manual")
        #test_case.add_test_case_labels("Automated")
        test_case.add_test_case_labels("Git Version Control" )
        test_case.add_test_case_labels("Generate ssh key")
        #test_case.add_test_case_labels(row['Type of test case'])
        print(test_case.test_case_title)
        test_case.add_test_case_to_github()
        #sleep for 1 second
        #time.sleep(5)
        dbg = 1
