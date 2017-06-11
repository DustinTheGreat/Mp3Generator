import os
from subprocess import call
#this is what converts the videos to .mp4
def convert(path):
	del_all = str(raw_input('Do you want to replace the .mp4 files? (yes)-or-(no):'))

	for filename in os.listdir(path):
		if filename.endswith('.mp4'):
			print("Now---converting --.mp4 to ---.mp3 --")
	        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", path + "/" + filename ])
	        call(["lame", "-h", "-b", "192", "audiodump.wav", path + "/" + filename.replace('.mp4', '.mp3')])
		if del_all =='yes':
			if filename.endswith('.mp4'):
				os.remove(path+'/'+filename)



if __name__ == '__main__':
	convert('/home/main/Desktop/Youtube')