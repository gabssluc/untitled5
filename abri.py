import json


dic = {"dic": "3424"}
a = json.dumps(dic)
b = a.encode()
arq = open("texto.json", "w")
print(arq.writelines(a))

arq.close()