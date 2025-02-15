# twitter-crawler

To install dependencies:

```bash
pip install requests
```
##Data

data文件夹下有制作的小数据集twitter15，16
其中twitter16/tree为完整数据集
##Code
To run:

Update the file `config.json` and add your headers to it:

```json
{
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "authorization": "Bearer ******",
        "Cookie": "auth_token=******; ct0=******;",
        "x-csrf-token": "******",
		"Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
}
```

You can get them from your browser after your login x.com.

Then run the script:

```bash
python get_users_tweet_detail.py
```
##Result

运行结果存储在result文件夹
每个推文及其用户相关信息存储在以推文ID命名的文件夹下

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
##TODO

还有一些功能未实现：

- 获取某个用户的所有推文（分页）
- 获取某个推文的所有推文
- 获取用户某段时间内的推文
