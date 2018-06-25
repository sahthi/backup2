from optparse import OptionParser
parser=OptionParser()
print parser
parser.add_option("-t","--thresahold",dest="thresh",type="int",default=90,help="set threshold(%)")
optons,args=parser.parse_args()
print"Threshold is:",thresh
print "Non optional is:",args


