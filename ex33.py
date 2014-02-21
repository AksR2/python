i=0
numbers=[]
def func1(x):
	global i
	while i<x:
		print "At the top i is %d"%i
		numbers.append(i)
	
		i=i+1
		
		print "numbers now:", numbers
		print "At the bottom i is %d" %i

	
	print "The numbers:"

	for num in numbers:
		print num
x1=raw_input(">")
func1(int(x1))