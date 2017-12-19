import os
import sys
from os import listdir
from os.path import isfile, join


flags_list = ""
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	words = line.split(",")
	# parse the input we got from mapper.py
	current_country = words[0].strip().lower()
	dir_name = "/media/saumay/W Files2/PADHAI/WINTER SEM 3/Subjects/E2-Data Mining/Project/Flags_of_all_countries/"
	dir_name += current_country + " flag/"
	onlyfiles = [f for f in listdir(dir_name) if isfile(join(dir_name, f))]#print(current_country)
	#print(flags_list)
	prev_name = dir_name + onlyfiles[0]
	new_name = dir_name + current_country + ".png"
	os.rename(prev_name, new_name)
