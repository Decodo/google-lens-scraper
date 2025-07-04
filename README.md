# Google Lens Scraper

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![License](https://img.shields.io/github/license/decodo/Google-News-scraper)

<p align="center">
<a href="https://dashboard.decodo.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://github.com/user-attachments/assets/60bb48bd-8dcc-48b2-82c9-a218e1e4449c"></a>
</p>

[![](https://dcbadge.vercel.app/api/server/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)


## What is Google Lens?
Google Lens is a visual search tool developed by Google that utilizes image recognition and AI to identify objects, text, and landmarks in photos or from your camera. It helps users extract information, translate text, find similar products, and more.

## What is a Google Lens scraper?
A Google Lens scraper is a tool that automates the process of sending image queries to Google Lens and extracting the resulting visual search data, such as object descriptions, similar images, product links, and translated text. This tool is useful for automating the extraction of image-based data at scale. It's ideal for product matching, reverse image search, translation, or visual content analysis. You can save time and effort compared to manually using Google Lens, especially when working with large datasets.

## Features
- **Customizable requests**. The API accepts various parameters, including geolocation and device type, to target and extract specific data. 
- **Real-time data**. Choose between synchronous or asynchronous requests for your targets.
- **Effortless integration**. Easily set up the scraper with dynamically generated code examples and easy API authentication.
- **Flexible output options**. Choose between raw HTML, structured JSON, or table formats to read and analyze data immediately.
- **Proxy integration**. Built-in 125+ residential proxies ensure you'll avoid blocks and CAPTCHAs.
- **Anti-bot bypass**. advanced techniques, such as browser fingerprinting, to overcome restrictions and appear as a genuine user, ensuring reliable access even on protected sites.
- **Risk-free**. Test before you buy on the API playground, get a 7-day free trial with 1K requests, and only pay for the data you need.
## Setup
### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Requests Python library](https://pypi.org/project/requests/)
- [Decodo's Web Scraping API Advanced plan](https://dashboard.decodo.com/web-scraping-api/scraper?target=google_lens)
### Installation
1. **Clone the repository**. Open the terminal, navigate to your target directory, and run the following command:
```
git clone https://github.com/Decodo/google-lens-scraper.git
```
2. **Open the ```google-lens-scraper.py``` file**. 
2. **Enter authentication credentials**. Go to the Decodo dashboard and copy the basic authentication token and add it to the ```authorization``` header.

![Google Lens scraper API](https://github.com/user-attachments/assets/8cdc9a9a-e127-4b9f-aa57-65e0b373096e)


4. **Customize the request**. Modify the payload to change parameters for parsing, JS rendering, device type, and browser.
```
payload = {
      "target": "google_lens", # Choose a target
      "query": "[your image URL]", # Enter the image URL to search with
      "headless": "html", # Remove this line to disable JS rendering
      "parse": True # Change to False to skip parsing
}
```
5. **Run the script**. Save the script file and run it with the following terminal command:
```
python google-lens-scraper.py
```
You can also modify the parameters and send a request directly from the dashboard to achieve the same results, thereby skipping the manual setup. 
## Usage examples
### Search using an image URL
Use an image URL to search for related images, pages, and other results.
```
import requests
  
url = "https://scraper-api.decodo.com/v2/scrape"
  
payload = {
      "target": "google_lens",
      "query": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQVpHoNY7fNuiiCf-fqZ0_6tz42XzNiqdK-R-XI-r_K-mAO3TnbuCKANshFwAZSGRpZMfVji1l7i3qFwYhjIznGzQ",
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
```

## Output
Example output result:
<img width="1282" alt="Google Lens scraper API" src="https://github.com/user-attachments/assets/9b317920-eabb-4709-bcef-794990bb18ea" />

## License
All code is released under the [MIT License](https://github.com/Decodo/Decodo/blob/master/LICENSE).
## Read more
🗺️ [Google Maps scraper](https://github.com/Decodo/google-maps-scraper)

📰 [Google News scraper](https://github.com/Decodo/Google-News-scraper)
