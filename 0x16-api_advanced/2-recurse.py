#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    # Construct the URL to query the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Define custom User-Agent header to avoid being blocked by Reddit
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Set parameters for the API request, including the 'after' parameter for
    # pagination
    params = {'after': after} if after else {}

    # Send HTTP GET request to Reddit API
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    # Check if the response status code is not 200 (indicating a successful
    # request)
    if response.status_code != 200:
        # If the request was not successful, return None
        return None

    # Parse the JSON response data
    data = response.json()
    # Check if the response data contains the necessary structure
    if 'data' not in data or 'children' not in data['data']:
        # If the structure is not as expected, return None
        return None

    # Extract the list of children (posts) from the response data
    children = data['data']['children']
    # Iterate over each post in the list of children
    for child in children:
        # Append the title of the post to the hot_list
        hot_list.append(child['data']['title'])

    # Get the 'after' parameter from the response data for pagination
    after = data['data']['after']
    # If there are more pages of results (i.e., the 'after' parameter is not
    # None)
    if after is not None:
        # Recursively call the recurse function with the updated 'after'
        # parameter
        recurse(subreddit, hot_list, after)

    # Return the hot_list after all pages have been processed
    return hot_list


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
