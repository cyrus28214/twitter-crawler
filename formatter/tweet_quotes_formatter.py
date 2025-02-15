from .tweet_formatter import tweet_formatter


def tweet_quotes_formatter(data: dict) -> dict:
    data = data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"]
    for instruction in data:
        if instruction["type"] == "TimelineAddEntries":
            data = instruction["entries"]
            break
    res = []
    for x in data:
        if x["content"]["entryType"] != "TimelineTimelineItem":
            continue
        x = x["content"]["itemContent"]["tweet_results"]["result"]
        x = tweet_formatter(x)
        res.append(x)
    return res

