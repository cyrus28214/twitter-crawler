# twitter-crawler

To install dependencies:

```bash
pip install requests
```

To run:

Create a new file `config.json` and add your headers to it:

```json
{
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "authorization": "Bearer ******",
        "Cookie": "auth_token=******; ct0=******;",
        "x-csrf-token": "******"
    }
}
```

You can get them from your browser after your login x.com.

Then run the script:

```bash
python main.py
```

## important fields

Use search to find them.

Tweet:

- `full_text`: The text of the tweet.
- `view.count`
- `bookmark_count`
- `favorite_count`: The number of likes.
- `reply_count`
- `quote_count` and `repost_count`: They add up to the total number of retweets.
- `created_at`

User:

- `rest_id`
- `name`
- `screen_name`
- `description`
- `followers_count`
- `friends_count`: The number of followings.
- `created_at`