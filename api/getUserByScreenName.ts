import { get } from "../utils/request";

const url = "https://x.com/i/api/graphql/32pL5BWe9WKeSK1MoPvFQQ/UserByScreenName";

export async function getUserByScreenName(screenName: string) {
    const params = {
        variables: {
            "screen_name": screenName
        },
        features: {
            "hidden_profile_subscriptions_enabled":true, 
            "profile_label_improvements_pcf_label_in_post_enabled":true, 
            "rweb_tipjar_consumption_enabled":true,
            "responsive_web_graphql_exclude_directive_enabled":true,
            "verified_phone_label_enabled":false,
            "subscriptions_verification_info_is_identity_verified_enabled":true,
            "subscriptions_verification_info_verified_since_enabled":true,
            "highlights_tweets_tab_ui_enabled":true,
            "responsive_web_twitter_article_notes_tab_enabled":true,
            "subscriptions_feature_can_gift_premium":true,
            "creator_subscriptions_tweet_preview_api_enabled":true,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,
            "responsive_web_graphql_timeline_navigation_enabled":true
        },
        fieldToggles: {
            "withAuxiliaryUserLabels":false
        }
    };
    return await get(url, params);
}
