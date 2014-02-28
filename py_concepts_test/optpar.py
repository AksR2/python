from optparse import OptionParser
parser=OptionParser()
parser.add_option('-e','--hosts',type='string',dest='hostname',help=("ESX servers to be installed"))
parser.add_option('-b','--build',type='string',dest='buildnum',help=("Build number to be installed"))

(options,args)=parser.parse_args()
print options
print args