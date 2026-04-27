import requests
import json

def load_rules(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json()
    except:
        return {
            "work_periods": [],
            "blacklist": [],
            "warning_minutes": 10,
            "messages": {}
        }
