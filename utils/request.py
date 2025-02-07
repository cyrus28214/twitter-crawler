import requests
import json

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)
        if "headers" not in config:
            config["headers"] = {}
        if "User-Agent" not in config["headers"]:
            config["headers"]["User-Agent"] = DEFAULT_USER_AGENT
        return config

def get(url: str, params: dict) -> dict:
    config = load_config()
    response = requests.get(url, params=params, headers=config["headers"])
    return response.json()