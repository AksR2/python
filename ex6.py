#%d replaced by ten
x = "There are %d types of people." %10
binary = "binary"
do_not="don't"
#%s replaced  by the two variables
y="those who know %s and those who %s" %(binary,do_not)
print x
print y
#%r not sure.
print "I said: %r." %x
print "I also said : '%s'." %y
hilarious =False
#%r used for boolean
joke_evaluation="Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e=" a string with a right side."
#string appended together
print w+e
 