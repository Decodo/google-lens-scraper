from pprint import pprint
import requests

url = "https://scraper-api.decodo.com/v2/scrape"

payload = {
      "target": "google_search",
      "query": "hand",
      "locale": "en-us",
      "geo": "United States",
      "device_type": "desktop_chrome",
      "domain": "com",
      "page_from": "1",
      "num_pages": "10",
      "google_results_language": "en",
      "google_tbm": "isch",
      "parse": True,
      "google_safe_search": True
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

pprint(data)