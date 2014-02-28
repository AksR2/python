from base import Base

class drv(Base):
	def _init_(self):
		pass
	def func2(self,str):
		self.func1(str)
		
a=drv()
a.func2("Akshay Rawat")