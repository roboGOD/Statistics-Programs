
def meaner(cm,cc,n):
	return (cm*cc+n)/(cc+1)

currentMean = 10
currentCount = 5
new = 4
newMean = meaner(currentMean,currentCount,new)

print(newMean)