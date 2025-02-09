from .tweet_formatter import tweet_formatter

def tweet_detail_formatter(data: dict) -> dict:
    data = data["data"]["threaded_conversation_with_injections_v2"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    tweet = [x for x in data if x["content"]["entryType"] == "TimelineTimelineItem"][0]
    tweet = tweet["content"]["itemContent"]["tweet_results"]["result"]
    tweet = tweet_formatter(tweet)
    comment_list = [] # TODO: Get comment list
    return {
        "tweet": tweet,
        "comment_list": comment_list
    }
