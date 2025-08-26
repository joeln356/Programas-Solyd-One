import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://shop.bancocn.com"

with open("wordlist.txt", 'r') as f:
    wordlist = f.readlines()

def testar(palavra):
    palavra = palavra.strip()  # remove \n
    url_final = f"{url}/{palavra}"
    try:
        r = requests.get(url_final)
        if r.status_code == 200:
            print(f"{url_final} -> {r.status_code}")
    except requests.exceptions.RequestException:
        pass

# aqui passamos a lista wordlist (não url_final sozinho)
with ThreadPoolExecutor(max_workers=25) as executor:
    executor.map(testar, wordlist)
