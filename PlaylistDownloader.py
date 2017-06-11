
from subprocess import call     # for calling mplayer and lame
from sys import argv            # allows user to specify input and output directories
import os    
from pytube import *
from pprint import pprint                   # help with file handling
import urllib
import urllib2
from bs4 import BeautifulSoup

all_links = []




def check_file_exists(directory, filename, extension):
    path = directory + "/" + filename + extension
    return os.path.isfile(path)

def main(indir, outdir):


    try:
        # check specified folders exist
        if not os.path.exists(indir):
            exit("Error: Input directory \'" + indir + "\' does not exist. (try prepending './')")
        if not os.path.exists(outdir):
            exit("Error: Output directory \'" + outdir + "\' does not exist.")
        if not os.access(outdir, os.W_OK):
            exit("Error: Output directory \'" + outdir + "\' is not writeable.")

        print "[%s/*.mp4] --> [%s/*.mp3]" % (indir, outdir)
        files = [] # files for exporting
            
        # get a list of all convertible files in the input directory
        filelist = [ f for f in os.listdir(indir) if f.endswith(".mp4") ]
        for path in filelist:
            basename = os.path.basename(path) 
            filename = os.path.splitext(basename)[0]
            files.append(filename)
        # remove files that have already been outputted from the list
        files[:] = [f for f in files if not check_file_exists(outdir, f, ".mp3")]
    except OSError as e:
        exit(e)
    
    if len(files) == 0:
        exit("Could not find any files to convert that have not already been converted.")

    # convert all unconverted files
    for filename in files:
        print "-- converting %s.mp4 to %s.mp3 --" % (indir + "/" + filename, outdir + "/" + filename)
        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", indir + "/" + filename + ".mp4"])
        call(["lame", "-h", "-b", "192", "audiodump.wav", outdir + "/" + filename + ".mp3"])
        os.remove(filename + '.mp4')
        os.remove("audiodump.wav")

# set the default directories and try to get input directories
args = [".", "."]
for i in range(1, min(len(argv), 3)):
    args[i - 1] = argv[i]

# if only input directory is set, make the output directory the same
if len(argv) == 2:
    args[1] = args[0]





#This is what goes through the list of songs I want and donwloads them to youtube
def get_video():
    b = [0,20,40,60]
    for nums in b:
        try:
            link = str(x[nums])
            yt = YouTube(link)
            yt.filter('mp4')[-1]
            video = yt.get('mp4')
            video.download('/home/main/Desktop/Youtube/'+'{}'.format(nums))
            print'finished loop {}'.format(nums)
        except:
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
    get_link(['handmouth sedona lyrics', 'milo pizza party', 'waving flags lyrics'])
    get_video()
   # get_video()
    #main(args[0], args[1])
