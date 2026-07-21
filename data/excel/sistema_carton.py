import subprocess
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    limpar_tela()

    print("=" * 40)
    print("      SISTEMA CARTON")
    print("=" * 40)
    print("1 - Consultar OF")
    print("2 - Indicador por Data")
    print("0 - Sair")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        subprocess.run(["python3", "consulta_of.py"])
        input("\nPressione ENTER para voltar...")

    elif opcao == "2":
        limpar_tela()
        subprocess.run(["python3", "data/excel/indicador_data.py"])
        input("\nPressione ENTER para voltar...")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("\nOpção inválida!")
        input("Pressione ENTER...")