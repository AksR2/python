ten_things="Apples Oranges song Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."
stuff=ten_things.split(' ')
more_stuff=["Day","Night","Song","Day","song","Day","Girl","Boy"]

while len(stuff)!=10:
	next_one=more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There's %d items now." %len(stuff)
	
print "There we go :",stuff
print "Let's do some things with stuff."
print stuff[1]
print stuff[-1]
print ' '.join(stuff)
print '#'.join(stuff[3:5])
from collections import Counter
c=Counter(more_stuff)
print c