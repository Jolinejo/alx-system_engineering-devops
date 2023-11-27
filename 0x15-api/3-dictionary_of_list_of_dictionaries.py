#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    import json
    to_json = {}
    for num in range(1, 11):
        api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
        response = requests.get(api_url)
        name = response.json()["username"]
        long_url = "https://jsonplaceholder.typicode.com/users/"
        api_url = "{}{}/todos".format(long_url, num)
        response = requests.get(api_url)
        dicti = response.json()
        titles = []
        for todo in dicti:
            task = {}
            task["task"] = todo["title"]
            task["completed"] = todo["completed"]
            task["username"] = name
            titles.append(task)
        to_json[num] = titles
    with open("todo_all_employees.json", 'w+') as f:
        json.dump(to_json, f)
