import os

restaurantes = ['Outback','Mangai']


def exibir_nome_app ():
    print('Sabor Express:\n')

def menu_app():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def exibir_mensagem(texto):
    os.system('cls')
    print(texto)
    print()

def escolher_opcao():
    try:
        opcao_escolher = int(input('Qual a sua escolha?'))

        if opcao_escolher == 1:
            print('Vamos Cadastrar!')
            cadastrar_restaurante()
        elif opcao_escolher == 2:
            print('Vamos Listar!')
            listar_restaurante()
        elif opcao_escolher == 3:
            print('Vamos Ativar!')
        elif opcao_escolher == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def voltar_menu(menu_escolhido):
    input('\nPressione enter para continuar')
    menu_escolhido()

def cadastrar_restaurante():
    restaurante_igual = False
    exibir_mensagem('Cadastro de novo restaurante: [Digite "Sair" para voltar ao menu"]')
    nome_restaurante = input('Qual o nome do restaurante que deseja cadastrar: ').strip(" ")
    if nome_restaurante != 'Sair':
        for i in range(0, len(restaurantes)):
            if restaurantes[i] == nome_restaurante:
                restaurante_igual = True
        if restaurante_igual == True:
            print('Restaurante já cadastrado!')
            voltar_menu(cadastrar_restaurante)
        else:
            restaurantes.append(nome_restaurante)
            print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
            voltar_menu(main)
    else:
        main()

def listar_restaurante():
    exibir_mensagem('Listando os restaurantes:')
    for lista in restaurantes:
        print(f'- {lista}')
    voltar_menu(main)

def finalizar_app():
    exibir_mensagem('Finalizando o app')

def opcao_invalida():
    print ('Opção inválida!')
    voltar_menu(main)

def main():
    os.system('cls')
    exibir_nome_app()
    menu_app()
    escolher_opcao()
  
if __name__  == '__main__':
    main()