import math

def reallyMean(data):
	return sum(data)/len(data)

def medianIndex(data):
	index = (len(data)-1)/2
	return index

def variance(data):
	mean = reallyMean(data)
	return reallyMean([(x-mean)**2 for x in data])

def stddev(data):
	return math.sqrt(variance(data))

def quartiles(data):
	srt = sorted(data)
	median = int(medianIndex(srt))
	m1 = median-1
	m2 = median+1
	upperQ = int(medianIndex(srt[:m1]))
	lowerQ = int(medianIndex(srt[m2:]))
	return srt[upperQ:lowerQ]

def calculateWeight(data,z):
	newData = quartiles(data)
	mean = reallyMean(newData)
	weight = mean+stddev(newData)*z
	return weight

data = [80.,85,200,85,69,65,68,66,85,72,85,82,65,105,75,80,70,74,72,70,80,60,
		80,75,80,78,63,88.65,90,89,91,1.00E+22,75,75,90,80,75,-1.00E+22,-1.00E+22,
		-1.00E+22,86.54,67,70,92,70,76,81,93,70,85,75,76,79,89,80,73.6,80,80,120,
		80,70,110,65,80,250,80,85,81,80,85,80,90,85,85,82,83,80,160,75,75,80,85,
		90,80,89,70,90,100,70,80,77,95,120,250,60]

weight = calculateWeight(data,-2.)
print(weight)
#meanMLE = MLE(newData)