from decimal import Decimal
from functools import singledispatch


@singledispatch
def calc_num(num):
    raise NotImplementedError("Unknown number type error")


@calc_num.register(int)
def _calc_int(num):
    print(f"Dispatch for int: {num}")

    # The decorator also support stacking


@calc_num.register(float)
@calc_num.register(Decimal)
def _calc_float(num):
    print(f"Dispatch for float or decimal {num}")


if __name__ == '__main__':
    try:
        calc_num(1)
        calc_num(1.12)
        calc_num(Decimal(1.22))

    except Exception as e:
        print(e)
    finally:
        print("Done!")
