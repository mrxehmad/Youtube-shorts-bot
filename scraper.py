import requests
from bs4 import BeautifulSoup

# Step 1: Send HTTP request and extract video URLs
url = 'https://www.tiktok.com/tag/funnyvideo'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
video_urls = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('https://www.tiktok.com/@'):
        video_urls.append(href)

# Step 2: Save URLs to file
with open('list.txt', 'w') as f:
    for url in video_urls[:15]:
        f.write(url + '\n')
