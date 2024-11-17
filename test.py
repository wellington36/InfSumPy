from infsumpy.infsum import infsum

def f(n):
    return n / (2 ** n)

def g(n):
    return 1/n**2

def dg(n):
    return 1/n

print(infsum(f, 'fixed', 10**4, 1))
print(infsum(f, 'threshold', 10**4, 1))
print(infsum(f, 'ratio', 10**4, 1, L=1/2))
print(infsum(g, 'integral', 10**6, 1, eps=10**(-5), g=dg))