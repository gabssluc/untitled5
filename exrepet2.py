a = str(input("digite seu nome\n")).upper()
pas = str(input("digite sua senha\n")).upper()
while a == pas:
    pas = str(input("ERRO! Sua senha não deve ser igual ao seu nome, digite outra seenha: \n")).upper()
print("conta realizada")
