# condicionais.py
# Exemplo de estruturas condicionais

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")

# Operador ternário
par_ou_impar = "par" if numero % 2 == 0 else "ímpar"
print(f"O número é {par_ou_impar}.")
