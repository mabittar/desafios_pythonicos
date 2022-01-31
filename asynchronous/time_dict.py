from time import time

DICT_RANGE = 100000000

class DictTiming:
    def geta(self):
        ...

    def getb(self):
        ...

    def getc(self):
        ...

    def getd(self):
        ...

    def gete(self):
        ...

    def getf(self):
        ...

    def get(i):
        return {
            "valor_de_i": i
        }


def direct_access():
    start_time = time()
    for i in range(DICT_RANGE):
        DictTiming.get(i)
    stop_time = time() - start_time
    print(f"direct_access elapsed time: {stop_time} s")
    return stop_time

def pointed_access():
    start_time = time()
    get = DictTiming.get
    for i in range(DICT_RANGE):
        get(i)
    stop_time = time() - start_time
    print(f"pointed_access elapsed time: {stop_time} s")
    return stop_time

if __name__=="__main__":
    direct = direct_access()
    pointed = pointed_access()
    div = pointed / direct
    print(f"pointed / direct = {div}")
