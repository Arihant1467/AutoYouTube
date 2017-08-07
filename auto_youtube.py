import pafy
import sys
import os
print sys.argv
url=sys.argv[1]
video=pafy.new(url)
if video:	
	print "Title of the video-:",video.title
	best=video.getbest()
	print "Details of the best video available for the URL\n"
	print "Resolution-",best.resolution," Extension-",best.extension," Size in KBs-",best.get_filesize()
	ans=raw_input("Want to download the video(Y/N)-\t")
	if(ans=="Y" or ans=="y"):
		filepath="./You Tube Download";
		if not os.path.exists(filepath):
			os.makedirs(filepath)
		file=best.download(quiet=False,filepath=filepath+"/"+video.title+"."+best.extension)
		print "Download complete"
	else:
		print "The position does not exists"	
else:
	print "not a youtube video"	