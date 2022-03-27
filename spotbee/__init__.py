import asyncio

from spotbee.spotify import SpotifyHandler

from .ytsearch import YoutubeSearch


class SpotBee:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.spotify_handler = SpotifyHandler(client_id, client_secret)

    async def _get_urls(self, song: str) -> str:
        results = await YoutubeSearch.search(song, max_results=1)
        base_url = "https://www.youtube.com/"

        complete_url = base_url + results[0]["url_suffix"]

        return complete_url

    async def get_youtube_urls(self, spotify_link: str) -> tuple:
        tracks = await self.spotify_handler.handle_spotify_url(spotify_link)
        tasks = [self._get_urls(track) for track in tracks]
        urls = await asyncio.gather(*tasks)

        return urls

    async def get_track_titles(self, spotify_link: str) -> list:
        tracks = await self.spotify_handler.handle_spotify_url(spotify_link)

        return tracks
