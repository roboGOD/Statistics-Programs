import math
import random
import matplotlib.pyplot as plt

def Flip(n):
	#list = []
	#for i in range(n):
	#	list.append(random.random() > 0.5)
	#return list
	return [random.random() > 0.5 for i in range(n)]

def reallyMean(data):
	return sum(data)/len(data)

def variance(data):
	mean = reallyMean(data)
	return reallyMean([(x-mean)**2 for x in data])

def stddev(data):
	return math.sqrt(variance(data))

def createNMeans(N):
	return [reallyMean(Flip(i+1)) for i in range(N)]

N = 1000
f = Flip(N)
print(reallyMean(f))
print(stddev(f))

means = createNMeans(N)
plt.hist(means,range=(0.4,0.6),bins=30)
plt.show()