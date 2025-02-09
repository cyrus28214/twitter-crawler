def user_formatter(data: dict) -> dict:
    res = {
        "user_id": data["rest_id"],
        "name": data["legacy"]["name"],
        "user_name": data["legacy"]["screen_name"],
        "user_description": data["legacy"]["description"],
        "created_at": data["legacy"]["created_at"],
        "user_url": f'https://x.com/{data["legacy"]["screen_name"]}',
        "followers_count": data["legacy"]["followers_count"],
        "following_count": data["legacy"]["friends_count"],
        "previous_post_count": data["legacy"]["statuses_count"],
        "location": data["legacy"]["location"]
    }
    return res