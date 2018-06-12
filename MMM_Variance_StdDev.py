import math

def reallyMean(data):
	return sum(data)/len(data)

def manInTheMedian(data):
	srt = sorted(data)
	index = (len(data)-1)/2
	return srt[index]

def justMode(data):
	counter = 0
	for i in range(len(data)):
		if(data.count(data[i]) > counter):
			counter = data.count(data[i])
			index = i
	return data[index]

def variance(data):
	mean = reallyMean(data)
	#ndata = []
	#for i in data:
	#	ndata.append((i-mean)**2)
	#return reallyMean(ndata)
	return reallyMean([(x-mean)**2 for x in data])

def stddev(data):
	return math.sqrt(variance(data))

data = [1,2,5,10,-20,5,5]
data1 = [49,66,24,98,37,64,98,27,56,93,68,78,22,25,11]
data2 = [13.04,1.32,22.65,17.44,29.54,23.22,17.65,10.12,26]

#print(reallyMean(data1))
#print(manInTheMedian(data1))
#print(justMode(data))
#print(variance(data2))

print(stddev(data2))