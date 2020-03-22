from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import json, requests, urllib.request, tkinter as tk


def CreateWidgets():
    urlLabel = Label(root, text=" YOUR INSTAGRAM ID :", background="white")
    urlLabel.grid(row=0, column=0, padx=5, pady=5)

    root.urlEntry = Entry(root, width=30, textvariable=insta_id)
    root.urlEntry.grid(row=0, column=1, columnspan=2, pady=5)

    dwldBTN = Button(root, text="DOWNLOAD DP", command=i_Downloader, highlightbackground="black")
    dwldBTN.grid(row=0, column=3, padx=5, pady=5)

    root.resultLabel = Label(root, textvariable=dwldtxt, background="white")
    root.resultLabel.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
    root.resultLabel.config(font=("Courier", 25))

    root.previewLabel = Label(root, text="DP PREVIEW :", background="white")
    root.previewLabel.grid(row=3, column=0, padx=5, pady=5)

    root.dpLabel = Label(root, background="white")
    root.dpLabel.grid(row=4, column=1, columnspan=2, padx=1, pady=1)


def i_Downloader():
    download_path = "E:/IgDpdownloader/"
    insta_username = insta_id.get()
    insta_url = "https://www.instagram.com/" + insta_username
    insta_response = requests.get(insta_url)
    soup = BeautifulSoup(insta_response.text, 'html.parser')
    script = soup.find('script', text=re.compile('window._sharedData'))
    page_json = script.text.split('=', 1)[1].rstrip(';')
    data = json.loads(page_json)
    dp_url = data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    dp_name = download_path + insta_username + '.jpg'
    urllib.request.urlretrieve(dp_url, dp_name)
    dp_name = Image.open(dp_name)
    dp_name = dp_name.resize((200, 200), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(dp_name)
    root.dpLabel.config(image=image)
    root.dpLabel.photo = image
    dwldtxt.set("DP DOWNLOADED SUCCESSFULLY")


root = tk.Tk()

root.geometry("700x350")
root.title("IG-DP DOWNLOADER")
root.config(background="white")

insta_id = StringVar()
dwldtxt= StringVar()

CreateWidgets()

root.mainloop()