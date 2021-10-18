import spotbee
import asyncio

async def get_links():
    urls = await spotbee.get_songs("spotify_client_id", "spotfiy_client_secret", "spotify_playlist_link")
    # Get Spotify Client ID, Spotify Client Secret from https://developer.spotify.com
    print(urls)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_links())