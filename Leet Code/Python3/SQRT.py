import math
def mySqrt(x)->int:
    return int(math.sqrt(x))

if __name__ == "__main__":
    x = int(input())
    ans = mySqrt(x)
    print(ans)