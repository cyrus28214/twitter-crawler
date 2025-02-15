import requests
import json
import time
from datetime import datetime
url = 'https://x.com/i/api/graphql/o5eNLkJb03ayTQa97Cpp7w/Following'
proxies = {
    'http': 'http://127.0.0.1:7890',  # 替换为 Clash 中的 HTTP 代理地址和端口
    'https': 'http://127.0.0.1:7890'  # 替换为 Clash 中的 HTTPS 代理地址和端口
}
def get_followings(session: requests.Session, user_id: str) -> list:
    all_followings_raw = []
    cursor = None
    count = 50  # 每页最大数量
    max_retries=5
    retry_count=0
    while True:
        # 构建请求参数
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": False
        }
        if cursor:
            variables["cursor"] = cursor
            
        params = {
            "variables": json.dumps(variables),
            "features": json.dumps({
                # 保持原有features配置
                "profile_label_improvements_pcf_label_in_post_enabled": True,
                "rweb_tipjar_consumption_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "creator_subscriptions_tweet_preview_api_enabled": True,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "premium_content_api_read_enabled": False,
                "communities_web_enable_tweet_community_results_fetch": True,
                "c9s_tweet_anatomy_moderator_badge_enabled": True,
                "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
                "responsive_web_grok_analyze_post_followups_enabled": True,
                "responsive_web_jetfuel_frame": False,
                "responsive_web_grok_share_attachment_enabled": True,
                "articles_preview_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "responsive_web_twitter_article_tweet_consumption_enabled": True,
                "tweet_awards_web_tipping_enabled": False,
                "responsive_web_grok_analysis_button_from_backend": True,
                "creator_subscriptions_quote_tweet_preview_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
                "rweb_video_timestamps_enabled": True,
                "longform_notetweets_rich_text_read_enabled": True,
                "longform_notetweets_inline_media_enabled": True,
                "responsive_web_grok_image_annotation_enabled": True,
                "responsive_web_enhance_cards_enabled": False
            })
        }
        
        # 发送请求
        response = session.get(url, params=params, proxies=proxies)
        remaining_requests = int(response.headers.get('x-rate-limit-remaining', 1))
        reset_timestamp = int(response.headers.get('x-rate-limit-reset', time.time() + 900))
            
        print(f"剩余请求次数: {remaining_requests}, 限制重置时间: {datetime.fromtimestamp(reset_timestamp)}")
        # 解析响应
        if response.status_code == 429:
                wait_seconds = max(reset_timestamp - int(time.time()), 180)  # 至少等待5分钟
                print(f"触发速率限制，等待 {wait_seconds//60} 分 {wait_seconds%60} 秒")
                time.sleep(wait_seconds)
                retry_count += 1
                if retry_count > max_retries:
                    print("超过最大重试次数")
                    break
                continue
        if response.status_code == 401:
            print("请求次数太多，IP被封禁！！")
            break
        response=response.json()
        entries = []
        try:
            instructions = response['data']['user']['result']['timeline']['timeline']['instructions']
            for instruction in instructions:
                if instruction['type'] == 'TimelineAddEntries':
                    entries = instruction['entries']
                    break
        except KeyError:
            break
        
        # 处理分页
        next_cursor = None
        for entry in entries:
            entry_id = entry.get('entryId', '')       
            # 提取分页游标
            if entry_id.startswith('cursor-bottom-'):
                next_cursor = entry.get('content', {}).get('value')
        all_followings_raw.append(response) 
        if next_cursor.split("|")[0]=="0" and cursor.split("|")[0]=="0":
            print("爬取完毕")
            break
        
        cursor = next_cursor
        print(f"已获取 {len(all_followings_raw)} 页数据，下一页游标: {cursor}")
    
    return all_followings_raw
