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
    source_id = None
    if data["legacy"]["is_quote_status"]:
        source_id = data["legacy"]["quoted_status_id_str"]
    source_tweet = data.get("quoted_status_result")
    if source_tweet:
        source_tweet = tweet_formatter(source_tweet["result"])
    tweet = {
        "post_id": data["rest_id"],
        "content": data["legacy"]["full_text"],
        "post_time": data["legacy"]["created_at"],
        "user_id": user["user_id"],
        "post_url": post_url,
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
