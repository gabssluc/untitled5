def bub(lispc):
    for c in range(len(lispc)):
        for i in range(len(lispc)-1):
            if lispc[i + 1] < lispc[i]:
                v = lispc[i+1]
                b = lispc[i]
                lispc[i], lispc[i+1] = v, b

    return lispc


def cria_lista(num):
    li = []
    for k in range(num):
        f = int(input("digite um numero\n"))
        li.append(f)
    return li


a = cria_lista(5)
sorted_nums = bub(a)
for x in sorted_nums:
    print(x, end=' ')
