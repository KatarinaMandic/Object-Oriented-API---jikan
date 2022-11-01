from multiprocessing import current_process
from urllib import response
import arrow
import requests
import ujson

class Anime:

    #instance methods


    #static methods
    @staticmethod
    def daily_shows():
        current = arrow.now()
        today = current.format('dddd').lower()
        r = requests.get(f'https://api.jikan.moe/v4/schedules/{today}')
        response = ujson.loads(r.text)
        print(response)
