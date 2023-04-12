from collections import deque as dq
import random as rd


def exe1():

    filaCaixaEconomica = dq()

    for i in range(1, 6):
        filaCaixaEconomica.append(i)

    filaCaixaEconomica.popleft()
    filaCaixaEconomica.popleft()

    print(filaCaixaEconomica)
    
def exe2():

    filaLoterica = dq()

 
    for i in range(10):
        filaLoterica.append(rd.randint(1, 100))

 
    contaFila = len(filaLoterica)
    contadordeDesocupados = 0
    while contadordeDesocupados < contaFila:
        if filaLoterica[contadordeDesocupados] % 2 == 0:
            filaLoterica.remove(filaLoterica[contadordeDesocupados])
            contaFila -= 1
        else:
            contadordeDesocupados += 1

    print(filaLoterica)

def exe3():

    filaCaixaEconomica = dq()

    for zebra in range(1, 11):
        filaCaixaEconomica.append(zebra)

    print(filaCaixaEconomica[3])

def exe4():

    filaCaixaEconomica = dq()

    for i in range(10):
        filaCaixaEconomica.append(rd.randint(1, 100))

    fila_invertida = filaCaixaEconomica.copy()
    fila_invertida.rotate(180)

    print(fila_invertida)

def exe5():

    filaCaixaEconomica = dq()

    for i in range(40):
        filaCaixaEconomica.append(rd.randint(1, 100))

    print(f"Fila antes da remoção: {filaCaixaEconomica}")

    maximuss = max(filaCaixaEconomica)
    filaCaixaEconomica.remove(maximuss)

    print(f"Fila após a remoção: {filaCaixaEconomica}")

def exe6():

    filaCaixaEconomica = dq()

    for i in range(40):
        filaCaixaEconomica.append(rd.randint(1, 100))

    print(f"Fila antes da remoção: {filaCaixaEconomica}")

    minimus = min(filaCaixaEconomica)
    theMinimusIndex = filaCaixaEconomica.index(minimus)
    newInput = 200
    filaCaixaEconomica[theMinimusIndex] = newInput

    print(f"Fila após a remoção e substituição: {filaCaixaEconomica}")

def exe7():

    filaCaixaEconomica = dq()

    for i in range(40):
        filaCaixaEconomica.append(rd.randint(1, 100))
    print(f"Fila antes da ordenação: {filaCaixaEconomica}")

    print(f"Fila após a ordenação: {sorted(filaCaixaEconomica)}")

def menu():

    opcoes = {
        "1": exe1,
        "2": exe2,
        "3": exe3,
        "4": exe4,
        "5": exe5,
        "6": exe6,
        "7": exe7
    }

    while True:
        print("Escolha o exercício Professor:")
        print("1 - Executar exercício 1")
        print("2 - Executar exercício 2")
        print("3 - Executar exercício 3")
        print("4 - Executar exercício 4")
        print("5 - Executar exercício 5")
        print("6 - Executar exercício 6")
        print("7 - Executar exercício 7")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao in opcoes:
            opcoes[opcao]()
        elif opcao == "0":
            print('Até mais...')
            break
        else:
            print("Opção inválida")

menu()