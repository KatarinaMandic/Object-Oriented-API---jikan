from multiprocessing import current_process
import arrow
import requests
import ujson

class Anime:

    #instance methods


    #static methods
    @staticmethod
    def daily_shows():
        current = arrow.now()
        print(current)