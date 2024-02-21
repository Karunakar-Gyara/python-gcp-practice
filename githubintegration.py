import requests

data_git = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")

user_data=data_git.json()

for i in range(len(user_data)):
    print(user_data[i]["user"]["login"])