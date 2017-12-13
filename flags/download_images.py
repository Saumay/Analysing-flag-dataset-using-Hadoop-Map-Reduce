import os
import sys

flags_list = ""
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	words = line.split(",")
	# parse the input we got from mapper.py
	current_country = words[0].strip().lower()
	current_country_flag = "'" + current_country + " flag" + "'"
	#print(current_country)
	#print(flags_list)

	os.system("python /media/saumay/W\ Files2/PADHAI/WINTER\ SEM\ 3/Subjects/E2-Data\ Mining/Project/google-images-download/google_images_download/google_images_download.py --keywords " +current_country_flag+" --limit 1")
