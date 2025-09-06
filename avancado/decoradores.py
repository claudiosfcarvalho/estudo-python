# avancado/decoradores.py
# Exemplo de decorator para medir tempo de execução

import time
from functools import wraps

def tempo_exec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"[{func.__name__}] tempo: {fim - inicio:.4f}s")
        return resultado
    return wrapper

@tempo_exec
def contar_ate(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    print("Soma:", contar_ate(1_000_000))
