class  Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def mostrar(self):
        print(self.nome, self.peso, self.altura)

pessoa1 = Pessoa('gabriel', 500, 164)

pessoa1.mostrar()