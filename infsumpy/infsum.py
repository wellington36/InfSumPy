from .methods.fixed_method import FixedSum
from .methods.threshold_method import ThresholdSum
from .methods.ratio_test_method import RatioTestSum
from .methods.integral_test_method import IntegralTestSum

from mpmath import mp, exp, mpf

def infsum(f, method: str, M: int, initial: int, eps=mpf(2)**mpf(-52), L=mpf(1), g=None, precision = 53):
    mp.prec = precision

    if method == 'fixed':
        r = FixedSum(f, M, initial)
    elif method == 'threshold':
        r = ThresholdSum(f, M, eps, initial)
    elif method == 'ratio':
        r = RatioTestSum(f, M, L, eps, initial)
    elif method == 'integral':
        r = IntegralTestSum(f, g, M, eps, initial)
    else:
        raise ValueError(f"Method {method} not supported, try 'ratio', 'integral', 'threshold' or 'fixed'")
    
    return (r[0], float(exp(r[1])))

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)