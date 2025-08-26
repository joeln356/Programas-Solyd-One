#Directory Brute Force

import aiohttp
import asyncio
import colorama

from functools import lru_cache

URL = "http://shop.bancocn.com"


@lru_cache 
def get_wordlist(): # leva 0,02 em média
    with open("wordlist.txt", 'r') as f:
        wordlist = [line.strip() for line in f.readlines()]
    return wordlist


async def get_response(session, word):
    final_url = f"{URL}/{word}"

    try:
        async with session.get(final_url) as response:
            print(
                (colorama.Fore.RED if response.status > 400 else colorama.Fore.GREEN)
                + f"{final_url} -> {response.status}"
            )
            
    except Exception as error:
        print(f"URL: {final_url} -> error: {type(error).__name__}")


async def main():
    # timeout absurdo de 1h, só para n bugar, ksks
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60 * 60)) as session:
        tasks = [get_response(session, word) for word in get_wordlist()]
        await asyncio.gather(*tasks)


asyncio.run(main())
