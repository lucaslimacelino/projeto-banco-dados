from conexao import conectar


def listar_cursos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT idcurso, nome, grau, turno, campus, nivel
        FROM universidade.curso
        ORDER BY idcurso
    """)

    cursos = cur.fetchall()

    if not cursos:
        print("\nNenhum curso cadastrado.")
    else:
        print("\n===== CURSOS =====")
        for curso in cursos:
            print(curso)

    cur.close()
    conn.close()


def inserir_curso():
    nome = input("Nome do curso: ")

    print("\nGrau:")
    print("1 - Bacharelado")
    print("2 - Licenciatura Plena")
    opcao = input("Escolha: ")

    if opcao == "1":
        grau = "Bacharelado"
    elif opcao == "2":
        grau = "Licenciatura Plena"
    else:
        print("Opção inválida!")
        return

    print("\nTurno:")
    print("1 - Matutino")
    print("2 - Vespertino")
    print("3 - Noturno")
    print("4 - Turno Indefinido")

    opcao = input("Escolha: ")

    turnos = {
        "1": "Matutino",
        "2": "Vespertino",
        "3": "Noturno",
        "4": "Turno Indefinido"
    }

    turno = turnos.get(opcao)

    if not turno:
        print("Opção inválida!")
        return

    campus = input("Campus: ")

    print("\nNível:")
    print("1 - Graduação")
    print("2 - Mestrado")
    print("3 - Doutorado")
    print("4 - Lato")

    opcao = input("Escolha: ")

    niveis = {
        "1": "Graduação",
        "2": "Mestrado",
        "3": "Doutorado",
        "4": "Lato"
    }

    nivel = niveis.get(opcao)

    if not nivel:
        print("Opção inválida!")
        return

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO universidade.curso
        (nome, grau, turno, campus, nivel)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, grau, turno, campus, nivel))

    conn.commit()

    print("\nCurso cadastrado com sucesso!")

    cur.close()
    conn.close()


def atualizar_curso():
    listar_cursos()

    idcurso = input("\nID do curso a atualizar: ")

    nome = input("Novo nome: ")

    print("\nGrau:")
    print("1 - Bacharelado")
    print("2 - Licenciatura Plena")

    opcao = input("Escolha: ")

    graus = {
        "1": "Bacharelado",
        "2": "Licenciatura Plena"
    }

    grau = graus.get(opcao)

    print("\nTurno:")
    print("1 - Matutino")
    print("2 - Vespertino")
    print("3 - Noturno")
    print("4 - Turno Indefinido")

    opcao = input("Escolha: ")

    turnos = {
        "1": "Matutino",
        "2": "Vespertino",
        "3": "Noturno",
        "4": "Turno Indefinido"
    }

    turno = turnos.get(opcao)

    campus = input("Novo campus: ")

    print("\nNível:")
    print("1 - Graduação")
    print("2 - Mestrado")
    print("3 - Doutorado")
    print("4 - Lato")

    opcao = input("Escolha: ")

    niveis = {
        "1": "Graduação",
        "2": "Mestrado",
        "3": "Doutorado",
        "4": "Lato"
    }

    nivel = niveis.get(opcao)

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE universidade.curso
        SET nome = %s,
            grau = %s,
            turno = %s,
            campus = %s,
            nivel = %s
        WHERE idcurso = %s
    """, (nome, grau, turno, campus, nivel, idcurso))

    conn.commit()

    if cur.rowcount > 0:
        print("\nCurso atualizado com sucesso!")
    else:
        print("\nCurso não encontrado!")

    cur.close()
    conn.close()


def excluir_curso():
    listar_cursos()

    idcurso = input("\nID do curso a excluir: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM universidade.curso
        WHERE idcurso = %s
    """, (idcurso,))

    conn.commit()

    if cur.rowcount > 0:
        print("\nCurso excluído!")
    else:
        print("\nCurso não encontrado!")

    cur.close()
    conn.close()