# coding: utf-8
import time
time.stftime('%Y-%m-%d %H:%M:%S', '2018-09-12 12:12:12')
time.strptime('%Y-%m-%d %H:%M:%S', '2018-09-12 12:12:12')
time.strstime('%Y-%m-%d %H:%M:%S', '2018-09-12 12:12:12')
time.strptime('2018-09-12 12:12:12', "%Y-%m-%d %H:%M:%S")
time.strptime('2018-09-12 12:12:12', "%Y-%m-%d")
time.strptime('2018-09-12 12:12:12', "%Y-%m-%d %H:%M:%S")
t = time.strptime('2018-09-12 12:12:12', "%Y-%m-%d %H:%M:%S")
t
dir(t)
time.mktime(t)
ss = time.mktime(t)
datetime.datetime.fromtimestamp(ss)
import datetime
datetime.datetime.fromtimestamp(ss)
datetime.datetime.fromtimestamp(ss).date
datetime.datetime.fromtimestamp(ss).date()
d =datetime.datetime.fromtimestamp(ss).date()
str(d)
datetime.datetime('2018-09-12 12:12:12')
dir(datetime)
dir(datetime.time)
from datetime import datetime
datetime.strptime('2018-08-12 12:12:21', "%Y-%m-%d %H:%M:%S")
datetime.strptime('2018-08-12 12:12:21', "%Y-%m-%d %H:%M:%S").date()
import pandas as pd
d =[array([10,  1,  7,  3]),
 array([ 0, 14, 12, 13]),
 array([ 3, 10,  7,  8]),
 array([7, 5]),
 array([ 5, 12,  3]),
 array([14,  8, 10])]
d =pd.Array([10,  1,  7,  3],
    [ 0, 14, 12, 13],
 [ 3, 10,  7,  8],
 [7, 5],
 [ 5, 12,  3],
[14,  8, 10])
import numpy as np
d =np.Array([10,  1,  7,  3],
    [ 0, 14, 12, 13],
 [ 3, 10,  7,  8],
 [7, 5],
 [ 5, 12,  3],
[14,  8, 10])
dir(np)
dir(np.array)
d =np.array([10,  1,  7,  3],
    [ 0, 14, 12, 13],
 [ 3, 10,  7,  8],
 [7, 5],
 [ 5, 12,  3],
[14,  8, 10])
d =np.array([[10,  1,  7,  3],
    [ 0, 14, 12, 13],
 [ 3, 10,  7,  8],
 [7, 5],
 [ 5, 12,  3],
[14,  8, 10]])
d
d =[[10,  1,  7,  3],
    [ 0, 14, 12, 13],
 [ 3, 10,  7,  8],
 [7, 5],
 [ 5, 12,  3],
[14,  8, 10]]
d
np.where
help(np.where)
np
