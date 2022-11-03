import PySimpleGUI as sg
from jikan.Anime import Anime

sg.theme('DarkBlue14')

layout = [
    [sg.Button('Daily Anime'), 
    sg.Button('Search Anime for Phrase'),
    sg.Button('Search Anime for Season')],
    [sg.Listbox(values = [], size = (100,10), key = '_RESULTS_')],
    [sg.Button('Show Details')]
]

window = sg.Window('Jukan GUI API', 
                    layout = layout,
                    font = ('Arial', 16))


while True:
    event, values = window.read()

    if event == None:
        break
    if event == 'Daily Anime':
        daily_anime = Anime.daily_shows()
        daily_anime = daily_anime.values()
        window['_RESULTS_'].Update(values=daily_anime)


window.close()