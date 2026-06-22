from conexao_mongo import conectar

db = conectar()
colecao = db["vinculos"]


def listar_vinculos():
    for v in colecao.find():
        print(v)


def inserir_vinculo():
    idvinculo = int(input("ID do vínculo: "))
    mat = input("Matrícula do estudante: ")
    idcurso = int(input("ID do curso: "))

    estudante = db["estudantes"].find_one({"_id": mat})
    if estudante is None:
        print("Erro: estudante não existe.")
        return

    curso = db["cursos"].find_one({"_id": idcurso})
    if curso is None:
        print("Erro: curso não existe.")
        return

    vinculo_id_existente = colecao.find_one({"_id": idvinculo})
    if vinculo_id_existente is not None:
        print("Erro: já existe um vínculo com esse ID.")
        return

    vinculo_repetido = colecao.find_one({
        "mat_estudante": mat,
        "curso": idcurso
    })

    if vinculo_repetido is not None:
        print("Erro: este estudante já possui vínculo com esse curso.")
        return

    print("\nStatus:")
    print("1 - Ativo")
    print("2 - Cancelada")
    print("3 - Formando")
    print("4 - Graduado")

    status_map = {
        "1": "Ativo",
        "2": "Cancelada",
        "3": "Formando",
        "4": "Graduado"
    }

    opcao = input("Escolha: ")
    status = status_map.get(opcao)

    if status is None:
        print("Status inválido.")
        return

    data_entrada = input("Data entrada (YYYY-MM-DD): ")
    data_saida = input("Data saída (YYYY-MM-DD ou vazio): ")

    if data_saida == "":
        data_saida = None

    vinculo = {
        "_id": idvinculo,
        "mat_estudante": mat,
        "curso": idcurso,
        "data_entrada": data_entrada,
        "status": status,
        "data_saida": data_saida
    }

    colecao.insert_one(vinculo)
    print("Vínculo inserido!")


def atualizar_vinculo():
    idvinculo = int(input("ID do vínculo: "))

    vinculo_atual = colecao.find_one({"_id": idvinculo})

    if vinculo_atual is None:
        print("Erro: vínculo não existe.")
        return

    mat = input("Nova matrícula do estudante: ")
    idcurso = int(input("Novo ID do curso: "))

    estudante = db["estudantes"].find_one({"_id": mat})
    if estudante is None:
        print("Erro: estudante não existe.")
        return

    curso = db["cursos"].find_one({"_id": idcurso})
    if curso is None:
        print("Erro: curso não existe.")
        return

    vinculo_repetido = colecao.find_one({
        "mat_estudante": mat,
        "curso": idcurso,
        "_id": {"$ne": idvinculo}
    })

    if vinculo_repetido is not None:
        print("Erro: já existe outro vínculo desse estudante com esse curso.")
        return

    print("\nStatus:")
    print("1 - Ativo")
    print("2 - Cancelada")
    print("3 - Formando")
    print("4 - Graduado")

    status_map = {
        "1": "Ativo",
        "2": "Cancelada",
        "3": "Formando",
        "4": "Graduado"
    }

    opcao = input("Escolha: ")
    status = status_map.get(opcao)

    if status is None:
        print("Status inválido.")
        return

    data_entrada = input("Nova data entrada (YYYY-MM-DD): ")
    data_saida = input("Nova data saída (YYYY-MM-DD ou vazio): ")

    if data_saida == "":
        data_saida = None

    novos_dados = {
        "mat_estudante": mat,
        "curso": idcurso,
        "data_entrada": data_entrada,
        "status": status,
        "data_saida": data_saida
    }

    resultado = colecao.update_one(
        {"_id": idvinculo},
        {"$set": novos_dados}
    )

    print(
        "Vínculo atualizado!"
        if resultado.modified_count > 0
        else "Nenhuma alteração feita."
    )


def excluir_vinculo():
    idvinculo = int(input("ID do vínculo: "))

    resultado = colecao.delete_one({"_id": idvinculo})

    print("Vínculo excluído!" if resultado.deleted_count > 0 else "Vínculo não encontrado.")