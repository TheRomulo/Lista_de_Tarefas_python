"""
*************************************************************
Lista de Tarefas
Projeto final DiversificaDev

by Romulo

*************************************************************
"""


def adicionar_tarefa(lista_de_tarefas, tarefa): # Função para adicionar uma nova tarefa a lista
    tarefa = input("Insira uma nova tarefa: ")
    if tarefa == "":
         print("Tarefa vazia, favor inserir uma tarefa válida")
    else:
        lista_de_tarefas.append(tarefa)
        print(" ")
        print("Tarefa adicionada com sucesso!")
        print(" ")
        return lista_de_tarefas

def listar_tarefas(lista_de_tarefas): # Função que lista todas as tarefas cadastradas
        print("*" * 50)
        print(f"{' '*15}Lista de Tarefas") #Título da lista
        print("-"*50)
        n = 1
        if not lista_de_tarefas: #If caso a lista esteja vazia
            print(f"{' '*15}Lista Vazia")
        else:
            for tarefa in lista_de_tarefas:
                print(f"{n} - {tarefa}")
                n += 1
        print("-"*50)

def deletar_tarefa(lista_de_tarefas, tarefa): # Função para que uma tarefa seja deletada
     tarefa = input("Insira o número da tarefa que deseja deletar: ")
     if not tarefa.isnumeric(): # If para caso o usuário não digite um número
          print("*" * 50)
          print("Número inválido! Tente Novamente.")
          print("*" * 50)
     elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0: # Elif para caso o número digitado não esteja dentre as tarefas existentes
          print(" ")
          print("*" * 50)
          print("Número inválido! Tente Novamente.")
          print("*" * 50)
     else:     
        tarefa = int(tarefa)
        lista_de_tarefas.pop((tarefa - 1))
        return lista_de_tarefas

def exibir_menu(): # Exibe o menu com as opções da lista de tarefas
    print("-" * 50)
    print("Escolha uma opção:\n" \
    "1 - Inserir nova tarefa\n" \
    "2 - Listar tarefas\n" \
    "3 - Deletar tarefa\n" \
    "4 - Sair") 
    print("-" * 50)

# Váriaveis
lista_de_tarefas = list()
continuar = True
tarefa = ""


print("-" * 50)
print(f"{' '*6}Seja Bem vinde a sua lista de tarefas")
print("-" * 50)

lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)


# Loop da lista
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")


    if opcao == "1":
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)

    elif opcao == "3":
        deletar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "4":
        continuar = False
 
    else:
        print("-"*60)
        print("Opção Inválida! Pro favor, tente novamente")
        print("-"*60)
    print(" ")