import asyncio
from time import time

from requests.api import get

from extract_songs import get_tracks_from_playlist
from extract_youtube_urls import URLFinder


async def get_songs():
    tracks = await get_tracks_from_playlist(
        str(input("Enter a Spotify Playlist URL: "))
    )
    tasks = [URLFinder(track) for track in tracks]
    urls = await asyncio.gather(*tasks)

    print(urls)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_songs())
