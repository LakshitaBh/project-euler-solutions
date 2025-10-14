def solve():
    res = 0
    for i in range(999, 99, -1):
        if i*i < res:
            break
        for j in range(i, 99, -1):
            prod = i*j
            if prod <= res:
                break
            if str(prod) == str(prod)[::-1]:
                res = prod
    return res

def efficient_solve():
    '''
    product is 6 digits number. So, it can be written as:
    abccba = 100000a + 10000b + 1000c + 100c + 10b + a = 100001a + 10010b + 1100c = 11(9091a + 910b + 100c)
    so the product must be divisible by 11. One of the two numbers must be multiple of 11.
    '''
    res = 0
    for i in range(999, 99, -1):
        if i*i < res:
            break
        # one of i or j must be multiple of 11
        if i % 11 == 0:
            j_start = 999
            j_step = 1
        else:
            j_start = 990  # largest 3 digit number divisible by 11
            j_step = 11
        for j in range(j_start, 99, -j_step):
            prod = i*j
            if prod <= res:
                break
            if str(prod) == str(prod)[::-1]:
                res = prod
    return res

if __name__=="__main__":
    # Largest palindrome made from the product of two 3-digit numbers
    # Most optimal is brute force
    print(solve())
    print(efficient_solve())