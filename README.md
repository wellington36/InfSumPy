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
print(infsum(lambda n: n/(2**n), 'ratio', max_terms=10**4, initial=1, eps=2**(-52), L=1/2))
```

```bash
> (56, 2.0)
```

### Integral test
```py
from infsumpy import infsum

# the infinity sum of 1/n**2 pass in the integral test with integral
# g(n) = ∫_n^∞ 1/n**2 = 1/n, then we can evaluate with controled error
print(infsum(lambda n: 1/(n**2), 'integral', max_terms=10**4, initial=1, eps=10**(-3), g=lambda n: 1/n))
```

```bash
> (499, 1.64493406229104)
```

### Threshold (not guaranteed)
```py
from infsumpy import infsum

# we can also use a stoping criterio such that sum until the n-th are less
# than the epsilon, here for the infinity sum of 2/(2**n)
print(infsum(lambda n: n/(2**n), 'threshold', max_terms=10**4, initial=1, eps=2**(-52)))
```

```bash
> (57, 2.0)
```

### Fixed (not guaranteed)
```py
from infsumpy import infsum

# we can just sum a fixed number of terms of the infinite sum of 2/(2**n)
print(infsum(lambda n: n/(2**n), 'fixed', max_terms=10**4, initial=1))
```

```bash
> (10000, 2.0)
```
