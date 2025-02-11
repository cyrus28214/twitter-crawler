from .tweet_formatter import tweet_formatter

def tweet_detail_formatter(data: dict) -> dict:
    data = data["data"]["threaded_conversation_with_injections_v2"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    
    # 获取主推文
    tweet = [x for x in data if x["content"]["entryType"] == "TimelineTimelineItem"][0]
    tweet = tweet["content"]["itemContent"]["tweet_results"]["result"]
    tweet = tweet_formatter(tweet)
    
    # 获取评论列表
    comment_list = []
    for entry in data:
        if entry["content"]["entryType"] != "TimelineTimelineModule":
            continue
        thread = entry["content"]["items"]
        thread = [
            tweet_formatter(x["item"]["itemContent"]["tweet_results"]["result"])
            for x in thread
            if x["item"]["itemContent"]["itemType"] == "TimelineTweet"
        ]
        comment_list.append(thread)
        
    return {
        "tweet": tweet,
        "comment_list": comment_list
    }
