#!/usr/bin/env python
#for landmass

import sys

# input comes from STDIN (standard input)
def main():
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split(",")
        
	country = words[0]
        feature = words[4]
        print '%s\t%s' % (country, feature)

main()
