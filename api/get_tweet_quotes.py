import json
import requests
import time

from util.request import request
url = 'https://x.com/i/api/graphql/KI9jCXUx3Ymt-hDKLOZb9Q/SearchTimeline'

def get_tweet_quotes(session: requests.Session, tweet_id: str, count: int = 20, cursor: str = None) -> list:
    variables = {
        "rawQuery": f"quoted_tweet_id:{tweet_id}",
        "count": count,
        "querySource": "tdqt",
        "product": "Top",
        "requestContext": "tdqt"
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
    data = request(session, url, params=params)

    next_cursor = None

    instructions = data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"]

    for instruction in instructions:
        if instruction["type"] != "TimelineAddEntries":
            continue
        entries = instruction["entries"]
        for entry in entries:
            if entry["content"]["entryType"] == "TimelineTimelineCursor" and entry["content"]["cursorType"] == "Bottom":
                next_cursor = entry["content"]["value"]
                break
    return data, next_cursor
            
