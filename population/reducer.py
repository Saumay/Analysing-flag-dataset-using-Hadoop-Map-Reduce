#!/usr/bin/env python

from operator import itemgetter
import sys
import random
import bisect
import collections  
import numpy as np
import matplotlib.pyplot as plt

features = []
countries = []

def cdf(weights):
	total = sum(weights)
	result = []
	cumsum = 0
	for w in weights:
		cumsum += w
		result.append(cumsum / total)
	#print(cumsum,total)
	return result

def choice(population, weights):
	assert len(population) == len(weights)
	cdf_vals = cdf(weights)
	x = random.random()
	idx = bisect.bisect(cdf_vals, x)
	#print(population[idx])
	return population[idx]

def weighted_sampling(weights, population):
	#weights=[0.1, 0.8, 0.1]
	#population = 'ABC'
	counts = collections.defaultdict(int)
	#print(choice(population, weights))
	return choice(population, weights)
	#print(counts)
	"""testing
	for i in range(100):
		print(choice(population, weights))
		counts[choice(population, weights)] += 1
	"""

def MAIN():
	# input comes from STDIN
		for line in sys.stdin:
			# remove leading and trailing whitespace
			line = line.strip()
			words = line.split("\t")
			# parse the input we got from mapper.py
			current_country = words[0]
			current_feature = words[1]
			print '%s,%s' % (current_country, current_feature)
			features.append(int(current_feature))
			countries.append(current_country)

MAIN()
