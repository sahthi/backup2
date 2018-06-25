from subprocess import Popen,PIPE
import sys
process = Popen(['cat','pri.py'],stdout=PIPE,stderr=PIPE)
stdout,stderr=process.communicate()
if stderr:
       print "error in command execution"
       sys.exit(100)
print stdout
