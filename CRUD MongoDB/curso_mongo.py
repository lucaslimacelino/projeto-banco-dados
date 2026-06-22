from conexao_mongo import conectar

db = conectar()
colecao = db["cursos"]

def listar_cursos():
    for c in colecao.find():
        print(c)

def escolher_opcao(titulo, opcoes):
    print(f"\n{titulo}:")
    for chave, valor in opcoes.items():
        print(f"{chave} - {valor}")

    escolha = input("Escolha: ")
    valor = opcoes.get(escolha)

    if valor is None:
        print("Opção inválida!")
        return None

    return valor


def inserir_curso():
    nome = input("Nome: ")

    graus = {
        "1": "Bacharelado",
        "2": "Licenciatura Plena"
    }

    turnos = {
        "1": "Matutino",
        "2": "Vespertino",
        "3": "Noturno",
        "4": "Turno Indefinido"
    }

    niveis = {
        "1": "Graduação",
        "2": "Mestrado",
        "3": "Doutorado",
        "4": "Lato"
    }

    grau = escolher_opcao("Grau", graus)
    if grau is None:
        return

    turno = escolher_opcao("Turno", turnos)
    if turno is None:
        return

    campus = input("Campus: ")

    nivel = escolher_opcao("Nível", niveis)
    if nivel is None:
        return

    curso = {
        "_id": int(input("ID do curso: ")),
        "nome": nome,
        "grau": grau,
        "turno": turno,
        "campus": campus,
        "nivel": nivel
    }

    colecao.insert_one(curso)
    print("Curso inserido!")

def escolher_opcao(titulo, opcoes):

    print(f"\n{titulo}:")

    for chave, valor in opcoes.items():
        print(f"{chave} - {valor}")

    escolha = input("Escolha: ")

    valor = opcoes.get(escolha)

    if valor is None:
        print("Opção inválida!")
        return None

    return valor


def atualizar_curso():

    idcurso = int(input("ID do curso: "))

    curso = colecao.find_one({"_id": idcurso})

    if curso is None:
        print("Curso não encontrado.")
        return

    nome = input("Novo nome: ")

    graus = {
        "1": "Bacharelado",
        "2": "Licenciatura Plena"
    }

    turnos = {
        "1": "Matutino",
        "2": "Vespertino",
        "3": "Noturno",
        "4": "Turno Indefinido"
    }

    niveis = {
        "1": "Graduação",
        "2": "Mestrado",
        "3": "Doutorado",
        "4": "Lato"
    }

    grau = escolher_opcao("Grau", graus)

    if grau is None:
        return

    turno = escolher_opcao("Turno", turnos)

    if turno is None:
        return

    campus = input("Novo campus: ")

    nivel = escolher_opcao("Nível", niveis)

    if nivel is None:
        return

    novos_dados = {
        "nome": nome,
        "grau": grau,
        "turno": turno,
        "campus": campus,
        "nivel": nivel
    }

    resultado = colecao.update_one(
        {"_id": idcurso},
        {"$set": novos_dados}
    )

    print(
        "Curso atualizado!"
        if resultado.modified_count > 0
        else "Nenhuma alteração feita."
    )

def excluir_curso():
    idcurso = int(input("ID do curso: "))

    resultado = colecao.delete_one({"_id": idcurso})

    print("Curso excluído!" if resultado.deleted_count > 0 else "Curso não encontrado.")