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

centeroids = []
centeroids_countries = []

clusters = [[]]
clusters_countries = [[]]

sum_of_squared_error = []

labels = ["A","B","C","D","E"]

##WEIGHTED  SAMPLING
def cdf(weights):
	total = sum(weights)
	result = []
	cumsum = 0
	for w in weights:
		cumsum += w
		result.append(cumsum / total)
	#print(cumsum,total)
	return result

def sort_countries_centeroids(A,B):
	for i in range( len( A ) ):
		for k in range( len( A ) - 1, i, -1 ):
			if ( A[k] < A[k - 1] ):
				swap( A, k, k - 1 )
				swap( B, k, k - 1)
def swap( A, x, y ):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

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
	"""#

##RANDOM SAMPLING
def random_sampling(population):
	n = random.sample(features, 1)
	return n[0]

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

def k_means(k):
	clusters_prev=[[]]
	while(1):
		sum_errors = 0

		for i in range(0,len(centeroids)):
			clusters.append([centeroids[i]])
			clusters_countries.append([centeroids_countries[i]])
		#print(clusters)
		#print(clusters_countries)

		if(len(clusters)==k+1):
			clusters.pop(0)
			clusters_countries.pop(0)

		#print(len(clusters))
		#print(clusters_countries)

		count = 0		

		for i in range(len(features)):
			dist_list = []
			for j in range(len(centeroids)):
				##############################################
				dist = abs(features[i]-centeroids[j])
				##############################################
				dist_list.append(dist)

			min_dist_index = dist_list.index(min(dist_list))
			clusters[min_dist_index].append(features[i])
			clusters_countries[min_dist_index].append(countries[i])

			sum_errors += min(dist_list)

			centeroids[min_dist_index] = sum(clusters[min_dist_index])/len(clusters[min_dist_index])
			#print(dist_list)
		#print(clusters)
		#print()
		#print(clusters_countries)
		#print()

		if(clusters==clusters_prev):
			#print(count)
			break
		clusters_prev = clusters

		for i in range(k):
			clusters.pop()
			clusters_countries.pop()

		count += 1

	sum_of_squared_error.append(sum_errors)

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
	

		#print '%d' % (features_sum)  
		k=5

		compute_centeroids(k)
		#print(centeroids)
		#print(centeroids_countries)

		sort_countries_centeroids(centeroids, centeroids_countries)

		print "Centeroids:",centeroids
		print "Countries corresponding to centeroids:",centeroids_countries

		########################################################
		plt.plot(features, np.zeros_like(features), '.')
		plt.show()
		########################################################

		k_means(k)
		count = 0
		print("\n")
		for i in range(k):
			print "%s:" % (labels[i%5])
			plt.plot(clusters[i], np.zeros_like(clusters[i]), '.')
			#draw_graph(clusters[i])
			for j in range(1, len(clusters[i])):
				print '%s,%d' % (clusters_countries[i][j],clusters[i][j])
				count += 1
			print("\n")
		print 'Total Countries = %d' % (count)
		plt.show()

		print(sum_of_squared_error)

MAIN()
