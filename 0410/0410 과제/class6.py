def deci2bin(n):
    binary = ""

    while n != 0:
        value = n % 2
        if value == 0 :
            binary = "0" + binary 
        else:
            binary = "1" + binary
        n = n // 2
        
    return binary

x = int(input("10진수: "))
print(deci2bin(x))