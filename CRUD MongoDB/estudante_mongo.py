from conexao_mongo import conectar

db = conectar()
colecao = db["estudantes"]

def listar_estudantes():
    for e in colecao.find():
        print(e)

def inserir_estudante():
    db = conectar()

    mat = input("Matrícula: ")
    cpf = int(input("CPF do usuário: "))

    usuario = db["usuarios"].find_one({"_id": cpf})

    if usuario is None:
        print("Erro: usuário não existe.")
        return

    estudante = {
        "_id": mat,
        "cpf": cpf,
        "mc": float(input("MC: ")),
        "ano_ingresso": int(input("Ano de ingresso: "))
    }

    colecao.insert_one(estudante)
    print("Estudante inserido!")

def atualizar_estudante():

    mat = input("Matrícula do estudante: ")

    estudante = colecao.find_one({"_id": mat})

    if estudante is None:
        print("Erro: estudante não existe.")
        return

    novo_mc = float(input("Novo MC: "))

    resultado = colecao.update_one(
        {"_id": mat},
        {"$set": {"mc": novo_mc}}
    )

    print("Estudante atualizado!" if resultado.modified_count > 0 else "Nenhuma alteração feita.")

def excluir_estudante():
    mat = input("Matrícula do estudante: ")

    resultado = colecao.delete_one({"_id": mat})

    print("Estudante excluído!" if resultado.deleted_count > 0 else "Estudante não encontrado.")