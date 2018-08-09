import hashlib
from project.lib.db import rdx

RED_PACKGE_LIST = 'red_packet_list_{}'

def my_hash(oid):
    return  hashlib.md5(str(oid)).hexdigest()

def my_key(oid):
    key_sub= my_hash(oid)
    key = RED_PACKGE_LIST.format(key_sub)
    return key


def pack_red_packet(lst, oid, ex=24*60*60, privi=True):
    key_sub= my_hash(oid)
    key = RED_PACKGE_LIST.format(key_sub)
    rdx.sadd(key, *lst)
    rdx.expire(key, ex)
    return key_sub


def pop_one(key):
    key = RED_PACKGE_LIST.format(key)
    return rdx.spop(key)

def pull_back(key, oid):
    key = RED_PACKGE_LIST.format(key)
    rdx.sadd(key, oid)

def is_exists(key):
    key = RED_PACKGE_LIST.format(key)
    s = rdx.exists(key)
    return s


if __name__ == '__main__':
    #ret = pack_red_packet([1,2,3,4], 12)
    #print(ret)
    pass

