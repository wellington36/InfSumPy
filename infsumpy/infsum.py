from .methods.fixed_method import FixedSum
from .methods.threshold_method import ThresholdSum
from .methods.ratio_test_method import RatioTestSum
from .methods.integral_test_method import IntegralTestSum

from mpmath import mp, exp, mpf

def infsum(f, method: str, max_terms: int, initial: int, eps=mpf(2)**mpf(-52), L=mpf(1), g=None, precision = 53):
    mp.prec = precision

    if method == 'fixed':
        r = FixedSum(f, max_terms, initial)
    elif method == 'threshold':
        r = ThresholdSum(f, max_terms, eps, initial)
    elif method == 'ratio':
        r = RatioTestSum(f, max_terms, L, eps, initial)
    elif method == 'integral':
        r = IntegralTestSum(f, g, max_terms, eps, initial)
    else:
        raise ValueError(f"Method {method} not supported, try 'ratio', 'integral', 'threshold' or 'fixed'")
    
    return (r[0], float(exp(r[1])))

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)