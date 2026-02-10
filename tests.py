from infsumpy.methods.fixed_method import FixedSum
from infsumpy.methods.threshold_method import ThresholdSum
from infsumpy.methods.ratio_test_method import RatioTestSum
from infsumpy.methods.integral_test_method import IntegralTestSum

from infsumpy.infsum import infsum

from mpmath import exp, log, mp, pi
import pytest

#################### Test Import ##########################
import infsumpy

#################### Auxiliar function ####################
def f(n):
    return n / (2 ** n)

def g(n):
    return 1/n**2

def dg(n):
    return 1/n

def equivalence(a, b, epsilon=0.0001):
    if a == b:
        return True
    else:
        return abs(a - b) < epsilon
    
#################### TESTS ##########################
def test_methods():
    eps = 10**(-3)

    fixed = infsum(f, 'fixed', 10**4, 1)
    threshold = infsum(f, 'threshold', 10**4, 1, eps=eps)
    ratio_test = infsum(f, 'ratio', 10**4, 1, L=1/2, eps=eps)
    integral_test = infsum(g, 'integral', 10**3, 1, eps=eps, g=dg)

    assert equivalence(fixed[1], 2, epsilon=eps)
    assert equivalence(threshold[1], 2, epsilon=eps)
    assert equivalence(ratio_test[1], 2, epsilon=eps)
    assert equivalence(integral_test[1], pi**2/6, epsilon=eps)

def test_invalid_method_raises_error():
    with pytest.raises(ValueError, match="not supported"):
        infsum(f, 'unsupported_method', 10**4, 1)



if __name__ == '__main__':
    test_methods()
    test_invalid_method_raises_error()
