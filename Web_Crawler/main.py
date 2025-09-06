import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

target = ['http://44.222.68.207/']  
visited = set()                   
founded = set()

def found_links(url):
    try:
        print(f"Visitando: {url}")
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()


        # Avoid processing non-HTML responses

        if 'text/html' not in response.headers.get('Content-Type', ''):
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for tag in soup.find_all('a'):
            href = tag.get('href')
            if href:
                
                if href.startswith(('http://', 'https://')):  
                    full_url = href
                else:
                    full_url = urljoin(url, href)
                
                # Limpa a URL
                full_url = full_url.split('#')[0]
                
                founded.add(full_url)
                
                if (full_url not in visited and 
                    full_url not in target and 
                    full_url.startswith(('http://', 'https://'))):
                    target.append(full_url)
        
        time.sleep(0.1)
                    
    except Exception as e:
        print(f"Erro em {url}: {e}")

max_links = 1000
while target and len(visited) < max_links:
    link = target.pop(0)
    if link not in visited:
        found_links(link)
        visited.add(link)

print(f"\n{len(founded)} links encontrados:")
for link in sorted(founded):
    print(link)