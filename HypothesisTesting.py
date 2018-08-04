import math

def reallyMean(data):
	return float(sum(data))/float(len(data))

def variance(data):
	mean = reallyMean(data)
	return sum([(x-mean)**2 for x in data])/len(data)

def factor(data):
	return 1.96

def conf(data):
	var = variance(data)
	a = factor(data)

	return a*math.sqrt(var/len(data))

def test(data, h):
	m = reallyMean(data)
	c = conf(data)
	if h >= m-c and h <= m+c:
		return True
	return False

data = [199, 200, 201, 202, 203, 204]
h = 201

if test(data, h):
	print "Yes!"
else:
	print "No!"



