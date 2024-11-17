from .methods.fixed_sum import FixedSum
from .methods.threshold_sum import ThresholdSum

from mpmath import mp, exp, mpf

def infsum(f, method: str, M: int, initial: int, eps=mpf(2)**mpf(-52), precision = 53):
    mp.prec = precision

    if method == 'fixed':
        return exp(FixedSum(f, M, initial)[1])
    elif method == 'threshold':
        print("vravrv")
        return exp(ThresholdSum(f, M, eps, initial)[1])
    else:
        raise ValueError(f"Method {method} not supported, try 'fixed'")

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)