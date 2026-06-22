from curso_mongo import *
from usuario_mongo import *
from estudante_mongo import *
from vinculo_mongo import *

def menu_crud(nome, listar, inserir, atualizar, excluir):
    while True:
        print(f"\n===== {nome.upper()} =====")
        print("1 - Listar")
        print("2 - Inserir")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            listar()
        elif op == "2":
            inserir()
        elif op == "3":
            atualizar()
        elif op == "4":
            excluir()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

while True:
    print("\n==============================")
    print("   SISTEMA UNIVERSIDADE - MONGODB")
    print("==============================")
    print("1 - Gerenciar Cursos")
    print("2 - Gerenciar Usuários")
    print("3 - Gerenciar Estudantes")
    print("4 - Gerenciar Vínculos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        menu_crud("Cursos", listar_cursos, inserir_curso, atualizar_curso, excluir_curso)
    elif opcao == "2":
        menu_crud("Usuários", listar_usuarios, inserir_usuario, atualizar_usuario, excluir_usuario)
    elif opcao == "3":
        menu_crud("Estudantes", listar_estudantes, inserir_estudante, atualizar_estudante, excluir_estudante)
    elif opcao == "4":
        menu_crud("Vínculos", listar_vinculos, inserir_vinculo, atualizar_vinculo, excluir_vinculo)
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")