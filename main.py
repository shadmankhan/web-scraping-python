from bs4 import BeautifulSoup
import requests
import sys
import webbrowser

res = requests.get(
    'https://www.google.com/search?q=site%3Alinkedin.com%2Fin+front+end+developer+react+notice+period')
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.prettify())
print('--------------------------------')
# print(soup.title.text)

# soup = BeautifulSoup(res.text, "html.parser")
# raw_headings = soup.find_all('h3', attrs={'class': 'zBAuLc'})
# raw_urls = soup.find_all('div', attrs={'class': 'yuRUbf'})

raw_data = soup.find_all('div', attrs={'class': 'kCrYT'})

for data in raw_data:
    url = data.a
    print(url)

# print(raw_urls)

# headings = []
# for heading in raw_headings:
#     h3 = heading.find('div').text
#     headings.append(h3)

# urls = []
# for url in raw_urls:
#     href = url['href']
#     urls.append(href)

# print(urls, headings)
