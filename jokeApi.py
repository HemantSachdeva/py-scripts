#!/usr/bin/env python3

import requests
categories = {
    1: 'Programming',
    2: 'Misc',
    3: 'Dark',
    4: 'Pun',
    5: 'Spooky',
    6: 'Christmas',
}
for key, values in categories.items():
    print(f"{key}. {values}")
while category := input("Enter a joke category[1-6]: "):
    if not category.isdigit():
        print("Invalid input")
        continue

    category = int(category)
    if not (0 < category < 7):
        print('Invalid input')
        continue
    break
api_url = "https://v2.jokeapi.dev/joke/{}".format(categories[category])
resp = requests.get(api_url)
if not (200 <= resp.status_code < 300):
    exit(print("Cannot connect to server"))
resp = resp.json()
if resp.get("type") == 'single':
    print(resp.get("joke"))
else:
    print(resp.get("setup"))
    print(resp.get("delivery"))
