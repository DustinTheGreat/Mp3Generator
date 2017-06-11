
"""
This script takes songs-titles off of a pre-made list and fetches the youtube video and converts it to .mp3 format.

Requirements:
    sudo apt-get install lame
    sudo apt-get install mplayer

Python packages:
    pip install BeautifulSoup
    pip install pytube


Dustin Roberts 6/11/17
"""

from subprocess import call     # for calling mplayer and lame
from sys import argv            # allows user to specify input and output directories
import os    
from pytube import *
from pprint import pprint                   # help with file handling
import urllib
import urllib2
from bs4 import BeautifulSoup
import convert
all_links = []




#This is what goes through the list of songs I want and donwloads them to youtube
def get_video():
    b = [0,20,40, 60,80]
    for nums in b:
        try:
            link = str(x[nums])
            yt = YouTube(link)
            try:
                print(yt.filter('mp4')[-1])
                video = yt.get('mp4', '360p')
                video.download('/home/main/Desktop/Youtube/'+'{}'.format(nums) + '.mp4')
                print'finished loop {}'.format(nums)
            except:
                try:
                    print(yt.filter('mp4')[-1])                 
                    video = yt.get('3gp', '144p')
                    video.download('/home/main/Desktop/Youtube/'+'{}'.format(nums) + '.mp4')
                    print'finished loop {}'.format(nums)
                except:
                    print'couldnt download anything'

        except:
            print'failed'
            continue
x  = list()

def get_link(song_list):
    counter = 0
    for num in range(len(song_list)):
        textToSearch = song_list[num]
        query = urllib.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            x.append('https://www.youtube.com' + vid['href'])




if __name__=='__main__':
    get_link([ 'milo pizza party', 'waving flags lyrics', 'back in black lyrics','mr jones', 'peach plumb pear jonna newsome'])
    get_video()
   # get_video()
    convert.convert('/home/main/Desktop/Youtube')