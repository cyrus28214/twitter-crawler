import json
import requests
import os
from requests.adapters import HTTPAdapter

from api import *
from formatter import *

def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    s = requests.Session()
    s.timeout = (3, 5)
    s.headers.update(config["headers"])
    if "proxies" in config:
        s.proxies.update(config["proxies"])
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))

    save_dir = "examples"
    os.makedirs(save_dir, exist_ok=True)
    
    # ===== get user by screen name =====
    user_res = get_user_by_screen_name(s, "zjuidg")
    with open(f"{save_dir}/user_by_screen_name_raw.json", "w") as f:
        json.dump(user_res, f, indent=2)
    user = user_formatter(user_res["data"]["user"]["result"])
    with open(f"{save_dir}/user_by_screen_name.json", "w") as f:
        json.dump(user, f, indent=2)

    # ===== get user tweets =====
    cursor = None
    i = 1
    tweets = []
    user_id = user["user_id"] # user_id from above user
    while True:
        res, cursor = get_user_tweets(s, user_id, cursor=cursor)
        # create directory if not exists
        os.makedirs(f"{save_dir}/user_tweets_raw", exist_ok=True)
        with open(f"{save_dir}/user_tweets_raw/{i}.json", "w") as f:
            json.dump(res, f, indent=2)
        res = user_tweets_formatter(res)
        if len(res) == 0 or cursor is None:
            break
        tweets.extend(res)
        i += 1
    with open(f"{save_dir}/user_tweets.json", "w") as f:
        json.dump(tweets, f, indent=2)

    # ===== get tweet detail =====
    cursor = None
    i = 1
    tweet_id = "1890673021376950749"
    tweet = None
    comment_list = []
    while True:
        res, cursor = get_tweet_detail(s, tweet_id, cursor=cursor)
        os.makedirs(f"{save_dir}/tweet_detail_raw", exist_ok=True)  
        with open(f"{save_dir}/tweet_detail_raw/{i}.json", "w") as f:
            json.dump(res, f, indent=2)
        res = tweet_detail_formatter(res)
        if i == 1: # set main tweet in the first iteration
            tweet = res["tweet"]
        comment_res = res["comment_list"]
        if len(comment_res) == 0 or cursor is None:
            break
        comment_list.extend(comment_res)
        i += 1
    with open(f"{save_dir}/tweet_detail.json", "w") as f:
        json.dump({"tweet": tweet, "comment_list": comment_list}, f, indent=2)
        
    # ===== get retweeters =====
    cursor = None
    i = 1
    retweeters = []
    while True:
        res, cursor = get_retweeters(s, tweet_id, cursor=cursor)
        os.makedirs(f"{save_dir}/retweeters_raw", exist_ok=True)
        with open(f"{save_dir}/retweeters_raw/{i}.json", "w") as f:
            json.dump(res, f, indent=2)
        res = retweeters_formatter(res)
        if len(res) == 0 or cursor is None:
            break
        retweeters.extend(res)
        i += 1
    with open(f"{save_dir}/retweeters.json", "w") as f:
        json.dump(retweeters, f, indent=2)

    # ===== get tweet quotes =====
    cursor = None
    i = 1
    quote_list = []
    while True:
        res, cursor = get_tweet_quotes(s, tweet_id, cursor=cursor)
        os.makedirs(f"{save_dir}/tweet_quotes_raw", exist_ok=True)
        with open(f"{save_dir}/tweet_quotes_raw/{i}.json", "w") as f:
            json.dump(res, f, indent=2)
        res = tweet_quotes_formatter(res)
        if len(res) == 0 or cursor is None:
            break
        quote_list.extend(res)
        i += 1
    with open(f"{save_dir}/tweet_quotes.json", "w") as f:
        json.dump(quote_list, f, indent=2)
    
    # print("get_followers")
    # res = get_followers(s, "44196397")
    # with open("examples/followers_raw.json", "w") as f:
    #     json.dump(res, f, indent=2)
    # res = followers_formatter(res)
    # with open("examples/followers.json", "w") as f:
    #     json.dump(res, f, indent=2)
        
    # print("get_followings")
    # res = get_followings(s, "44196397")
    # with open("examples/followings_raw.json", "w") as f:
    #     json.dump(res, f, indent=2)
    # res = followings_formatter(res)
    # with open("examples/followings.json", "w") as f:
    #     json.dump(res, f, indent=2)

if __name__ == "__main__":
    main() 