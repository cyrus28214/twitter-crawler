from .user_formatter import user_formatter
from .user_list_formatter import user_list_formatter

def followers_formatter(data: dict) -> list:
    data = data["data"]["user"]["result"]["timeline"]["timeline"]["instructions"]
    data = [x for x in data if x["type"] == "TimelineAddEntries"][0]["entries"]
    return user_list_formatter(data)