from math import exp
from unicodedata import name
REGISTRY = {}

def register(name):
    def _decorator(fn):
        REGISTRY[name] = fn
        return fn
    return _decorator

@register("relu")
def rectified(x):
    return x if x > 0 else 0


@register("sigmoid")
def sigmoid(x):
    return 1 / (1 + exp(-x))

def active(x, func_name):
    if func_name not in REGISTRY:
        raise NotImplementedError(f"Function {func_name} is not implemented!!!")
    else:
        func = REGISTRY[func_name]
        return func(x)



if __name__ == "__main__":
    print(active(1.23, "relu"))
    print(active(1.23, "sigmoid"))
    print(active(1.23, "tanh"))    