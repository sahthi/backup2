
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   flag = 0
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   opt_list = []
   for opt,args in opts:
      opt_list.append(opt)
   if "-i" in opt_list and "-o" in opt_list:
      pass
   else:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit()
      
     

  
   
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
	 outputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

   with open(inputfile) as fp:
      data = fp.readlines()
      sum_num = 0
      for i in data:
          sum_num = sum_num+int(i)
      
   with open(outputfile,"w") as f:
      f.write(str(sum_num))

    

   

if __name__ == "__main__":
   main(sys.argv[1:])
