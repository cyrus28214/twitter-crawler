import fs from "fs/promises";

import { getUserByScreenName } from "./api/getUserByScreenName";
import { getUserTweets } from "./api/getUserTweets";
import { getTweetDetail } from "./api/getTweetDetail";
import { getTweetQuotes } from "./api/getTweetQuotes";
import { getRetweeters } from "./api/getRetweeters";

let res = await getUserByScreenName("elonmusk");
res = JSON.stringify(res, null, 2);
console.log(res);
// await fs.writeFile("examples/UserByScreenName.json", res);

res = await getUserTweets("44196397", 20);
res = JSON.stringify(res, null, 2);
console.log(res);
// await fs.writeFile("examples/UserTweets.json", res);

res = await getTweetDetail("1883416606933680469");
res = JSON.stringify(res, null, 2);
console.log(res);
// await fs.writeFile("examples/TweetDetail.json", res);

res = await getTweetQuotes("1883416606933680469");
res = JSON.stringify(res, null, 2);
console.log(res);
// await fs.writeFile("examples/TweetQuotes.json", res);

res = await getRetweeters("1883416606933680469");
res = JSON.stringify(res, null, 2);
console.log(res);
// await fs.writeFile("examples/Retweeters.json", res);