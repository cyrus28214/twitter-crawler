# twitter-crawler

To install dependencies:

```bash
pip install requests
```
## Data

data文件夹下有制作的小数据集twitter15，16
其中twitter16/tree为完整数据集

## Code

To run:

Create a new file `config.json` and add your headers to it:

```json5
{
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "authorization": "Bearer ******",
        "Cookie": "auth_token=******; ct0=******;",
        "x-csrf-token": "******",
	    "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    },
    // if need proxy, add this
    "proxies": { 
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
}
```

You can get them from your browser after your login x.com.

Create a new folder `result`

运行结果将存储在该文件夹下

Then run the script:

```bash
python get_users_tweet_detail.py
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

## TODO

还有一些功能未实现：

- 获取某个用户的所有推文（分页）
- 获取某个推文的所有评论
- 获取用户某段时间内的推文
- 用户id为151945897调用get_user_tweet.py时，tweet_fomatter有问题
