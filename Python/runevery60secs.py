import time
import datetime
starttime=time.time()
while True:
  print("tick -",datetime.datetime.now().strftime(("%d-%m-%Y   %I:%M:%S.%f")) )
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
