from sys import argv
#unpacking the arguments
script,filename=argv
txt=open(filename)
print "Here's your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again=raw_input(">")
txt_again=open(file_again)

lines=txt_again.read()
print "The contents are :\n%s"%lines
txt.close()