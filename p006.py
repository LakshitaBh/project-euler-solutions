def solve(n=100):
    sq_of_sum = (n*(n+1)//2)**2
    sum_of_sq = n*(n+1)*(2*n+1)//6
    return sq_of_sum - sum_of_sq

if __name__=="__main__":
    print(solve())