from tkinter import *
from bs4 import BeautifulSoup
from PIL import ImageTk,Image
import requests
import webbrowser
from tkinter import messagebox



video_links = []
titles = []
pictures = []
episodes = []
translate = []
download_links = []

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

    #download_links for animes
    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[0])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)
        print(download_links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[1])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[2])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[3])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[4])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[5])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[6])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[7])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[8])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[9])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[10])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[11])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[12])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[13])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[14])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[15])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[16])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[17])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[18])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

    anime_download_1 = requests.get("https://www3.gogoanime.io" + video_links[19])
    soup = BeautifulSoup(anime_download_1.text, "lxml")
    for download_link in soup.find_all("div", {"class": "download-anime"}):
        links = download_link.a.get("href")
        download_links.append(links)

download_data()


class AnimeApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Anime GoGo Recent Releases Webscraper")
        self.anime_select = ""
        self.anime_watch = ""
        self.width = 200
        self.height = 300
        self.download_pictures()
        self.images()
        self.window_canvas()
        self.labels()
        self.frames()
        self.info_canvas()
        self.scrollbar()
        self.edit()
        self.buttons()
        self.information_canvas.tag_bind('anime1', '<Button-1>', self.anime_1)
        self.information_canvas.tag_bind('anime2', '<Button-1>', self.anime_2)
        self.information_canvas.tag_bind('anime3', '<Button-1>', self.anime_3)
        self.information_canvas.tag_bind('anime4', '<Button-1>', self.anime_4)
        self.information_canvas.tag_bind('anime5', '<Button-1>', self.anime_5)
        self.information_canvas.tag_bind('anime6', '<Button-1>', self.anime_6)
        self.information_canvas.tag_bind('anime7', '<Button-1>', self.anime_7)
        self.information_canvas.tag_bind('anime8', '<Button-1>', self.anime_8)
        self.information_canvas.tag_bind('anime9', '<Button-1>', self.anime_9)
        self.information_canvas.tag_bind('anime10', '<Button-1>', self.anime_10)
        self.information_canvas.tag_bind('anime11', '<Button-1>', self.anime_11)
        self.information_canvas.tag_bind('anime12', '<Button-1>', self.anime_12)
        self.information_canvas.tag_bind('anime13', '<Button-1>', self.anime_13)
        self.information_canvas.tag_bind('anime14', '<Button-1>', self.anime_14)
        self.information_canvas.tag_bind('anime15', '<Button-1>', self.anime_15)
        self.information_canvas.tag_bind('anime16', '<Button-1>', self.anime_16)
        self.information_canvas.tag_bind('anime17', '<Button-1>', self.anime_17)
        self.information_canvas.tag_bind('anime18', '<Button-1>', self.anime_18)
        self.information_canvas.tag_bind('anime19', '<Button-1>', self.anime_19)
        self.information_canvas.tag_bind('anime20', '<Button-1>', self.anime_20)
        self.root.mainloop()

    def anime_1(self, evt):
        messagebox.showinfo("Anime Information", titles[0] + "\n" + episodes[0] + "\n" + translate[0])
        self.anime_select = download_links[0]
        self.anime_watch = "gogoanimes.co" + video_links[0]

    def anime_2(self, evt):
        messagebox.showinfo("Anime Information", titles[1] + "\n" + episodes[1] + "\n" + translate[1])
        self.anime_select = download_links[1]
        self.anime_watch = "gogoanimes.co" + video_links[1]

    def anime_3(self, evt):
        messagebox.showinfo("Anime Information", titles[2] + "\n" + episodes[2] + "\n" + translate[2])
        self.anime_select = download_links[2]
        self.anime_watch = "gogoanimes.co" + video_links[2]

    def anime_4(self, evt):
        messagebox.showinfo("Anime Information", titles[3] + "\n" + episodes[3] + "\n" + translate[3])
        self.anime_select = download_links[3]
        self.anime_watch = "gogoanimes.co" + video_links[3]

    def anime_5(self, evt):
        messagebox.showinfo("Anime Information", titles[4] + "\n" + episodes[4] + "\n" + translate[4])
        self.anime_select = download_links[4]
        self.anime_watch = "gogoanimes.co" + video_links[4]

    def anime_6(self, evt):
        messagebox.showinfo("Anime Information", titles[5] + "\n" + episodes[5] + "\n" + translate[5])
        self.anime_select = download_links[5]
        self.anime_watch = "gogoanimes.co" + video_links[5]

    def anime_7(self, evt):
        messagebox.showinfo("Anime Information", titles[6] + "\n" + episodes[6] + "\n" + translate[6])
        self.anime_select = download_links[6]
        self.anime_watch = "gogoanimes.co" + video_links[6]

    def anime_8(self, evt):
        messagebox.showinfo("Anime Information", titles[7] + "\n" + episodes[7] + "\n" + translate[7])
        self.anime_select = download_links[7]
        self.anime_watch = "gogoanimes.co" + video_links[7]

    def anime_9(self, evt):
        messagebox.showinfo("Anime Information", titles[8] + "\n" + episodes[8] + "\n" + translate[8])
        self.anime_select = download_links[8]
        self.anime_watch = "gogoanimes.co" + video_links[8]

    def anime_10(self, evt):
        messagebox.showinfo("Anime Information", titles[9] + "\n" + episodes[9] + "\n" + translate[9])
        self.anime_select = download_links[9]
        self.anime_watch = "gogoanimes.co" + video_links[9]

    def anime_11(self, evt):
        messagebox.showinfo("Anime Information", titles[10] + "\n" + episodes[10] + "\n" + translate[10])
        self.anime_select = download_links[10]
        self.anime_watch = "gogoanimes.co" + video_links[10]

    def anime_12(self, evt):
        messagebox.showinfo("Anime Information", titles[11] + "\n" + episodes[11] + "\n" + translate[11])
        self.anime_select = download_links[11]
        self.anime_watch = "gogoanimes.co" + video_links[11]

    def anime_13(self, evt):
        messagebox.showinfo("Anime Information", titles[12] + "\n" + episodes[12] + "\n" + translate[12])
        self.anime_select = download_links[12]
        self.anime_watch = "gogoanimes.co" + video_links[12]

    def anime_14(self, evt):
        messagebox.showinfo("Anime Information", titles[13] + "\n" + episodes[13] + "\n" + translate[13])
        self.anime_select = download_links[13]
        self.anime_watch = "gogoanimes.co" + video_links[13]

    def anime_15(self, evt):
        messagebox.showinfo("Anime Information", titles[14] + "\n" + episodes[14] + "\n" + translate[14])
        self.anime_select = download_links[14]
        self.anime_watch = "gogoanimes.co" + video_links[14]

    def anime_16(self, evt):
        messagebox.showinfo("Anime Information", titles[15] + "\n" + episodes[15] + "\n" + translate[15])
        self.anime_select = download_links[15]
        self.anime_watch = "gogoanimes.co" + video_links[15]

    def anime_17(self, evt):
        messagebox.showinfo("Anime Information", titles[16] + "\n" + episodes[16] + "\n" + translate[16])
        self.anime_select = download_links[16]
        self.anime_watch = "gogoanimes.co" + video_links[16]

    def anime_18(self, evt):
        messagebox.showinfo("Anime Information", titles[17] + "\n" + episodes[17] + "\n" + translate[17])
        self.anime_select = download_links[17]
        self.anime_watch = "gogoanimes.co" + video_links[17]

    def anime_19(self, evt):
        messagebox.showinfo("Anime Information", titles[18] + "\n" + episodes[18] + "\n" + translate[18])
        self.anime_select = download_links[18]
        self.anime_watch = "gogoanimes.co" + video_links[18]

    def anime_20(self, evt):
        messagebox.showinfo("Anime Information", titles[19] + "\n" + episodes[19] + "\n" + translate[19])
        self.anime_select = download_links[19]
        self.anime_watch = "gogoanimes.co" + video_links[19]

    def download_anime_episode(self):
        webbrowser.open_new_tab('%s' % self.anime_select)

    def open_website(self):
        webbrowser.open_new_tab("gogoanimes.co")

    def watch_anime_online(self):
        webbrowser.open_new_tab(self.anime_watch)

    def download_pictures(self):
        self.request1 = requests.get(pictures[0])
        with open("anime_1.png", "wb") as f:
            f.write(self.request1.content)

        self.request2 = requests.get(pictures[1])
        with open("anime_2.png", "wb") as f:
            f.write(self.request2.content)

        self.request3 = requests.get(pictures[2])
        with open("anime_3.png", "wb") as f:
            f.write(self.request3.content)

        self.request4 = requests.get(pictures[3])
        with open("anime_4.png", "wb") as f:
            f.write(self.request4.content)

        self.request5 = requests.get(pictures[4])
        with open("anime_5.png", "wb") as f:
            f.write(self.request5.content)

        self.request6 = requests.get(pictures[5])
        with open("anime_6.png", "wb") as f:
            f.write(self.request6.content)

        self.request7 = requests.get(pictures[6])
        with open("anime_7.png", "wb") as f:
            f.write(self.request7.content)

        self.request8 = requests.get(pictures[7])
        with open("anime_8.png", "wb") as f:
            f.write(self.request8.content)

        self.request9 = requests.get(pictures[8])
        with open("anime_9.png", "wb") as f:
            f.write(self.request9.content)

        self.request10 = requests.get(pictures[9])
        with open("anime_10.png", "wb") as f:
            f.write(self.request10.content)

        self.request11 = requests.get(pictures[10])
        with open("anime_11.png", "wb") as f:
            f.write(self.request11.content)

        self.request12 = requests.get(pictures[11])
        with open("anime_12.png", "wb") as f:
            f.write(self.request12.content)

        self.request13 = requests.get(pictures[12])
        with open("anime_13.png", "wb") as f:
            f.write(self.request13.content)

        self.request14 = requests.get(pictures[13])
        with open("anime_14.png", "wb") as f:
            f.write(self.request14.content)

        self.request15 = requests.get(pictures[14])
        with open("anime_15.png", "wb") as f:
            f.write(self.request15.content)

        self.request16 = requests.get(pictures[15])
        with open("anime_16.png", "wb") as f:
            f.write(self.request16.content)

        self.request17 = requests.get(pictures[16])
        with open("anime_17.png", "wb") as f:
            f.write(self.request17.content)

        self.request18 = requests.get(pictures[17])
        with open("anime_18.png", "wb") as f:
            f.write(self.request18.content)

        self.request19 = requests.get(pictures[18])
        with open("anime_19.png", "wb") as f:
            f.write(self.request19.content)

        self.request20 = requests.get(pictures[19])
        with open("anime_20.png", "wb") as f:
            f.write(self.request20.content)

    def images(self):
        self.anime_image_1 = ImageTk.PhotoImage(Image.open("anime_1.png").resize((self.width, self.height)))
        self.anime_image_2 = ImageTk.PhotoImage(Image.open("anime_2.png").resize((self.width, self.height)))
        self.anime_image_3 = ImageTk.PhotoImage(Image.open("anime_3.png").resize((self.width, self.height)))
        self.anime_image_4 = ImageTk.PhotoImage(Image.open("anime_4.png").resize((self.width, self.height)))
        self.anime_image_5 = ImageTk.PhotoImage(Image.open("anime_5.png").resize((self.width, self.height)))
        self.anime_image_6 = ImageTk.PhotoImage(Image.open("anime_6.png").resize((self.width, self.height)))
        self.anime_image_7 = ImageTk.PhotoImage(Image.open("anime_7.png").resize((self.width, self.height)))
        self.anime_image_8 = ImageTk.PhotoImage(Image.open("anime_8.png").resize((self.width, self.height)))
        self.anime_image_9 = ImageTk.PhotoImage(Image.open("anime_9.png").resize((self.width, self.height)))
        self.anime_image_10 = ImageTk.PhotoImage(Image.open("anime_10.png").resize((self.width, self.height)))
        self.anime_image_11 = ImageTk.PhotoImage(Image.open("anime_11.png").resize((self.width, self.height)))
        self.anime_image_12 = ImageTk.PhotoImage(Image.open("anime_12.png").resize((self.width, self.height)))
        self.anime_image_13 = ImageTk.PhotoImage(Image.open("anime_13.png").resize((self.width, self.height)))
        self.anime_image_14 = ImageTk.PhotoImage(Image.open("anime_14.png").resize((self.width, self.height)))
        self.anime_image_15 = ImageTk.PhotoImage(Image.open("anime_15.png").resize((self.width, self.height)))
        self.anime_image_16 = ImageTk.PhotoImage(Image.open("anime_16.png").resize((self.width, self.height)))
        self.anime_image_17 = ImageTk.PhotoImage(Image.open("anime_17.png").resize((self.width, self.height)))
        self.anime_image_18 = ImageTk.PhotoImage(Image.open("anime_18.png").resize((self.width, self.height)))
        self.anime_image_19 = ImageTk.PhotoImage(Image.open("anime_19.png").resize((self.width, self.height)))
        self.anime_image_20 = ImageTk.PhotoImage(Image.open("anime_20.png").resize((self.width, self.height)))

    def window_canvas(self):
        self.window_size = Canvas(self.root, width=1000, height=490, bg="#91a6b3")
        self.window_size.pack()
        self.window_text = self.window_size.create_text(400, 500, text="GoGo Anime TV Recent Releases", fill="#ea1c1c", font="OpenSans 20 bold")

    def frames(self):
        self.information_frame = Frame(self.window_size, bd=5, relief="ridge")
        self.information_frame.place(rely=0.15, relheight=0.69, relwidth=0.6805, relx=0.001)

    def labels(self):
        self.header = Label(self.window_size, bg="#33a8ff", text="GoGo Anime TV Recent Releases", font="OpenSans 20 bold", fg="white")
        self.header.place(rely=0.005, relwidth=0.699, relheight=0.149, relx=0.001)
        self.option = Label(self.window_size, bg="#33a8ff", text="Options", font="OpenSans 20 bold", fg="white")
        self.option.place(rely=0.005, relwidth=0.3, relheight=0.149, relx=0.696)
        self.bottom = Label(self.window_size, bg="#33a8ff", font="OpenSans 20 bold", fg="white")
        self.bottom.place(rely=0.83, relwidth=0.995, relheight=0.165, relx=0.001)
    def info_canvas(self):
        self.information_canvas = Canvas(self.information_frame, width=1500, height=200, bg="#33a8ff", scrollregion=(0, 0, 0, 2230))
        self.information_canvas.place(relheight=1, relwidth=1)
        self.anime_1_image = self.information_canvas.create_image(120, 170, image=self.anime_image_1, tags="anime1")
        self.anime_2_image = self.information_canvas.create_image(335, 170, image=self.anime_image_2, tags="anime2")
        self.anime_3_image = self.information_canvas.create_image(550, 170, image=self.anime_image_3, tags="anime3")
        self.anime_4_image = self.information_canvas.create_image(120, 485, image=self.anime_image_4, tags="anime4")
        self.anime_5_image = self.information_canvas.create_image(335, 485, image=self.anime_image_5, tags="anime5")
        self.anime_6_image = self.information_canvas.create_image(550, 485, image=self.anime_image_6, tags="anime6")
        self.anime_7_image = self.information_canvas.create_image(120, 800, image=self.anime_image_7, tags="anime7")
        self.anime_8_image = self.information_canvas.create_image(335, 800, image=self.anime_image_8, tags="anime8")
        self.anime_9_image = self.information_canvas.create_image(550, 800, image=self.anime_image_9, tags="anime9")
        self.anime_10_image = self.information_canvas.create_image(120, 1115, image=self.anime_image_10, tags="anime10")
        self.anime_11_image = self.information_canvas.create_image(335, 1115, image=self.anime_image_11, tags="anime11")
        self.anime_12_image = self.information_canvas.create_image(550, 1115, image=self.anime_image_12, tags="anime12")
        self.anime_13_image = self.information_canvas.create_image(120, 1430, image=self.anime_image_13, tags="anime13")
        self.anime_14_image = self.information_canvas.create_image(335, 1430, image=self.anime_image_14, tags="anime14")
        self.anime_15_image = self.information_canvas.create_image(550, 1430, image=self.anime_image_15, tags="anime15")
        self.anime_16_image = self.information_canvas.create_image(120, 1745, image=self.anime_image_16, tags="anime16")
        self.anime_17_image = self.information_canvas.create_image(335, 1745, image=self.anime_image_17, tags="anime17")
        self.anime_18_image = self.information_canvas.create_image(550, 1745, image=self.anime_image_18, tags="anime18")
        self.anime_19_image = self.information_canvas.create_image(120, 2060, image=self.anime_image_19, tags="anime19")
        self.anime_20_image = self.information_canvas.create_image(335, 2060, image=self.anime_image_20, tags="anime20")

    def scrollbar(self):
        self.scrollX = Scrollbar(self.window_size, orient=VERTICAL)
        self.scrollX.place(relwidth=0.02, relheight=0.689, rely=0.15, relx=0.679)

    def edit(self):
        self.scrollX.config(command=self.information_canvas.yview)
        self.information_canvas.config(yscrollcommand = self.scrollX.set)

    def buttons(self):
        self.download_button = Button(self.window_size, text="Download Anime", font="OpenSans 15 bold", relief="flat", bd=10, bg="#33a8ff", fg="white", command=self.download_anime_episode)
        self.download_button.place(relx=0.7, rely=0.153, relwidth=0.296, relheight=0.17)
        self.visit_website = Button(self.window_size, text="Go to Website", font="OpenSans 15 bold", relief="flat", bd=10, bg="#33a8ff", fg="white", command=self.open_website)
        self.visit_website.place(relx=0.7, rely=0.32, relwidth=0.296, relheight=0.17)
        self.watch_online = Button(self.window_size, text="Watch Anime online", font="OpenSans 15 bold", relief="flat", bd=10, bg="#33a8ff", fg="white", command=self.watch_anime_online)
        self.watch_online.place(relx=0.7, rely=0.49, relwidth=0.296, relheight=0.17)
        self.info = Button(self.window_size, text="Info", font="OpenSans 15 bold", relief="flat", bd=10, bg="#33a8ff", fg="white")
        self.info.place(relx=0.7, rely=0.66, relwidth=0.296, relheight=0.17)


AnimeApp()

