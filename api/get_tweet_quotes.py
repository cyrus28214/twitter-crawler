import json
import requests
import time

url = 'https://x.com/i/api/graphql/KI9jCXUx3Ymt-hDKLOZb9Q/SearchTimeline'
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

def get_tweet_quotes(session: requests.Session, tweet_id: str) -> list:
    all_quotes = []
    cursor = None
    base_count = 100  # 每次请求的基本数量
    
    
    while True:
        # 构建请求参数
        variables = {
            "rawQuery": f"quoted_tweet_id:{tweet_id}",
            "count": base_count,
            "querySource": "tdqt",
            "product": "Top",
            "requestContext": "tdqt"
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

        # 添加速率控制
        time.sleep(1.8)  # 基础请求间隔
        
        response = session.get(
            url,
            params=params,
            proxies=proxies,
            timeout=15
        )
        
        # 处理速率限制
        if response.status_code == 429:
            reset_time = int(response.headers.get('x-rate-limit-reset', time.time() + 900))
            wait_time = max(reset_time - int(time.time()), 300)
            print(f"触发速率限制，等待 {wait_time//60} 分钟")
            time.sleep(wait_time)
            continue
        if response.status_code == 401:
            print("请求次数太多，IP被封禁！！")
            break 
        response.raise_for_status()
        
        # 解析JSON响应
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("响应内容不是有效JSON")
            print("原始响应:", response.text[:500])
            break

        # 提取推文条目
        entries = []
        try:
            instructions = data['data']['search_by_raw_query']['search_timeline']['timeline']['instructions']
            for instruction in instructions:
                if instruction['type'] == 'TimelineAddEntries':
                    entries = instruction['entries']
                    break
        except KeyError as e:
            print(f"响应结构异常: {str(e)}")
            break

        # 提取分页游标和引用推文
        next_cursor = None
        new_quotes = 0
        
        for entry in entries:
            entry_id = entry.get('entryId', '')
            
            # 提取分页游标
            if entry_id.startswith('cursor-bottom-'):
                next_cursor = entry.get('content', {}).get('value')
                break

        print(f"累计 {len(all_quotes)} 条")
        
        # 终止条件
        if not next_cursor or next_cursor == cursor:
            print("分页结束")
            break
        all_quotes.append(response.json())    
        cursor = next_cursor
        print(f"下一页游标: {cursor}")
    return all_quotes
