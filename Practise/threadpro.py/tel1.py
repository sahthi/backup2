import telnetlib

tn=telnetlib.Telnet("linuxzoo.net")
tn.read_until("login: "+"\n")
tn.write("root")
tn.read_until("password: "+"\n")
tn.write("secure")
tn.read_until("#")
tn.write("df -h"+"\n")
op = tn.read_until("#")

for line in op.split("\r\n"):
     print line

