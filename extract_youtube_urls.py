import asyncio
import ytsearch


async def URLFinder(song):
    results = await ytsearch.YoutubeSearch.search(song, max_results=1)

    baseurl = "https://www.youtube.com/"

    complete_url = baseurl + results[0]["url_suffix"]

    return complete_url
