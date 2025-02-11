import json
import requests
from requests.adapters import HTTPAdapter

from api import *
from formatter import *

def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    s = requests.Session()
    s.timeout = (3, 5)
    s.headers.update(config["headers"])
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    
    print("get_user_by_screen_name")
    res = get_user_by_screen_name(s, "elonmusk")
    with open("examples/user_by_screen_name_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = user_formatter(res["data"]["user"]["result"])
    with open("examples/user_by_screen_name.json", "w") as f:
        json.dump(res, f, indent=2)

    print("get_user_tweets")
    res = get_user_tweets(s, "44196397", 20)
    with open("examples/user_tweets_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = user_tweets_formatter(res)
    with open("examples/user_tweets.json", "w") as f:
        json.dump(res, f, indent=2)

    print("get_tweet_detail")
    res = get_tweet_detail(s, "1887535165603561505")
    # res = get_tweet_detail(s, "1887872220279554140")
    with open("examples/tweet_detail_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = tweet_detail_formatter(res)
    with open("examples/tweet_detail.json", "w") as f:
        json.dump(res, f, indent=2)
        
    print("get_retweeters")
    res = get_retweeters(s, "1883416606933680469")
    with open("examples/retweeters_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = retweeters_formatter(res)
    with open("examples/retweeters.json", "w") as f:
        json.dump(res, f, indent=2)

    print("get_followers")
    res = get_followers(s, "44196397")
    with open("examples/followers_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = followers_formatter(res)
    with open("examples/followers.json", "w") as f:
        json.dump(res, f, indent=2)
        
    print("get_followings")
    res = get_followings(s, "44196397")
    with open("examples/followings_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    res = followings_formatter(res)
    with open("examples/followings.json", "w") as f:
        json.dump(res, f, indent=2)

if __name__ == "__main__":
    main() 