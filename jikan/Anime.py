from multiprocessing import current_process
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

    def long_info(self):
        self.details()
        return f'{self.title}\n' + \
        f'{self.title_japanese}\n' + \
            f'Score: {self.score}\n' + \
                f'URL: {self.url}\n' + \
                    f'Episodes: {self.episodes}\n' + \
                        f'Airing: {self.airing}\n' + \
                            f'Synopsis: {self.synopsis}'

    #static methods
    @staticmethod
    def daily_shows():
        current = arrow.now()
        today = current.format('dddd').lower()
        r = requests.get(f'https://api.jikan.moe/v4/schedules/{today}')
        response = ujson.loads(r.text)
        response = response['data']
        daily_anime = {}

        for record in response:
            daily_anime[record['mal_id']] = Anime(record['mal_id'], record['title'], record['score'])
        return daily_anime

    @staticmethod
    def search_anime_by_phrase(phrase):
        r = requests.get(f'https://api.jikan.moe/v4/anime?q={phrase}')
        response = ujson.loads(r.text)
        response = response['data']
        daily_anime = {}

        for record in response:
            daily_anime[record['mal_id']] = Anime(record['mal_id'], record['title'], record['score'])
        return daily_anime
        