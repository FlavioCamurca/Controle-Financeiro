# Controle Financeiro

from datetime import datetime

opcoes_menu = [
    "1 - Listar Relatório",
    "2 - Adicionar lançamento",
    "3 - Atualização",
    "4 - Excluir lançamento",
    "5 - Gerar relatório mensal",
    "6 - Encerrar",
]

def iniciar_menu():
    while True:
        print("\n- MENU PRINCIPAL -\n")

        for opcao in opcoes_menu:
            print(opcao)
        
        opcao_escolhida = input("\nDigite uma opção: ")
        
        match opcao_escolhida:
            case '1':
                print("\n ** LISTAR RELATÓRIO ** \n")
                #...                #...
            case '2':
                print("\n ** ADICIONAR LANÇAMENTO ** \n")
                #...
            case '3':
                print("\n ** ATUALIZAÇÃO ** \n")
                #...
            case '4':
                print("\n ** EXCLUIR LANÇAMENTO ** \n")
                #...
            case '5':
                print("\n ** GERAR RELATÓRIO MENSAL ** \n")
                #...
            case '6':
                print("\n ** PROGRAMA FINALIZADO  ** \n")
                break
                #...
            case _:
                print("\n OPCAO INVALIDA \n")

if __name__ == "__main__":
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()