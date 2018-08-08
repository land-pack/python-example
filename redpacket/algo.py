import random
import time
from decimal import Decimal


def accurate(n, b=8):
    return round(Decimal(n), b)


def re_rand(start, end, number):
    if number == 0:
        return 

    mid = random.randrange(start, end)
    return re_rand(
    

def generate(amount, number, min_value=0.05, f_type=0, scale=2):
    """
    @param f_type: 0 normal, 1 is random
    """
    if f_type == 0:
        lst = [accurate(accurate(amount) / number)] * number
        lst[0] = accurate(lst[0] + (amount - accurate(sum(lst))))
        return lst

    elif f_type == 1:
        average = accurate(accurate(amount) / number)
        max_value = average * scale

    else:
        return 

if __name__ == '__main__':
    print("Amount 12 | number 11")
    d = generate(12, 11)
    s = sum(d)
    print(d)
    print(s)

    print(re_rand(4, 7))
