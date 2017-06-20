from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import os
from pytube import YouTube
url='https://www.youtube.com/results?search_query='

songname=input('Enter the name of the song')
temp=songname.replace(" ","+")
temp
page=urllib.request.urlopen(url+temp).read()

soup=BeautifulSoup(page,'html.parser')

list1=[soup.find_all('a',class_="yt-uix-tile-link")]
y=[]
for list in list1:
	for x in list:
		#print(x.get('href'))
		y.append(x)

#print("all done")
#print(y[0].get('href'))

webbrowser.open("https://m.youtube.com/"+y[0].get('href'))
url_link="https://m.youtube.com/"+y[0].get('href')


url_open=urllib.request.urlopen(url_link)
url_open=url_open.read(50000)
soup=BeautifulSoup(url_open,'html.parser')
#title=title.replace("-YouTube","")


yt=YouTube(url_link)
yt.set_filename(songname)
video=yt.get('mp4','720p')
print("downloading ..... ->"+songname)
video.download('C:/Users/lenovo/Desktop')

#os.system("youtube-dl -citk --max-quality FORMAT url_link")