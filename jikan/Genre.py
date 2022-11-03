import arrow
import requests
import ujson

class Genre:
    def __init__(self, mal_id, name, **kwargs) -> None:
        self.mal_id = mal_id
        self.name = name

    def __str__(self) -> str:
        return f'[{self.mal_id}] {self.name}'

    
    #static methods
    @staticmethod
    def get_genre_id():
        r = requests.get(f'https://api.jikan.moe/v4/genres/anime')
        response = ujson.loads(r.text)
        response = response['data']
        results = {}

        for record in response:
            results[record['mal_id']] = Genre(record['mal_id'], record['name'])
        return results