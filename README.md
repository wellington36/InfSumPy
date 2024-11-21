![InfSumPy Logo](https://github.com/wellington36/InfSumPy/raw/main/man/figures/logo_README.png)

--------------------------------------------------------------------------------
![PyPI](https://img.shields.io/pypi/v/InfSumPy?label=pypi%20package)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
![example workflow](https://github.com/wellington36/InfSumPy/actions/workflows/test_infsum.yml/badge.svg)

InfSumPy is a Python package that evaluates infinite positive sums with guaranteed error.
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
We have the transformations implemented above, and for use, we have the `infsum` function.
Which receives from input:

- _A series_: In the form of a function f: $\mathbb{N} \to \mathbb{R}$.
- _Method_: Can be `ratio`, `integral`, `threshold` or `fixed`.
- _Max terms_: The maximum number of terms.
- _Start terms_: The index of the first term of the series.
- _Epsilon_ (optional): The expected error tolerance (if the method is `ratio`, `integral` or `threshold`).
- _L_ (optional): Limit of the ratio of terms (if the method is `ratio`).
- _Integral of series_ (optional): The function of g(n) = ∫_n^∞ f(x) dx for the integral test (if the method is `integral`).
- _Precision_ (optional): The precision for the `mpmath` library (default value is 53).

The function returns the number of terms used in the sum and the approximation.

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
# g(n) = ∫_n^∞ 1/x**2 dx = 1/n, then we can evaluate with controled error
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
