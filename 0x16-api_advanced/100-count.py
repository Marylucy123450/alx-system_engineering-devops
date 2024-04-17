#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
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
        # Recursively call the count_words function with the updated 'after'
        # parameter
        count_words(subreddit, word_list, hot_list, after)
    else:
        # If there are no more pages of results, initialize an empty dictionary
        # to count occurrences of keywords
        word_count = {}
        # Iterate over each title in the hot_list
        for title in hot_list:
            # Iterate over each keyword in the word_list
            for word in word_list:
                # Check if the lowercase version of the keyword is present in
                # the lowercase version of the title
                if word.lower() in title.lower().split():
                    # Increment the count of the keyword in the word_count
                    # dictionary
                    word_count[word.lower()] = word_count.get(
                        word.lower(), 0) + 1

        # Sort the word_count dictionary by count in descending order and then
        # alphabetically by word
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        # Iterate over each keyword-count pair in the sorted_word_count list
        for word, count in sorted_word_count:
            # Print the keyword and its count
            print(f"{word}: {count}")


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    word_list = input("Enter list of keywords (separated by space): ").split()
    count_words(subreddit, word_list)
