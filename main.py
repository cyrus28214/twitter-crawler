import json
from api import *

def main():
    # 获取用户信息
    res = get_user_by_screen_name("elonmusk")
    print(json.dumps(res, indent=2))
    with open("examples/user_by_screen_name.json", "w") as f:
        json.dump(res, f, indent=2)

    # # 获取用户推文
    # res = get_user_tweets("44196397", 20)
    # print(json.dumps(res, indent=2))
    # with open("examples/user_tweets.json", "w") as f:
    #     json.dump(res, f, indent=2)

    # # 获取推文详情
    # res = get_tweet_detail("1883416606933680469")
    # print(json.dumps(res, indent=2))
    # with open("examples/tweet_detail.json", "w") as f:
    #     json.dump(res, f, indent=2)

    # # 获取引用推文
    # res = get_tweet_quotes("1883416606933680469")
    # print(json.dumps(res, indent=2))
    # with open("examples/tweet_quotes.json", "w") as f:
    #     json.dump(res, f, indent=2)

    # # 获取转发用户
    # res = get_retweeters("1883416606933680469")
    # print(json.dumps(res, indent=2))
    # with open("examples/retweeters.json", "w") as f:
    #     json.dump(res, f, indent=2)

    # 获取用户粉丝
    res = get_followers("44196397")
    print(json.dumps(res, indent=2))
    with open("examples/followers.json", "w") as f:
        json.dump(res, f, indent=2)
        
    # # 获取用户关注
    # res = get_followings("44196397")
    # print(json.dumps(res, indent=2))
    # with open("examples/followings.json", "w") as f:
    #     json.dump(res, f, indent=2)

if __name__ == "__main__":
    main() 