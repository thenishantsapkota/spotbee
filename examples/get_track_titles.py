import asyncio

import spotbeeV2 as spotbee

instance = spotbee.SpotBee("spotify_client_id", "spotify_client_secret")


async def track_titles():
    tracks = await instance.get_track_titles("spotify_url")
    # Get Spotify Client ID, Spotify Client Secret from https://developer.spotify.com
    print(tracks)


asyncio.run(track_titles())
