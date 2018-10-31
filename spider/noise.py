import time
import sys
for i in range(1,6):
    sys.stdout.write('\r\a{i}'.format(i=i))
    sys.stdout.flush()
    time.sleep(1)
sys.stdout.write('\n')
