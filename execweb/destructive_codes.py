"""examples of destructive program inputs, which might cause exec server unstable"""

from exec_engine import *

examples = [
["import time\nwhile True:time.sleep(0.1)","python"],\
#["import time\nwhile True:print 'hoge'","python"],\
#["import os;os.system('ls')","python"],\
#["import os;os.remove('.')","python"],\
#["range(1000000000)","python"],\
#["9**9**9**9**9","python"],\
]

#here is example and soon deleted
if True:
  e = ExecEngine()
  for example in examples:
    print example
    r =e.execCode(example[0], example[1])
    print "result is:\n"+r
