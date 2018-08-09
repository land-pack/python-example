from datetime import datetime
from collections import defaultdict
import pandas as pd

group_by_date = defaultdict(list)

sample = [
    {"timestamp": "2017-08-01 12:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-01 22:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-11 12:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-21 14:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-21 12:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-11 19:12:12", "data":"fuck data"},
    {"timestamp": "2017-08-01 02:12:12", "data":"fuck data"}
]

for i in sample:

    the_date = datetime.strptime(i.get("timestamp"), "%Y-%m-%d %H:%M:%S").date()
    group_by_date[str(the_date)].append(i.values())

df = pd.DataFrame.from_dict(group_by_date, orient='index')
writer = pd.ExcelWriter('./output.xlsx')

df2 = df.T

df2.to_excel(writer,'Sheet')
writer.save()
