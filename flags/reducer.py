#!/usr/bin/env python
from operator import itemgetter
import sys
import random
import bisect
import collections  
import matplotlib.pyplot as plt
import numpy as np
import math
from shutil import copyfile
from os import listdir
from os.path import isfile, join
import os

current_word = None
current_feature = None

features = []
features1 = []
features2 = []

countries = []

"""
centeroids = []
centeroids_countries = []

clusters = [[]]
clusters_countries = [[]]
"""
sum_of_squared_error = []

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

##RANDOM SAMPLING
def random_sampling(population):
	n = random.sample(features, 1)
	return n[0]


##CALCULATING CENTRES OF CENTEROIDS
def compute_centeroids(centeroids, centeroids_countries, k):
	weights = []
	c1 = random_sampling(features1)
	#c2 = random_sampling(features2)

	centeroids.append(c1)
	index1 = features.index(c1)
	country1 = countries[index1]
	#print (centeroids,country1)
	
	centeroids_countries.append(country1)
	for i in range(0,k-1):
		for j in range(0,len(features)):
			small = max(features)
			for l in range(0,len(centeroids)):
				di = 0
				for m in range(0, len(features[0])):
					di += math.sqrt((features[j][m]-centeroids[l][m])**2)
				#print(di) 
				#print 'di=%d'%(di)
				if(di<small):
					small = di
			di_final = small
			#print 'di_final=%d'%(di_final)
			#print()
			weights.append(di_final)

		
		sum_weights = sum(weights)
		weights = [float(x)/sum_weights for x in weights]
		#print(weights)
		#print("Weights",weights)
		cn = weighted_sampling(weights, features)
		centeroids.append(cn)  

		indexn = features.index(cn)
		countryn = countries[indexn]
		centeroids_countries.append(countryn)  
		#print(centeroids)
		#print(centeroids_countries)

		weights=[]   
		#print '%d:%s' % (cn,countryn)  
	print("\n")
	return centeroids, centeroids_countries     

def k_means(centeroids, centeroids_countries, k):
	clusters = [[]]
	clusters_countries = [[]]
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

		count = 0		
		
		for i in range(len(features)):
			dist_list = []
			for j in range(len(centeroids)):
				#print("\n")
				#print(i,j)
				#print(len(features[i]))
				#print(len(centeroids[i]))
				dist = 0
				for m in range(0,13):
					#print(i,j,m)
					#print(features[i][m])
					#print(centeroids)
					dist += pow(features[i][m]-centeroids[j][m], 2)
				dist_list.append(dist)

			#print(dist_list)
			min_dist_index = dist_list.index(min(dist_list))
			clusters[min_dist_index].append(features[i])
			clusters_countries[min_dist_index].append(countries[i])

			#print(len(clusters))
			#print(len(clusters_countries))

			sum_errors += min(dist_list)

			sum_0=sum_1=sum_2=sum_3=sum_4=sum_5=sum_6=sum_7=sum_8=sum_9=sum_10=sum_11=sum_12=sum_13=0
			#centeroids[min_dist_index] = sum(clusters[min_dist_index])/len(clusters[min_dist_index])
			ll = []
			for i in range(len(clusters[min_dist_index])):
				sum_0 = clusters[min_dist_index][i][0] + sum_0
				sum_1 = clusters[min_dist_index][i][1] + sum_1
				sum_2 = clusters[min_dist_index][i][2] + sum_2
				sum_3 = clusters[min_dist_index][i][3] + sum_3
				sum_4 = clusters[min_dist_index][i][4] + sum_4
				sum_5 = clusters[min_dist_index][i][5] + sum_5
				sum_6 = clusters[min_dist_index][i][6] + sum_6
				sum_7 = clusters[min_dist_index][i][7] + sum_7
				sum_8 = clusters[min_dist_index][i][8] + sum_8
				sum_9 = clusters[min_dist_index][i][9] + sum_9
				sum_10 = clusters[min_dist_index][i][6] + sum_10
				sum_11 = clusters[min_dist_index][i][7] + sum_11
				sum_12 = clusters[min_dist_index][i][8] + sum_12
				sum_13 = clusters[min_dist_index][i][9] + sum_13
				"""
				print(len(clusters[min_dist_index][0]))
				sum_each = 0
				for b in range(len(clusters[min_dist_index][0])):
					sum_each += clusters[min_dist_index][i][b] + sum_each
				ll.append(float(sum_each)/float(len(clusters[min_dist_index])))
				"""
				clus_len = float(len(clusters[min_dist_index]))
			centeroids[min_dist_index] = (float(sum_0)/clus_len , float(sum_1)/clus_len, float(sum_2)/clus_len, float(sum_3)/clus_len, float(sum_4)/clus_len, float(sum_5)/clus_len, float(sum_6)/clus_len, float(sum_7)/clus_len, float(sum_8)/clus_len, float(sum_9)/clus_len, float(sum_10)/clus_len, float(sum_11)/clus_len, float(sum_12)/clus_len, float(sum_13)/clus_len)
			#centeroids[min_dist_index] = (float(sum_X)/float(len(clusters[min_dist_index])), float(sum_Y)/float(len(clusters[min_dist_index])))

		if(clusters==clusters_prev):
			#print(count)
			break
		clusters_prev = clusters

		for i in range(k):
			clusters.pop()
			clusters_countries.pop()
		count += 1
	sum_of_squared_error.append(sum_errors)
	print(sum_of_squared_error)
	return clusters, clusters_countries

def sort_countries_centeroids(A,B):
	for i in range( len( A ) ):
		for k in range( len( A ) - 1, i, -1 ):
			if ( A[k] < A[k - 1] ):
				swap( A, k, k - 1 )
				swap( B, k, k - 1)
	return A,B

def swap( A, x, y ):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

def MAIN():
		for line in sys.stdin:
			# remove leading and trailing whitespace
			line = line.strip()
			words = line.split("\t")
			# parse the input we got from mapper.py
			current_country = words[0]			#name
			current_feature1 = words[1]			#bars
			current_feature2 = words[2]			#stripes
			current_feature3 = words[3]			#colors
			current_feature4 = words[4]		#red
			current_feature5 = words[5]		#circles
			current_feature6 = words[6]		#crosses
			current_feature7 = words[7]		#saltires
			current_feature8 = words[8]		#quarters
			current_feature9 = words[9]		#crescent
			current_feature10 = words[10]		#triangles
			current_feature11 = words[11]		#icon
			current_feature12 = words[12]		#animate
			current_feature13 = words[13]		#text

			#print '%s,%s' % (current_country, current_feature)
			features.append((int(current_feature1), int(current_feature2), int(current_feature3), int(current_feature4), int(current_feature5), int(current_feature6), int(current_feature7), int(current_feature8), int(current_feature9), int(current_feature10), int(current_feature11), int(current_feature12), int(current_feature13)))
			features1.append(int(current_feature1))
			#features2.append(int(current_feature2))
			countries.append(current_country)
		
		print(len(features[0]))

		val = 0

		for k in range(8,9):
			for i in range(1,k):
				folder = '/media/saumay/W Files2/PADHAI/WINTER SEM 3/Subjects/E2-Data Mining/Project/Clusters_of_flags/Cluster ' + str(i)
				for the_file in os.listdir(folder):
				    file_path = os.path.join(folder, the_file)
				    try:
				        if os.path.isfile(file_path):
				            os.unlink(file_path)
				        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
				    except Exception as e:
				        print(e)

			centeroids = []
			centeroids_countries = []

			centeroids,centeroids_countries = compute_centeroids(centeroids, centeroids_countries, k)
			print(centeroids)
			print(centeroids_countries)
			#centeroids,centeroids_countries = sort_countries_centeroids(centeroids, centeroids_countries)
			
			#print "Centeroids:",centeroids
			#print "Countries corresponding to centeroids:",centeroids_countries

			clusters, clusters_countries = k_means(centeroids, centeroids_countries, k)
			count = 0

			print "\nFOR k=%d" % (k)
			for i in range(k):
				#print "%s:" % (labels[i%5])
				print '\nCluster %d:' % (i+1)
				#print clusters[i]
				val = 0
				"""
				X = []
				Y = []
				for coordinate in range(1,len(clusters[i])):
					X.append(clusters[i][coordinate][0])
					Y.append(clusters[i][coordinate][1])
				plt.plot(X, Y, '.')
				"""
				#plt.scatter(clusters[], np.zeros_like(clusters[7]))
				for j in range(1, len(clusters[i])):
					print clusters_countries[i][j],clusters[i][j]
					src = "/media/saumay/W Files2/PADHAI/WINTER SEM 3/Subjects/E2-Data Mining/Project/Flags_of_all_countries/"
					country = clusters_countries[i][j].lower()
					src += country + " flag/"
					src += country + ".png"
					#print(src)
					dest = "/media/saumay/W Files2/PADHAI/WINTER SEM 3/Subjects/E2-Data Mining/Project/Clusters_of_flags/"
					dest += "Cluster "+str(i+1) + "/"
					dest += country+".png"
					#print(dest)
					count += 1
					copyfile(src, dest)
				print("\n")
			print 'Total Countries = %d' % (count)
			print("Total error = "+str(sum_of_squared_error[0]))
		"""
		#plt.show()
		print(sum_of_squared_error)
		k_values = [x for x in range(2,15)]
		print(len(sum_of_squared_error),len(k_values))
		plt.plot(k_values, sum_of_squared_error)
		plt.show()
		"""
MAIN()
