#!/usr/bin/env python

from operator import itemgetter
import sys
import random
import bisect
import collections  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

features = []
countries = []

def MAIN():
	# input comes from STDIN
		for line in sys.stdin:
			# remove leading and trailing whitespace
			line = line.strip()
			words = line.split("\t")
			# parse the input we got from mapper.py
			current_country = words[0]
			current_feature = words[1]
			#print '%s,%s' % (current_country, current_feature)
			features.append(int(current_feature))
			countries.append(current_country)

MAIN()
