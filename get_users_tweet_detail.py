import json
import requests
from requests.adapters import HTTPAdapter

from api import *
from formatter import *
import os
from pathlib import Path
# 定义一个函数来提取箭头后面方括号内的字段


def extract_first_items_from_file(file_path):
    print(file_path)
    result = []
    user_id = []
    try:
        # 打开文件并逐行读取
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 找到箭头的位置
                arrow_index = line.find('->')
                if arrow_index != -1:
                    # 提取箭头左边的内容
                    left_part = line[:arrow_index].strip()
                    if left_part.startswith('[') and left_part.endswith(']'):
                        # 去除方括号
                        left_content = left_part[1:-1]
                        # 按逗号分隔内容，取第一项
                        left_first_item = left_content.split(
                            ',')[0].strip().strip("'")
                    else:
                        left_first_item = None

                    # 提取箭头右边的内容
                    right_part = line[arrow_index + 2:].strip()
                    if right_part.startswith('[') and right_part.endswith(']'):
                        # 去除方括号
                        right_content = right_part[1:-1]
                        # 按逗号分隔内容，取第一项
                        right_first_item = right_content.split(
                            ',')[0].strip().strip("'")
                    else:
                        right_first_item = None

                    # 将结果添加到列表中
                    if left_first_item and right_first_item:
                        result.append((left_first_item, right_first_item))

                # 打印提取的结果
            for left, right in result:
                if left != "ROOT":
                    user_id.append(left)
                user_id.append(right)
            # print(user_id)
            user_id = set(user_id)
            print(len(user_id))
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")

    return user_id


file_name = "500378223977721856"
file_dir = f"data/twitter16/{file_name}.txt"
user_ids = extract_first_items_from_file(file_dir)

root = "result"

folder_path = Path(f"{root}/{file_name}")


def main():
    folder_path.mkdir(exist_ok=True)
    with open("config.json", "r") as f:
        config = json.load(f)
    s = requests.Session()
    s.timeout = (3, 5)
    s.headers.update(config["headers"])
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    print("get_tweet_detail")
    res = get_tweet_detail(s, file_name)
    for item in res:
        if item.get("errors"):
            print(f"获取推文详情时出现错误: {file_name}")
            # error.append(file_name)
            continue

    # 保存原始数据
    with open(f"{folder_path}/tweet{file_name}_detail_raw.json", "w") as f:
        json.dump(res, f, indent=2)

    if res is None:
        # error.append(file_name)
        print("This Post is from a suspended account. Learn more")
    i = 0
    all_detail = []
    for detail in res:
        # 格式化数据
        tweet_and_commlist = tweet_detail_formatter(detail)
        if tweet_and_commlist is None:
            continue
        tweet = tweet_and_commlist["tweet"]
        comment_list = tweet_and_commlist["comment_list"]
        if i == 0:
            all_detail.append({"tweet": tweet})
        all_detail.append({"comment_list": comment_list})
    # 保存格式化后的数据
    with open(f"{folder_path}/tweet{file_name}_detail.json", "w") as f:
        json.dump(all_detail, f, indent=2)

    print("get_retweeters")
    res = get_retweeters(s, file_name)
    with open(f"{folder_path}/retweeters_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    all_retweeters = []
    for retweeter in res:

        res = retweeters_formatter(retweeter)
        all_retweeters.append(res)
    with open(f"{folder_path}/retweeters.json", "w") as f:
        json.dump(all_retweeters, f, indent=2)

    print("get_tweet_quotes")
    res = get_tweet_quotes(s, file_name)
    # print(res)
    all_quotes = []
    with open(f"{folder_path}/quotes_raw.json", "w") as f:
        json.dump(res, f, indent=2)
    for quote in res:
        # print(quote)
        res = tweet_quotes_formatter(quote)
        all_quotes.append(res)
    with open(f"{folder_path}/quotes.json", "w") as f:
        json.dump(all_quotes, f, indent=2)
    user_and_followers_info = {}
    user_and_following_info = {}
    user_and_followers_id = {}
    user_and_following_id = {}
    for fields in user_ids:
        follower_ids = []
        followers_info = []
        following_ids = []
        followings_info = []
        print("get_user_info_by_id")
        # fields="1182947209"
        # fields="318889294"
        # fields="972651"
        print(fields)
        res = get_user_tweets(s, fields)
        with open(f"{folder_path}/user{fields}_tweets_raw.json", "w") as f:
            json.dump(res, f, indent=2)
        if not res["data"]["user"] or res["data"]["user"]["result"]["__typename"] == "UserUnavailable":
            print(res)
            continue
        res = user_tweets_formatter(res)
        if res == None:
            print("This Post is from a suspended account. Learn more")
            continue
        with open(f"{folder_path}/user{fields}_tweets.json", "w") as f:
            json.dump(res, f, indent=2)
        screen_name = res[0]["user"]["user_name"]
        print("screen_name:", screen_name)
        user_info = get_user_by_screen_name(s, screen_name)
        with open(f"{folder_path}/user{fields}_by_screen_name_raw.json", "w") as f:
            json.dump(user_info, f, indent=2)
        user_info = user_formatter(user_info["data"]["user"]["result"])
        with open(f"{folder_path}/user{fields}_by_screen_name.json", "w") as f:
            json.dump(user_info, f, indent=2)

        print("get_followings")
        res_followings = get_followings(s, fields)
        for following in res_followings:
            res = followings_formatter(following)
            for i in res:
                following_ids.append(i["user_id"])
                followings_info.append(i)
        user_and_following_info[fields] = followings_info
        user_and_following_id[fields] = following_ids

        print("get_followers")
        res_followers = get_followers(s, fields)
        for follower in res_followers:
            res = followers_formatter(follower)
            for i in res:
                follower_ids.append(i["user_id"])
                followers_info.append(i)

        user_and_followers_info[fields] = followers_info
        user_and_followers_id[fields] = follower_ids
        with open(f"{folder_path}/following.json", "w") as f:
            json.dump(user_and_following_info, f, indent=2)
        with open(f"{folder_path}/followings_id.json", "w") as f:
            json.dump(user_and_following_id, f, indent=2)
        with open(f"{folder_path}/followers.json", "w") as f:
            json.dump(user_and_followers_info, f, indent=2)
        with open(f"{folder_path}/followers_id.json", "w") as f:
            json.dump(user_and_followers_id, f, indent=2)

    print("保存成功！")


if __name__ == "__main__":
    main()

