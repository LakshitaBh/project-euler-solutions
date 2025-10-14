import math
from sympy import primerange

def lcm(n):
    lcm = 1
    for i in range(1, n):
        lcm = math.lcm(i, lcm)
    return lcm

def lcm_efficient(n):
    '''
        n = p1^a1 * p2^a2 * ... * pk^ak where k is the number of primes <= n
        At the max pi^ai = n. Take log on both sides
        ai = floor(log(n)/log(pi))
        -> much faster
    '''
    lcm = 1
    for p in primerange(1, n+1):
        a = math.floor(math.log(n)/math.log(p))
        lcm *= p**a
    return lcm
    

if __name__=="__main__":
    print(lcm(20))
    print(lcm_efficient(20))