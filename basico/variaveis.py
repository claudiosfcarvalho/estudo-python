class Variaveis:
    def __init__(self, inteiro: int):
        self.inteiro = inteiro

    def variaveis(self, inteiro1):
        variavel = "valor variavel string"
        print("1º valor: " + str(self.inteiro))
        self.inteiro = "variavel também pode receber diferente de inteiro"
        print("2º valor: " + self.inteiro)


v = Variaveis(2)
v.variaveis(2)

nome = "Alice"  # string
idade = 28  # int
altura = 1.68  # float
esta_ativo = True  # bool

print(f"Nome: {nome}")
print("Idade:", idade)
print("Altura:", altura)
print("Usuário ativo?", esta_ativo)