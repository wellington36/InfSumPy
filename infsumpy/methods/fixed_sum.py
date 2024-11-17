from infsumpy.utils import logsumexp
from mpmath import mpf, log


def FixedSum(f, M, initial_k):
    '''Compute a fixed interations of the log-sum.
    
    Parameters:
    f                 (function): Log of the terms function
    M                      (int): Maximum number of iterations
    initial_k              (int): Start of the sum

    Return: (iterations, approximation in log-scale)
    '''
    k = initial_k
    log_terms = [log(mpf(0))] * (M+initial_k+1)

    log_terms[k] = log(mpf(f(k)))
    log_terms[k+1] = log(mpf(f(k+1)))
    k+=1

    while (k < M+initial_k):
        k+=1
        log_terms[k] = log(mpf(f(k)))
    
    log_sum = logsumexp(log_terms[initial_k:(k+1)])

    return (k-initial_k, log_sum)

if __name__ == '__main__':
    print("This is a module. Do not run it directly.")
    exit(1)