N=int(input())
if  N <= 1000:
	A=[int(x) for x in raw_input().split()]
	A.sort()
	print " ".join(map(str,A))
