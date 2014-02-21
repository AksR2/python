from sys import argv
#unpacking of command line arguments
script,user_name=argv
prompt='>'
print "Hi %s,I'm the %s script" %(script,user_name)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" %user_name
like=raw_input(prompt);