#!/usr/bin/python3
"""
script to get top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    fetches top ten hot posts from subreddit passed as an argument
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'api-request by Namasaka'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        res = res.json()
        posts = res['data']['children']
        # print the first 10 items
        for i in range(10):
            print(posts[i]['data']['title'])
    else:
        print('None')
