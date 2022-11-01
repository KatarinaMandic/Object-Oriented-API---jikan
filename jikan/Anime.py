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

    def short_info(self):
        return f'[{self.mal_id}] {self.title} - {self.score}'


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