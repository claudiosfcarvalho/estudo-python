# avancado/poo.py
# Exemplo básico de Programação Orientada a Objetos

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        self._saldo += valor

    def sacar(self, valor: float):
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor

if __name__ == "__main__":
    conta = ContaBancaria("Carlos", 100.0)
    conta.depositar(50)
    conta.sacar(30)
    print(f"Titular: {conta.titular}, Saldo: {conta.saldo}")
    try:
        conta.sacar(1000)
    except Exception as e:
        print(e)

    try:
        conta.depositar(-100)
    except Exception as e:
        print(e)