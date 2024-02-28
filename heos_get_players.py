import telnetlib 
from myconfig import *

# main sequence
myconf = myconfig()
myconf.vimport('radio.ini')
  
# Connect to the Telnet server 
tn = telnetlib.Telnet(myconf.ipx, myconf.portx)
  
# Send a command to the server 
tn.write(b"heos://player/get_players\n")
  
# Read the output from the server
all_result = tn.read_until(b"FIN\n", timeout = 1).decode('ascii')
  
# Print the output 
print(str(all_result))
tn.close() 
