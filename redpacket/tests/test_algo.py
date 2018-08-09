import sys
sys.path.append("..")
import pandas as pd
from project.lib.algo import re_rand



def test(max_time=10000):
    data = []
    min_ = 0.05
    amout = 12
    num = 10
    for i in range(max_time):
        d = re_rand(min_, amout, num, f_accurate=8)
        d.append([min_, amout, num])
        data.append(d)
    return data

if __name__ == '__main__':
    data = test()
    df = pd.DataFrame(data)

    writer = pd.ExcelWriter('./output.xlsx')
    df.to_excel(writer, 'Sheet')
    writer.save()
