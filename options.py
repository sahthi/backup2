from optparse import OptionParser

parser = OptionParser()

parser.add_option("-t", dest="threshold", type="int", default=90, help="set threshold (%)")

options,args = parser.parse_args()


print "Threshold you entered is:", options.threshold
print "Non optional arguments:", args
