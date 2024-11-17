from infsumpy.utils import logsumexp
from mpmath import mpf, log


def ThresholdSum(f, M, eps, initial_k):
    ''' Applies the sum-to-threshold approach to obtain the approximate sum.
    
    Parameters:
    f                 (function): Log of the terms function
    M                      (int): Maximum number of iterations
    eps                  (float): Error tolerance
    initial_k              (int): Start of the sum

    Return: (iterations, approximation in log-scale)
    '''
    k = initial_k
    leps = log(mpf(eps))
    log_terms = [log(mpf(0))] * (M+initial_k)

    def term(k):
        return log(mpf(f(k)))

    if (term(M) > leps):
        raise ValueError("It is not possible to reach the stopping criterion with the given M.")

    log_terms[k] = term(k)

    while (log_terms[k] > leps and k < M-1+initial_k):
        k+=1
        log_terms[k] = term(k)

    
    log_sum = logsumexp(log_terms[initial_k:(k+1)])

    return (k-initial_k, log_sum)

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)