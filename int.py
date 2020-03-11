n = int(input("digite um numero\n"))
s = 0
den: int = 1
for x in range(1, n + 1):
    if x == n:
        print("{}/{}".format(x, den), end=' ')
        s += x / den
        den += 2
    else:
        print("{}/{} + ".format(x, den), end='')
        s += x/den
        den += 2

print("=", s)
