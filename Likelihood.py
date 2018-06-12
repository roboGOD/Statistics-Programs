def likelihood(dist,data):
	total=1
	for d in data:
		total=total*dist[d]
	return total


dist = {'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2}
data = 'ABCEDDECAB'
print(likelihood(dist,data))