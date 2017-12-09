#!/usr/bin/env python
#for landmass
import sys

# input comes from STDIN (standard input)

def main():
    for line in sys.stdin:
        line = line.strip()
        # split the line into words
        words = line.split(",")
        
	current_country = words[0]			#name
	current_feature1 = words[7]			#bars
	current_feature2 = words[8]			#stripes
	current_feature3 = words[9]			#colors
	current_feature4 = words[10]		#red
	current_feature5 = words[18]		#circles
	current_feature6 = words[19]		#crosses
	current_feature7 = words[20]		#saltires
	current_feature8 = words[21]		#quarters
	current_feature9 = words[23]		#crescent
	current_feature10 = words[24]		#triangles
	current_feature11 = words[25]		#icon
	current_feature12 = words[26]		#animate
	current_feature13 = words[27]		#text
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (current_country, current_feature1, current_feature2, current_feature3, current_feature4, current_feature5, current_feature6, current_feature7, current_feature8, current_feature9, current_feature10, current_feature11, current_feature11, current_feature13)
main()
