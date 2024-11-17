from mpmath import mp, exp, log, fsum, fmul, fabs, inf, eps, expm1

def logsumexp(a: list):
    a_max = max(a)

    return a_max + log(fsum([exp(ai - a_max) for ai in a]))

def fma(a, b, c):
    with mp.extradps(100):  # Extra precision for more accurate result
        return fmul(a, b) + c

def logdiffexp(a, b):
    if b > a:
        a, b = b, a
    
    with mp.extradps(100):  # Increase precision
        diff = b - a
        
        # If a ≈ b, avoid precision loss
        if fabs(diff) < log(eps):
            return -inf  # Return negative infinity if the result is too close to 0
        
        # Compute log(exp(a) - exp(b)) using the trick
        return a + log(-expm1(diff))