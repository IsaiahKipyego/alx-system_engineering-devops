#!/usr/bin/python3
"""
query number of subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    gets number of subscribers in subreddit given as an arg
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'api-test by Namasaka'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    # parse if request is successful
    if res.status_code == 200:
        res = res.json()
        return (res['data']['subscribers'])
    return 0
