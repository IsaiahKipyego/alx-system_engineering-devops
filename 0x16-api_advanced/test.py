#!/usr/bin/python3
"""
function to get top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    module gets top ten hot posts from subreddit passed as an argument
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'api-request by KIPYEGO'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        res = res.json()
        posts = res['data']['children']
        # print the first 10 items
        print(len(posts))
        print(res['data']['dist'])
        i = 1
        for post in posts:
            print('{}. {}'.format(i, post['data']['title']))
            i += 1
    else:
        print('None')
