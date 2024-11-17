from mpmath import mpf, log, expm1
from infsumpy.utils import logsumexp


def RatioTestSum(f, M, L, eps, initial_k):
    ''' Assuming that the series passes the ratio test, we obtain an approximation with guaranteed error.
    
    Parameters:
    f                 (function): Log of the terms function
    M                      (int): Maximum number of iterations
    L                    (float): Parameter of the test ratio
    eps                  (float): Error tolerance
    initial_k              (int): Start of the sum

    Return: (iterations, approximation in log-scale)
    '''
    k = initial_k
    L = mpf(L)
    eps = mpf(eps)
    leps = log(eps)
    log_terms = [log(mpf(0))] * (M+initial_k)

    # Aux function
    def term(k):
        return log(mpf(f(k)))

    # Check the monotonicity of the ratio
    if L == 1:
        raise ValueError("Pass a L to the ratio in the interval [0, 1].")
    elif L == 0:
        is_decreasing = True
    else:
        is_decreasing = term(M) - term(M-1) > log(L)

    # Check if is the M sufficient
    if ((is_decreasing and term(M) - log(- expm1(term(M) - term(M-1))) >= log(mpf(2)) + leps)
        or (not is_decreasing and term(M) + log(L) - log(1 - L) >= log(mpf(2)) + leps)):
        raise ValueError("It is not possible to reach the stopping criterion with the given M.")

    log_terms[k] = term(k)
    log_terms[k+1] = term(k+1)
    k+=1

    while ((log_terms[k] >= log_terms[k-1] or
           (is_decreasing and log_terms[k] - log(- expm1(log_terms[k] - log_terms[k-1])) >= log(mpf(2)) + leps) or 
           (not is_decreasing and log_terms[k] + log(L) - log(1 - L) >= log(mpf(2)) + leps)) and
           k < M+initial_k):
        k+=1
        log_terms[k] = term(k)
    
    # Compute the log(sum) (the range improve performance)
    log_sum = logsumexp(log_terms[initial_k:(k+1)])

    # Compute the boundings and return the midpoint of the interval
    Bound1 = log_terms[k] + log(L) - log(1 - L)
    Bound2 = log_terms[k] - log(- expm1(log_terms[k] - log_terms[k-1]))
    return (k-initial_k, logsumexp([log_sum, Bound1 - log(mpf(2)), Bound2 - log(mpf(2))]))