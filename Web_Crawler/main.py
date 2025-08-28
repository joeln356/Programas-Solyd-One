import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

founded_links = []
visited = set()

target = "http://advanced.bancocn.com"

def parsing(link):
    if link in visited:
        return
    visited.add(link)

    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all('a'):
            href = tag.get('href')
            if href:
                full_link = urljoin(link, href)

                if "advanced.bancocn.com" in full_link:
                    founded_links.append(full_link)
    except Exception as e:
        print(f'Error accesing {link}: {e}')

parsing(target)

for link in founded_links:
        parsing(link)

print('=======Founded links=======')
for l in visited:
     print(l)

