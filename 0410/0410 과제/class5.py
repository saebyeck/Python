def getGCD(a, b):
    gcd = 1 
    i = 2   

    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd = i 
        i = i + 1

    return gcd 

x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))

print(getGCD(x, y))