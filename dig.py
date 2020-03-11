n = int(input("digite um numero"))
aux = n
reverso = 0
while aux > 0:
    dig = aux % 10
    aux = aux // 10
    reverso = 10*reverso + dig

print("o revedrso do numero é ", reverso)
if reverso == n:
    print("O numero é palindromo")

