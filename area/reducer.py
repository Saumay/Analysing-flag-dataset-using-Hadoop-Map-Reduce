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
def compute_centeroids(k):
	weights = []
	c1 = random_sampling(features)
	centeroids.append(c1)
	index1 = features.index(c1)
	country1 = countries[index1]
	print 'c1=%d,country=%s' % (c1,country1)
	centeroids_countries.append(country1)
	for i in range(0,k-1):
		for j in range(0,len(features)):
			small = max(features)
			for l in range(0,len(centeroids)):
				di = pow((int(features[j]) - centeroids[l]),2)
				#print 'di=%d'%(di)
				if(di<small):
					small = di
			di_final = small
			#print 'di_final=%d'%(di_final)
			#print()
			weights.append(pow(di_final,2))
		sum_weights = sum(weights)
		weights = [float(x)/sum_weights for x in weights]
		#print("Weights",weights)
		cn = weighted_sampling(weights, features)
		centeroids.append(cn)  

		indexn = features.index(cn)
		countryn = countries[indexn]
		centeroids_countries.append(countryn)  

		weights=[]   
		#print '%d:%s' % (cn,countryn)  
	print("\n")     

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
