import asyncio

import spotbeeV2 as spotbee

instance = spotbee.SpotBee("spotify_client_id", "spotify_client_secret")


async def youtube_urls():
    urls = await instance.get_youtube_urls("spotify_url")
    # Get Spotify Client ID, Spotify Client Secret from https://developer.spotify.com
    print(urls)


asyncio.run(youtube_urls())
