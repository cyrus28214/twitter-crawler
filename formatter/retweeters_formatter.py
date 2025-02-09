from .user_formatter import user_formatter
from .user_list_formatter import user_list_formatter

def retweeters_formatter(data: dict) -> list:
    data = data["data"]["retweeters_timeline"]["timeline"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    return user_list_formatter(data)