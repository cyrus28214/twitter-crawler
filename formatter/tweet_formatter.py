import sys
from .user_formatter import user_formatter


def tweet_formatter(data: dict) -> dict:
    """
    ```
    return {
        "tweet": tweet,
        "user": user,
        "source_tweet": source_tweet
    }
    ```
    """
    if data["__typename"] == "TweetWithVisibilityResults":
        data = data["tweet"]
    else:
        assert data["__typename"] == "Tweet"
    user = user_formatter(data["core"]["user_results"]["result"])
    post_url = f"https://x.com/{user['user_name']}/status/{data['rest_id']}"
    
    is_quote = "quoted_status_result" in data
    is_retweet = "retweeted_status_result" in data["legacy"]
    
    if is_quote:
        source_tweet = tweet_formatter(data["quoted_status_result"]["result"])
        source_id = source_tweet["tweet"]["post_id"]
    elif is_retweet:
        source_tweet = tweet_formatter(data["legacy"]["retweeted_status_result"]["result"])
        source_id = source_tweet["tweet"]["post_id"]
    else:
        source_tweet = None
        source_id = None

    tweet = {
        "post_id": data["rest_id"],
        "content": data["legacy"]["full_text"],
        "post_time": data["legacy"]["created_at"],
        "user_id": user["user_id"],
        "post_url": post_url,
        "is_quote": is_quote,
        "is_retweet": is_retweet,
        "source_id": source_id,
        "like_count": data["legacy"]["favorite_count"],
        "bookmark_count": data["legacy"]["bookmark_count"],
        "reply_count": data["legacy"]["reply_count"],
        "quote_count": data["legacy"]["quote_count"],
        "retweet_count": data["legacy"]["retweet_count"],
        "rec_count": data["views"]["count"],
    }
    return {
        "tweet": tweet,
        "user": user,
        "source_tweet": source_tweet
    }
