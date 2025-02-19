import requests
import time
from datetime import datetime

def request(session: requests.Session, *args, **kwargs) -> dict:
    while True:
        response = session.get(*args, **kwargs)

        remaining = response.headers.get('x-rate-limit-remaining')
        reset_timestamp = response.headers.get('x-rate-limit-reset')

        if remaining == None or reset_timestamp == None:
            raise Exception("Rate limit not found")

        print(f"Status code: {response.status_code}")
        print(f"Remaining requests for this API endpoint: {remaining}")
        print(f"Reset timestamp: {datetime.fromtimestamp(int(reset_timestamp))}")

        if response.status_code == 429:
            wait_seconds = reset_timestamp - int(time.time())
            print(f"Rate limit exceeded. Waiting for {wait_seconds} seconds.")
            time.sleep(wait_seconds)
            continue
        
        if response.status_code == 401:
            raise Exception("Too many requests, IP is blocked")
        
        # if it is not json, throw an error
        try:
            res = response.json()
        except:
            print(response.text[:500])
            raise Exception("Response is not json")
        
        return res

