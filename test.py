from infsumpy.infsum import infsum

def f(n):
    return n / (2 ** n)

print(infsum(f, 'fixed', 10**4, 1))
print(infsum(f, 'threshold', 10**4, 1))