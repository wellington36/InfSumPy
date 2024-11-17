from .methods.fixed_method import FixedSum
from .methods.threshold_method import ThresholdSum
from .methods.ratio_test_method import RatioTestSum

from mpmath import mp, exp, mpf

def infsum(f, method: str, M: int, initial: int, eps=mpf(2)**mpf(-52), L=mpf(0), precision = 53):
    mp.prec = precision

    if method == 'fixed':
        return exp(FixedSum(f, M, initial))
    elif method == 'threshold':
        return exp(ThresholdSum(f, M, eps, initial))
    elif method == 'ratio':
        return exp(RatioTestSum(f, M, L, eps, initial))
    else:
        raise ValueError(f"Method {method} not supported, try 'fixed'")

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)