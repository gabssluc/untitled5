n = int (input(" \n"))
s = 0
for x in range(1, n+1):
    if x == n:
        print("{}/{} = ".format(1, x), end=' ')
        s += 1/x
    else:
        print("{}/{} + ".format(1, x), end=' ')
        s += 1/x

print(s)