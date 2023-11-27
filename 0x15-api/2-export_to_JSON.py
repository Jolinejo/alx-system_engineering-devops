#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    import json
    num = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    response = requests.get(api_url)
    name = response.json()["username"]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    response = requests.get(api_url)
    dicti = response.json()
    titles = []
    tasks = 0
    for todo in dicti:
        task = {}
        task["task"] = todo["title"]
        task["completed"] = todo["completed"]
        task["username"] = name
        titles.append(task)
    to_json = {}
    to_json[num] = titles
    with open("{}.json".format(num), 'w+') as f:
        json.dump(to_json, f)
