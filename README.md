# Google Images Scraper

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![License](https://img.shields.io/github/license/decodo/Google-News-scraper)

<p align="center">
<a href="https://dashboard.decodo.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://github.com/user-attachments/assets/60bb48bd-8dcc-48b2-82c9-a218e1e4449c"></a>
</p>

[![](https://dcbadge.vercel.app/api/server/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)

## What is Google Images? 
[Google Images](https://images.google.com/) is a search engine feature that helps users find visual content, such as photographs, illustrations, and graphics, from across the web. It’s one of the most widely used tools for locating images online, offering results from billions of indexed web pages. 

## What is a Google Images scraper? 
Decodo’s Google Images scraper is a dedicated API designed to simplify the data-gathering process from Google Images. It handles all the complexities, such as rotating proxies, bypassing CAPTCHAs, and parsing the data into a structured format. This means you don't have to worry about technical challenges or extensive coding. 

## What data does this scraper return? 
- The **domain** where the image is hosted; 
- A **direct link** to the image; 
- The **destination URL** that the image links to; 
- The image’s **position** in the result page; 
- The image’s **global position** across all pages; 
- The page **title** or **snippet** associated with the image. 

## Features 
- **Image search scraping**. Retrieve image metadata and links directly from Google Images. 
- **Keyword-based targeting**. Customize search queries with any keyword input. 
- **Device emulation**. Simulate various browser and device behavior for realistic user-agent headers. 
- **Structured output**. Get clean, ready-to-use results in JSON and CSV formats for easy integration and analysis. 
- **Rotating proxy support**. Avoid CAPTCHAs, IP bans, and rate limits by routing requests through residential proxies. 
- **Geo-localized results**. Choose from 195+ locations worldwide, including countries, cities, and US states and ZIP codes, for highly localized search results. 

## Proxies 
This script works best with a proxy service. We recommend using Decodo’s residential proxies, which provide access to 115M+ IPs across 195+ locations, offering fast response times and high success rates. 
 
[Claim your free trial](https://dashboard.decodo.com/residential-proxies/pricing)

## Installation 
1.  **Clone the repository**. Run this command in your terminal to install and navigate to the project folder: 
```
git clone https://github.com/Decodo/google-images-scraper.git 
cd google-images-scraper 
```
2.  **Install Python**. Make sure you have [Python](https://www.python.org/downloads/) 3.8 or later installed. You can check by running: 
```
python3 --version 
```
3.  **Install dependencies**. This script uses only the Requests library. Install it if you haven’t already: 
```
pip install requests 
```
4.  **Insert proxy credentials**. Open the "google-images-scraper.py" file and replace the _authorization_ value in the _headers_ dictionary with your base64-encoded username:password token for Decodo. 
 
5.  **Customize your search query**. Modify the _payload_ dictionary to set your query, location, language, number of images, and other parameters. 
 
6.  **Run the script**. Execute the script in your terminal using this command: 
```
python3 google-images-scraper.py 
```
## Sample output 
Example output when running the script directly in the terminal:

![google-images-terminal-response](https://github.com/user-attachments/assets/ace8dee6-2313-4526-8f38-971cf579bb17)

And here’s an example output when using the scraper through our dashboard interface:

<img width="1187" alt="google-images-playground-response" src="https://github.com/user-attachments/assets/1e7e3622-3c51-4cbc-bed2-e540c9ced995" />

## Read more 
Find a detailed tutorial on how this script for scraping Google Images works on Decodo’s [blog](https://decodo.com/blog/how-to-scrape-google-images). 

## Related repositories 
[Google Maps scraper](https://github.com/Decodo/google-maps-scraper)

[Google News scraper](https://github.com/Decodo/Google-News-scraper)

[Python scraper tutorial](https://github.com/Decodo/Python-scraper-tutorial)
