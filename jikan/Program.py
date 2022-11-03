from secrets import choice
from unittest import result
from jikan.Anime import Anime
import sys

class Program:


    @staticmethod
    def main_menu():
        menu =  '[1] Show daily anime\n' + \
            '[2] Search anime for phrase\n' + \
            '[Q] Exit application'
        print(menu)

    @staticmethod
    def user_choice():
        return input('Your choice: ')

    @staticmethod
    def exit():
        print('Application will now close...')
        sys.exit(0)

    @staticmethod
    def show_daily_anime():
        daily_amime = Anime.daily_shows()
        daily_list = daily_amime.values()
        for item in daily_list:
            print(item.short_info())
        print('-----------')
        print('Enter ID for details or "N" for menu.')
        choice = Program.user_choice()
        if not choice == 'N':
            choice = int(choice)
            print(daily_amime[choice].long_info())

    @staticmethod
    def search_anime_for_phrase():
        phrase = input('Enter search phrase: ')
        results = Anime.search_anime_by_phrase(phrase)
        results = results.values()
        for anime in results:
            print(anime.short_info())