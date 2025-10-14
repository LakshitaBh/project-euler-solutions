import math

def lcm(n):
    lcm = 1
    for i in range(1, n):
        lcm = math.lcm(i, lcm)
    return lcm


if __name__=="__main__":
    print(lcm(20))