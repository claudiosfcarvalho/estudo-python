# avancado/geradores.py
# Exemplo de generator que retorna números pares

def pares_ate(n):
    """Gera números pares de 0 até n (inclusive)."""
    for i in range(0, n+1, 2):
        yield i

if __name__ == "__main__":
    for p in pares_ate(10):
        print("Par:", p)
