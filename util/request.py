import requests
import time
from datetime import datetime

def request(session: requests.Session, *args, **kwargs) -> dict:
    while True:
        response = session.get(*args, **kwargs)

        remaining = response.headers.get('x-rate-limit-remaining')
        reset_timestamp = response.headers.get('x-rate-limit-reset')

        if remaining is None or reset_timestamp is None:
            raise Exception("Rate limit not found")
        
        remaining = int(remaining)
        reset_timestamp = int(reset_timestamp)

        url_no_params = args[0].split('?')[0]
        print(f"URL: {url_no_params}")
        print(f"Status code: {response.status_code}")
        print(f"Remaining requests for this API endpoint: {remaining}")
        print(f"Reset timestamp: {datetime.fromtimestamp(reset_timestamp)}")
        print()

        if response.status_code == 429:
            wait_seconds = max(reset_timestamp - time.time(), 10)
            print(f"Rate limit exceeded. Waiting for {wait_seconds:.1f} seconds.")
            time.sleep(wait_seconds)
            continue
        
        # if it is not json, throw an error
        try:
            res = response.json()
        except:
            print(response.text[:500])
            raise Exception("Response is not json")
        
        return res

