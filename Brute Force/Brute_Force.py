import aiohttp
import asyncio

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
        async with session.get(final_url, timeout=120) as response:
            print(f"{final_url} -> {response.status}")
    except Exception as error:
        print(f"URL: {final_url} -> error: {type(error).__name__}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_response(session, word) for word in get_wordlist()]
        await asyncio.gather(*tasks)


asyncio.run(main())

# By Ângelote. :|.