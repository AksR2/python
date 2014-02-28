class Parent(object):
	def func1(self,a,b):
		print a+b
	def override(self):
		print "Parent function."

class Child(Parent):
	def override(self):
		print "Child function."
		
a=Parent()
b=Child()
a.override()
b.override()
b.func1(2,3)