import math

N = 10
p = 0.8
result = []
f_N = math.factorial(N)

for k in range(N+1):
	f_k = math.factorial(k)
	f_Nk = math.factorial(N-k)
	result.append(round(f_N/(f_k*f_Nk)*(p**k)*((1-p)**(N-k)), 4))

print result