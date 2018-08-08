import random
import time
from decimal import Decimal


def accurate(n, b=8):
    return round(Decimal(n), b)


def re_rand(min_value, amount, number):

    ava_lst = []
    origin_max = amount
    for i in range(number):
        max_value = accurate(accurate(amount - sum(ava_lst)) / (number - i))
        mid = random.randrange(min_value, max_value, _int=float)
        if mid >= min_value:
            mid = accurate(mid)
            ava_lst.append(mid)
        else:
            print("invalid value =%s" % mid)

    ava_lst.sort()
    print('after sort', ava_lst)
    ava_lst[0] = accurate(ava_lst[0] + (amount - accurate(sum(ava_lst))))
    print('after add addition part', ava_lst)
    random.shuffle(ava_lst)
    return ava_lst
    

def generate(amount, number, min_value=0.05, f_type=0, scale=2):
    """
    @param f_type: 0 normal, 1 is random
    """
    if f_type == 0:
        lst = [accurate(accurate(amount) / number)] * number
        lst[0] = accurate(lst[0] + (amount - accurate(sum(lst))))
        return lst

    elif f_type == 1:
        pass

    else:
        
        return 

if __name__ == '__main__':
    print("Amount 12 | number 11")
    #d = generate(12, 11)
    #s = sum(d)
    #print(d)
    #print(s)

    #print(re_rand(4, 7))


    ls = re_rand(5, 100, 10)

    print(ls)
    print(sum(ls))
    print(len(ls))
