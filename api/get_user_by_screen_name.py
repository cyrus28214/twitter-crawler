import json
import requests
from util.request import request
url = "https://x.com/i/api/graphql/32pL5BWe9WKeSK1MoPvFQQ/UserByScreenName"

def get_user_by_screen_name(session: requests.Session, screen_name: str) -> dict:
    params = {
        "variables": json.dumps({
            "screen_name": screen_name
        }),
        "features": json.dumps({
            "hidden_profile_subscriptions_enabled": True,
            "profile_label_improvements_pcf_label_in_post_enabled": True,
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "subscriptions_verification_info_is_identity_verified_enabled": True,
            "subscriptions_verification_info_verified_since_enabled": True,
            "highlights_tweets_tab_ui_enabled": True,
            "responsive_web_twitter_article_notes_tab_enabled": True,
            "subscriptions_feature_can_gift_premium": True,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True
        }),
        "fieldToggles": json.dumps({
            "withAuxiliaryUserLabels": False
        })
    }
    return request(session, url, params=params) 
