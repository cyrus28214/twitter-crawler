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