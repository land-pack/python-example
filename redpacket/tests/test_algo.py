import sys
sys.path.append("..")


from project.lib.algo import re_rand


def test(max_time=100000):
    
    for i in range(5):
        d = re_rand(0.5, 5, 10, f_accurate=4)
        print(d)


if __name__ == '__main__':
    test()

