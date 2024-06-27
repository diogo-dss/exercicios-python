'''
Crie um programa que receba uma lista de números inteiros e implima a amplitude entre os números informados.
'''

def valida_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
            break

        except ValueError:
            print("\nERROR! O número informado é inválido, por favor informe um número inteiro. Tente de novo:")


numeros = []

print("Você deve informe pelo menos dois números inteiros.\n")

while True:
    quantidade_numeros = valida_numero("Quantos números serão informados?\nQuantidade de números: ")

    if (quantidade_numeros >= 2):
        break

    print("\nERROR! É necessário informar no mínimo 2 números. Tente de novo:")

for i in range(0, quantidade_numeros):
    numero = valida_numero(f"Digite o número {i+1}: ")
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)
amplitude = maior_numero - menor_numero

print("\nOs números informados foram: ", end="")
for numero in numeros:
    print(f"{numero} ", end="")

print(f"\nMaior número: {maior_numero}\nMenor número: {menor_numero}\nAmplitude: {amplitude}")