'''
Crie uma função para receber do usuário uma das seguintes opções F para feminino, M para masculino e O para outro. O programa deverar verificar se o usuário informou uma das opções validas e se não foi o programa deverar continuar pedindo ate uma opção validada ser informada
'''

def separador():
    print("-"*45)


def valida_genero():
    while True:
        genero = str(input("Gênero: ")).strip().upper()

        if genero in "MFO":
            break

        separador()
        print("A opção informada é invalida. Tente de novo.")

    if genero == "M":
        return "Masculino"
    elif genero == "F":
        return "Feminino"
    else:
        return "Outro"
    

print("Qual seu gênero?\nOpções:\nM - Masculino\nF - Feminino\nO - Outro\n")
genero = valida_genero()
separador()
print(f"A opção informada foi: {genero}")