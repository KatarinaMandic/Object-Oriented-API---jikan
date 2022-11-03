from multiprocessing import current_process
import stat
from urllib import response
import arrow
import requests
import ujson

class Anime:

    #instance methods
    def __init__(self, mal_id, title, score, **kwargs) -> None:
        self.mal_id = mal_id
        self.title = title
        self.score = score
        self.url = ''
        self.title_japanese = ''
        self.status = ''
        self.episodes = 0
        self.synopsis = ''
        self.airing = ''
        self.image_url = ''

    def short_info(self):
        return f'[{self.mal_id}] {self.title} - {self.score}'


    def details(self):
        r = requests.get(f'https://api.jikan.moe/v4/anime/{self.mal_id}')
        response = ujson.loads(r.text)
        response = response['data']
        self.url = response['url']
        self.title_japanese = response['title_japanese']
        self.status = response['status']
        self.episodes = response['episodes']
        self.synopsis = response['synopsis']
        self.airing = response['aired']['string']
        self.image_url = response['images']['jpg']['image_url']

    def long_info(self):
        self.details()
        return f'{self.title}\n' + \
        f'{self.title_japanese}\n' + \
            f'Score: {self.score}\n' + \
                f'URL: {self.url}\n' + \
                    f'Episodes: {self.episodes}\n' + \
                        f'Airing: {self.airing}\n' + \
                            f'Synopsis: {self.synopsis}'

    def __str__(self) -> str:
        return f'[{self.mal_id}] {self.title} - {self.score}'
    
    #static methods

    @staticmethod
    def get_request_results(req_string):
        r = requests.get(req_string)
        response = ujson.loads(r.text)
        response = response['data']
        results = {}

        for record in response:
            results[record['mal_id']] = Anime(record['mal_id'], record['title'], record['score'])
        return results


    @staticmethod
    def daily_shows():
        current = arrow.now()
        today = current.format('dddd').lower()
        return Anime.get_request_results(f'https://api.jikan.moe/v4/schedules/{today}')

    @staticmethod
    def search_anime_by_phrase(phrase):
        return Anime.get_request_results(f'https://api.jikan.moe/v4/anime?q={phrase}')

    @staticmethod
    def get_anime_for_season(season, year):
        return Anime.get_request_results(f'https://api.jikan.moe/v4/seasons/{year}/{season}')
