from tkinter import *
from bs4 import BeautifulSoup
from PIL import ImageTk,Image
import requests
import webbrowser
from tkinter import messagebox
from pprint import pprint
import urllib.request
import wget


video_links = []
titles = []
pictures = []
episodes = []
translate = []
download_links = []
pprint(download_links)
def download_data():

    data = requests.get("https://www3.gogoanime.io/")

    soup = BeautifulSoup(data.text, "lxml")

    #video_link, title, pictures scrape
    for infos in soup.select("div.img"):
        link = infos.a.get("href")
        title = infos.a.get("title")
        picture = infos.a.find("img")
        video_links.append(link)
        titles.append(title)
        pictures.append(picture["src"])

    #episode scrape
    for episode_nr in soup.select("p.episode"):
        episode = episode_nr.text
        episodes.append(episode)

    #translation scrape
    for translation in soup.select("div.type"):
        translater = translation.text
        translate.append(translater)

    #download_links for animes still needs to be reworked can´t get the dl link
    for i in video_links:
        anime_download = requests.get("https://www3.gogoanime.io" + i)
        soup = BeautifulSoup(anime_download.text, "lxml")
        for download_link in soup.find_all("div", {"class": "download-anime"}):
            links = download_link.a.get("href")
            download_links.append(links)

def download_pictures(width, height):
    for x in range(0, len(pictures), 1):
        picture_request = requests.get(pictures[x])
        with open(str(x) + ".png", "wb") as f:
            f.write(picture_request.content)
            img = Image.open(str(x) + ".png").resize((width, height))
            img.save(str(x) + ".png")




download_data()
download_pictures(200, 200)



