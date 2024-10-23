import random

print("-----------------------------------------------------")
print('Outlet dos Pets')
print("-----------------------------------------------------")

filaRoupasFemeas = ["Roupas Fêmeas 1", "Roupas Fêmeas 2", "Roupas Fêmeas 3", "Roupas Fêmeas 4", "Roupas Fêmeas 5"]
filaRoupasMachos = ["Roupas Macho 1", "Roupas Macho 2", "Roupas Macho 3", "Roupas Macho 4", "Roupas Macho 5"]


Dono = []


def processaPedidoFemea():
    pet = input("Digite o nome do Pet (Fêmea): ")
    quantidade_roupas = random.randint(1, 10)  
    Dono.append(f'O pet {pet} recebeu {quantidade_roupas} roupas do outlet.')
    print(f'O pet {pet} recebeu {quantidade_roupas} roupas.')
    
    
    if random.choice([True, False]):
        notificaDono(pet, quantidade_roupas)


def processaPedidoMacho():
    pet = input("Digite o nome do Pet (Macho): ")
    quantidade_roupas = random.randint(1, 10)
    Dono.append(f'O pet {pet} recebeu {quantidade_roupas} roupas do outlet.')
    print(f'O pet {pet} recebeu {quantidade_roupas} roupas.')
    
    
    if random.choice([True, False]):
        notificaDono(pet, quantidade_roupas)


def notificaDono(pet, quantidade_roupas):
    print(f'Notificação: O dono do pet {pet} foi notificado de que ele(a) recebeu {quantidade_roupas} roupas!')


def filaHandler(valorPedido):
    if valorPedido > 0:
        print("----------------------------------------------------")
        print("Lista de Pets e Roupas Sorteadas:")
        for item in Dono:
            print(item)
    else:
        print('Nenhum Dono de Pet sorteado.')


def disparaPedido():
    i = 0
    while i < 5: 
        print("Escolha o tipo de roupa (1 para Fêmea, 2 para Macho) e sair com (sair):")
        tipo_roupa = input()
        if tipo_roupa == '1':
            processaPedidoFemea()
        elif tipo_roupa == '2':
            processaPedidoMacho()
        elif tipo_roupa == 'sair':
            break
        else:
            print("Opção inválida. Tente novamente.")
        i += 1
    filaHandler(i)


disparaPedido()