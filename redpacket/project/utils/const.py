
class CASH_LOG(dict):
    RED_PACKET_SEND = 7001
    RED_PACKET_OPEN = 7002
    RED_PACKET_BACK = 7003
 
        



class ERROR_CODE(object):
    ERR_DEFAULT = 5000, "> Please report this error when you see it to <abc@gmail.com>"
    ERR_OPENED_TWICE = 5001, "Sorry! You cannot grab twice!"
    ERR_TYPE_RUQ_INT = 5002, "The number of redpacket should be a int type"
    ERR_OVER_TOTAL = 5003, "Over flow pool, decrement your number/min-value or increment your amount"


def reverse(cls):
    obj = cls()
    attr_key = dir(obj)
    for i in attr_key:
        if i.isupper():
            attr = getattr(obj, i)
            setattr(obj, i, list(reversed(attr)))
    return obj


err = reverse(ERROR_CODE)


if __name__ == '__main__':
    print(err)
    print(err.ERR_DEFAULT)

