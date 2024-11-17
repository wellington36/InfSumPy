![InfSumPy Logo](https://github.com/wellington36/InfSumPy/blob/main/man/figures/logo_README.png)

--------------------------------------------------------------------------------

InfSumPy is a Python package that evaluates infinite positive sums with a guaranteed error.
Using ratio and integral tests we evaluate series that pass these tests with controlled error.

## Instalation

Make sure you have the mpmath library installed:

```bash
pip install mpmath
```

To install the package, run the following command:

```bash
pip install infsumpy
```

# Usage
### Ratio test
```py
from infsumpy import infsum

# the infinity sum of n/(2**n) pass in the ratio test with limit L = 1/2,
# then we can evaluate with controled error
print(infsum(lambda n: n/(2**n), 'ratio', 10**4, 1, eps=2**(-52), L=1/2))
```

### Integral test
```py
from infsumpy import infsum

# the infinity sum of 1/n**2pass in the integral test with integral g(n),
# then we can evaluate with controled error
print(infsum(lambda n: n/(2**n), 'ratio', 10**4, 1, eps=2**(-52), L=1/2))
```

# Methods

[[Bla bla bla]]

# Notes

[[Bla bla bla]]
