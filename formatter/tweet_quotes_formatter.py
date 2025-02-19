from .tweet_formatter import tweet_formatter


def tweet_quotes_formatter(data: dict) -> dict:
    entries = []
    instructions = data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"]
    for instruction in instructions:
        if instruction["type"] == "TimelineAddEntries":
            entries = instruction["entries"]
            break
    res = []
    for entry in entries:
        if entry["content"]["entryType"] != "TimelineTimelineItem":
            continue
        tweet = entry["content"]["itemContent"]["tweet_results"]["result"]
        tweet = tweet_formatter(tweet)
        res.append(tweet)
    return res

