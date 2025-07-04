import requests
  
url = "https://scraper-api.decodo.com/v2/scrape"
  
payload = {
      "target": "google_lens",
      "query": "[image URL]",
      "headless": "html",
      "parse": True
}
  
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic [your basic auth token]"
}
  
response = requests.post(url, json=payload, headers=headers)
  
print(response.text)
