from .tweet_formatter import tweet_formatter

def user_tweets_formatter(data: dict) -> list:
    data = data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    res = []
    for x in data:
        if x["content"]["entryType"] != "TimelineTimelineItem":
            continue
        tweet = x["content"]["itemContent"]["tweet_results"]["result"]
        tweet = tweet_formatter(tweet)
        res.append(tweet)
    return res
