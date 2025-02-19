from .tweet_formatter import tweet_formatter


def tweet_detail_formatter(data: dict) -> dict:
    data = data["data"]["threaded_conversation_with_injections_v2"]["instructions"]
    entries = [x["entries"] for x in data if x["type"] == "TimelineAddEntries"][0]

    tweet = None
    comment_list = []

    for entry in entries:
        entry_type = entry["content"]["entryType"]
        match entry_type:

            case "TimelineTimelineItem":
                itemType = entry["content"]["itemContent"]["itemType"]
                if itemType == "TimelineTimelineCursor":
                    continue
                if itemType != "TimelineTweet":
                    print(f"unknown item type: {itemType}")
                    continue
                tweet = entry["content"]["itemContent"]["tweet_results"]["result"]
                tweet = tweet_formatter(tweet)

            case "TimelineTimelineModule":
                thread = entry["content"]["items"]
                for item in thread:
                    if item["item"]["itemContent"]["itemType"] != "TimelineTweet":
                        print(f"unknown item type: {item['item']['itemContent']['itemType']}")
                        continue
                    item = tweet_formatter(item["item"]["itemContent"]["tweet_results"]["result"])
                    comment_list.append(item)

            case _:
                print(f"unknown entry type: {entry_type}")
                continue

    return {
        "tweet": tweet,
        "comment_list": comment_list
    }

