n = int(input())

def isUsual(num):
    if  num <=0:
        print("No")
    else:
        while num%2 ==0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        if num == 1:
            return False
    return True

if isUsual(n):
    print("No")
else:
    print("Yes")