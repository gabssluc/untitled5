class pizza(object):
    def __init__(self, cobertura):
        self.cobertura = cobertura
    @property
    def pega_cobertura(self):
        return self.cobertura
    @pega_cobertura.setter
    def pega_cobertura(self, valor):
        self.cobertura = ingtvalor



a = pizza("calabreza")
print(a.pega_cobertura)
a.pega_cobertura = True
print(a.pega_cobertura)