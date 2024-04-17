#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
 listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        print("None")
        return

    children = data['data']['children']
    for child in children:
        print(child['data']['title'])
