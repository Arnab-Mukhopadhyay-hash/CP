def addBinary(a, b)->str:
    a_dec = int(a, 2)
    b_dec = int(b, 2)
    sum = a_dec + b_dec
    return bin(sum)


if __name__ == "__main__":
    a = input()
    b = input()
    res = addBinary(a, b)
    print(res)