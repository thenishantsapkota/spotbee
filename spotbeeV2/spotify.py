import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyHandler:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.credentials = SpotifyClientCredentials(
            client_id,
            client_secret,
        )
        self.spotify = spotipy.Spotify(client_credentials_manager=self.credentials)

    async def get_tracks_from_playlist(self, playlist_url: str) -> list:
        results = self.spotify.playlist_tracks(playlist_url, additional_types=["track"])

        tracklist = []
        for item in results["items"]:
            tracklist.append(
                item["track"]["name"] + " - " + item["track"]["artists"][0]["name"]
            )

        return tracklist

    async def get_tracks_from_album(self, playlist_url: str) -> list:
        results = self.spotify.album_tracks(playlist_url)
        tracklist = []
        for item in results["items"]:
            tracklist.append(item["name"] + " - " + item["artists"][0]["name"])

        return list(set(tracklist))

    async def get_track_from_url(self, track_url: str) -> list:
        result = self.spotify.track(track_url)
        return ["{} - {}".format(result["name"], result["artists"][0]["name"])]

    async def handle_spotify_url(self, url: str) -> list | None:
        if url.__contains__("playlist"):
            return await self.get_tracks_from_playlist(url)
        elif url.__contains__("album"):
            return await self.get_tracks_from_album(url)
        elif url.__contains__("track"):
            return await self.get_track_from_url(url)
        else:
            return None
