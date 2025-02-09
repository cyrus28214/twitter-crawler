from .tweet_formatter import tweet_formatter

def tweet_quotes_formatter(data: dict) -> dict:
    data = data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    res = []
    for x in data:
        if x["content"]["entryType"] != "TimelineTimelineItem":
            continue
        x = x["content"]["itemContent"]["tweet_results"]["result"]
        x = tweet_formatter(x)
        res.append(x)
    return res
