from infsumpy.utils import logsumexp
from mpmath import mpf, log

def IntegralTestSum(f, g, M, eps, initial_k):
    ''' Assuming that the series passes the integration test, we obtain an approximation with guaranteed error.
    
    Parameters:
    f                 (function): Log of the terms function
    g                 (function): Integral of n to infinity of f
    theta (first parameter of f): Parameter of the function
    M                      (int): Maximum number of iterations
    eps                  (float): Error tolerance
    initial_k              (int): Start of the sum

    Return: (iterations, approximation in log-scale)
    '''
    k = initial_k
    eps = mpf(eps)
    leps = log(eps)
    log_terms = [log(mpf(0))] * (M + initial_k)

    if g == None:
        raise ValueError("g must be a function of the natural numbers to the real numbers.")

    if (log(mpf(g(M))) > log(mpf(2)) + leps):
        raise ValueError("It is not possible to reach the stopping criterion with the given M.")

    log_terms[k] = log(mpf(f(k)))
    k+=1

    while (log(mpf(g(k))) > log(mpf(2)) + leps):
        log_terms[k] = log(mpf(f(k)))
        k+=1
    
    log_sum = logsumexp(log_terms[initial_k:(k+1)])

    return (k-initial_k, logsumexp([log_sum, log(mpf(g(k)))  - log(mpf(2)), log(mpf(g(k-1)))  - log(mpf(2))]))

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)