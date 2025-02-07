import json
from api.get_user_by_screen_name import get_user_by_screen_name
from api.get_user_tweets import get_user_tweets
from api.get_tweet_detail import get_tweet_detail
from api.get_tweet_quotes import get_tweet_quotes
from api.get_retweeters import get_retweeters

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

if __name__ == "__main__":
    main() 