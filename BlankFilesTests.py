'''version notes- 
thius version works bu twill keep the files of any time the device shut off. thte delete function needs to be made independant of the rest
'''
import time 
import os
neo=''
time_keep=30#seconds before deleting, must be a multiple of file lenght
file_length=30#just a capture interval for now
while True:
  t=time.time()
  t=t-t%file_length#essentially rounds to thre nearest interval, so doesent matter when you start
  neo=open(str(t),'w')#insert mic code here
  if os.path.exists(str(t-time_keep)):
    os.remove(str(t-time_keep))
  else:
    print("The file does not exist",t-time_keep)
  time.sleep(file_length-1)

