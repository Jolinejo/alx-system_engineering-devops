#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    num = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    response = requests.get(api_url)
    dicti = response.json()
    titles = []
    tasks = 0
    for todo in dicti:
        tasks = tasks + 1
        if todo["completed"] is True:
            titles.append(todo["title"])
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    response = requests.get(api_url)
    name = response.json()["name"]
    tot = len(titles)
    print("Employee {} is done with tasks({}/{}):".format(name, tot, tasks))
    for item in titles:
        print("\t {}".format(item))
