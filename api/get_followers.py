import json
import requests
from util.request import request

url = 'https://x.com/i/api/graphql/OGScL-RC4DFMsRGOCjPR6g/Followers'

def get_followers(session: requests.Session, user_id: str) -> list:
    all_followers_raw = []
    cursor = None
    count = 100
    while True:
        variables = {
            "userId": user_id,
            "count": count,
            "includePromotedContent": False,
        }

        if cursor:
            variables["cursor"] = cursor
            
        params = {
            "variables": json.dumps(variables),
            "features": json.dumps({
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
       
        response = request(session, url, params=params)
        all_followers_raw.append(response) 
        
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
        if next_cursor.split("|")[0]=="0" and cursor.split("|")[0]=="0":
            print("爬取完毕")
            break
        
        cursor = next_cursor
        print(f"已获取 {len(all_followers_raw)} 页数据，下一页游标: {cursor}")
 
    return all_followers_raw
