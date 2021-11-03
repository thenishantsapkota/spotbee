import asyncio

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .ytsearch import YoutubeSearch


async def get_tracks_from_playlist(
    spotify_client_id: str,
    spotify_client_secret: str,
    playlist_url: str,
) -> list:
    credentials = SpotifyClientCredentials(spotify_client_id, spotify_client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=credentials)

    results = spotify.playlist_tracks(
        playlist_id=playlist_url, additional_types=("track",)
    )
    trackList = []

    for i in results["items"]:

        if i["track"]["artists"].__len__() == 1:
            trackList.append(
                i["track"]["name"] + " - " + i["track"]["artists"][0]["name"]
            )
        else:
            nameString = ""
            for index, b in enumerate(i["track"]["artists"]):
                nameString += b["name"]
                if i["track"]["artists"].__len__() - 1 != index:
                    nameString += ", "
            trackList.append(i["track"]["name"] + " - " + nameString)

    return trackList


async def get_url(song: str) -> str:
    results = await YoutubeSearch.search(song, max_results=1)

    baseurl = "https://www.youtube.com/"

    complete_url = baseurl + results[0]["url_suffix"]

    return complete_url


async def get_songs(
    spotify_client_id: str, spotify_client_secret: str, spotify_playlist_link: str
) -> tuple:
    tracks = await get_tracks_from_playlist(
        spotify_client_id, spotify_client_secret, spotify_playlist_link
    )
    tasks = [get_url(track) for track in tracks]
    urls = await asyncio.gather(*tasks)

    return urls
