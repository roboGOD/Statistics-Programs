
def bayes(p0,p1,p2,boola) :
	if boola is 0 :
		return p0*p1 / ( p0*p1+(1-p0)*(1-p2) )
	else :
		return p0*(1-p1) / ( p0*(1-p1)+(1-p0)*p2 )

p0 = float(input('Enter Prior \t\t: '))
p1 = float(input('Enter Sensitivity \t: '))
p2 = float(input('Enter Specitivity \t: '))
p3 = int(input('Enter 0:Positive or 1:Negative : '))

print 'Posterior Probability \t: ' + str(bayes(p0,p1,p2,p3))
