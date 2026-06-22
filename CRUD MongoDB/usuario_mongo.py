from conexao_mongo import conectar

db = conectar()
colecao = db["usuarios"]

def listar_usuarios():
    for u in colecao.find():
        print(u)

def inserir_usuario():
    usuario = {
        "_id": int(input("CPF: ")),
        "nome": input("Nome: "),
        "data_nascimento": input("Data nascimento (YYYY-MM-DD): "),
        "email": [input("Email: ")],
        "telefone": [input("Telefone: ")],
        "login": input("Login: "),
        "senha": input("Senha: ")
    }

    colecao.insert_one(usuario)
    print("Usuário inserido!")

def atualizar_usuario():
    cpf = int(input("CPF do usuário: "))

    novos_dados = {
        "nome": input("Novo nome: "),
        "data_nascimento": input("Nova data nascimento (YYYY-MM-DD): "),
        "email": [input("Novo email: ")],
        "telefone": [input("Novo telefone: ")],
        "login": input("Novo login: "),
        "senha": input("Nova senha: ")
    }

    resultado = colecao.update_one(
        {"_id": cpf},
        {"$set": novos_dados}
    )

    print("Usuário atualizado!" if resultado.modified_count > 0 else "Usuário não encontrado.")
def excluir_usuario():
    cpf = int(input("CPF do usuário: "))

    resultado = colecao.delete_one({"_id": cpf})

    print("Usuário excluído!" if resultado.deleted_count > 0 else "Usuário não encontrado.")