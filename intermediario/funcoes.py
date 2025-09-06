# intermediario/funcoes.py
# Exemplos de definição e uso de funções

def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"

def soma(a: int, b: int) -> int:
    """Retorna a soma de dois números."""
    return a + b

if __name__ == "__main__":
    print(saudacao("João"))
    print("2 + 3 =", soma(2, 3))
