from time import time

DICT_RANGE = 1000

class DictTiming:
    def get(i):
        return {
            "valor_de_i": i
        }
class KeyTiming:
    def get(i):
        dict_test = {"valor_de_i": i}
        return dict_test["valor_de_i"]


def direct_access():
    start_time = time()
    for i in range(DICT_RANGE):
        DictTiming.get(i)
    stop_time = time() - start_time
    print(f"direct_access elapsed time: {stop_time} s")
    return stop_time

def pointed_access():
    start_time = time()
    dict_get = DictTiming.get
    for i in range(DICT_RANGE):
        dict_get(i)
    stop_time = time() - start_time
    print(f"pointed_access elapsed time: {stop_time} s")
    return stop_time

def pointed_key():
    start_time = time()
    for i in range(DICT_RANGE):
        KeyTiming.get(i)
    stop_time = time() - start_time
    print(f"pointed_access elapsed time: {stop_time} s")
    return stop_time

if __name__=="__main__":
    direct = direct_access()
    pointed = pointed_access()
    pointed = pointed_key()
    div = pointed / direct
    print(f"pointed / direct = {div}")
    
    
    
import operator
