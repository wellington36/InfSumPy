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

print("vjzfbvkuaybikaru")

print(infsum(lambda n: n/(2**n), 'ratio', 10**4, 1, eps=2**(-52), L=1/2))
print(infsum(lambda n: 1/(n**2), 'integral', 10**4, 1, eps=10**(-3), g=lambda n: 1/n))
print(infsum(lambda n: n/(2**n), 'threshold', 10**4, 1, eps=2**(-52)))
print(infsum(lambda n: n/(2**n), 'fixed', max_terms=10**4, initial=1))