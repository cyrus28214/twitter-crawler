from .tweet_formatter import tweet_formatter


def tweet_detail_formatter(data: dict) -> dict:
    data = data["data"]["threaded_conversation_with_injections_v2"]["instructions"]
    for instruction in data:
        if instruction["type"] == "TimelineAddEntries":
            data = instruction["entries"]
            break
    # 获取主推文
    tweet = {}
    for instruction in data:
        if instruction["content"]["entryType"] == "TimelineTimelineItem":
            print(1)
            tweet = instruction
            break

    if tweet == {}:
        return None
    tweet = tweet["content"]["itemContent"]["tweet_results"]["result"]
    tweet = tweet_formatter(tweet)
    if tweet == None:
        return None
    # 获取评论列表
    comment_list = []
    for entry in data:
        if entry["content"]["entryType"] != "TimelineTimelineModule":
            continue
        thread = entry["content"]["items"]
        thread = [
            tweet_formatter(x["item"]["itemContent"]
                            ["tweet_results"]["result"])
            for x in thread
            if x["item"]["itemContent"]["itemType"] == "TimelineTweet"
        ]
        comment_list.append(thread)

    return {
        "tweet": tweet,
        "comment_list": comment_list
    }

