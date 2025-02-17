from .user_formatter import user_formatter

def user_list_formatter(data: dict) -> list:
    res = []
    for user in data:
        if user["content"]["entryType"] != "TimelineTimelineItem":
            continue
        # some of the user_result is `{}`, so use get
        user = user["content"]["itemContent"]["user_results"].get("result")
        if not user:
            continue
        formatter_user=user_formatter(user)
        if formatter_user:
            res.append(formatter_user)
    return res
