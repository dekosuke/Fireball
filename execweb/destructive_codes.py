"""examples of destructive program inputs, which might cause exec server unstable"""

["import time\nwhile True:sleep(0.1)","python"] #infinite loop
["import time\nwhile True:print 'hoge'","python"] #infinite message loop
["import os;os.system('ls')","python"] #exec
["range(1000000000)","python"] #consume memory
["9**9**9**9**9","python"] #consume cpu



