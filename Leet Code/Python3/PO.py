""" simply we convert the given list into integer add 1 to the number and then convert the number back to list and return the list"""
def plusOne(digits):
    nums = 0
    for i in digits:
        nums = (nums*10) + i
    nums += 1
    digits.clear()
    while nums != 0:
        digits.insert(0, nums %10)
        nums = nums//10
    return digits


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        li = []
        for i in range(n):
            li.append(int(input()))
        
        li = plusOne(li)
        print(li)


