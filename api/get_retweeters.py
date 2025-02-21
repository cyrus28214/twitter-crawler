import json
import requests
from util.request import request
from util.get_cursor_from_instructions import get_cursor_from_instructions

url = 'https://x.com/i/api/graphql/8fXdisbSK0JGESmFrHcp1g/Retweeters'

def get_retweeters(session: requests.Session, tweet_id: str, count: int = 20, cursor: str = None) -> list:
    """
    Get retweeters of a tweet

    rate limit: 500/min
    """
    variables = {
        "tweetId": tweet_id,
        "count": count,
        "includePromotedContent": False
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
    instructions = data["data"]["retweeters_timeline"]["timeline"]["instructions"]
    next_cursor = get_cursor_from_instructions(instructions)
    
    return data, next_cursor