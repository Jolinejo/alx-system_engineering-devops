#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    import csv
    num = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    response = requests.get(api_url)
    name = response.json()["name"]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    response = requests.get(api_url)
    dicti = response.json()
    titles = []
    tasks = 0
    f = open('{}.csv'.format(num), 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for todo in dicti:
        row = [num]
        row.append(name)
        row.append(todo["completed"])
        row.append(todo["title"])
        writer.writerow(row)
    f.close()
