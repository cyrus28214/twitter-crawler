# twitter-crawler

To install dependencies:

```bash
bun install
```

To run:

Create a new file `config.ts` and copy the headers from your browser to it:

```ts
export const headers = {
    "authorization": "Bearer ******",
    "Cookie": 'auth_token=******; ct0=******; ',
    "x-csrf-token": "******"
};
```

Then run the script:

```bash
bun run index.ts
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