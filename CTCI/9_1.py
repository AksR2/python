def fcs(n):
	if n==1 or n==0:
		return 1
	elif n<0:
		return 0
	else:
		return fcs(n-3)+fcs(n-2)+fcs(n-1)
count=fcs(3)
print "Number of ways to climb the stairs:",count