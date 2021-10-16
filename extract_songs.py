import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


load_dotenv()


async def get_tracks_from_playlist(playlist_url):
    credentials = SpotifyClientCredentials(
        os.environ.get("SPOTIFY_CLIENT_ID"), os.environ.get("SPOTIFY_CLIENT_SECRET")
    )
    spotify = spotipy.Spotify(client_credentials_manager=credentials)

    results = spotify.user_playlist_tracks(user="", playlist_id=playlist_url)
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
