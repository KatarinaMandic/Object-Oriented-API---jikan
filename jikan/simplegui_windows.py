from urllib import response
import PySimpleGUI as sg
from jikan.Anime import Anime
from PIL import Image
import requests
import os

def create_image(image_url):
    r = requests.get(image_url)
    path_jpg = os.getcwd() + r'\tmp.jpg'
    path_png = os.getcwd() + r'\tmp.png'
    file = open(path_jpg, 'wb')
    file.write(r.content)
    file.close()
    im = Image.open(path_jpg)
    im.save(path_png)
    return sg.Image(path_png)

def details_window(anime:Anime) -> sg.Window:
    anime.details()
    image = create_image(anime.image_url)
    layout = [
        [sg.Text(anime.title, font=('Arial', 24))],
        [create_image(anime.image_url)],
        [sg.Multiline(anime.synopsis, 
        disabled=True,
        size = (90, 10))]

    ]
    return sg.Window(anime.title, layout=layout, 
    finalize=True)