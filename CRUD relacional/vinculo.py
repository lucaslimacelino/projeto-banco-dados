from conexao import conectar

def listar_vinculos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT idvinculo, mat_estudante, curso, data_entrada, status, data_saida
        FROM universidade.vinculo
        ORDER BY idvinculo
    """)

    for v in cur.fetchall():
        print(v)

    cur.close()
    conn.close()


def inserir_vinculo():
    mat_estudante = input("Matrícula do estudante: ")
    curso = input("ID do curso: ")
    data_entrada = input("Data de entrada (YYYY-MM-DD ou deixe vazio): ")

    print("\nStatus:")
    print("1 - Ativo")
    print("2 - Cancelada")
    print("3 - Formando")
    print("4 - Graduado")

    status_op = input("Escolha: ")

    status_map = {
        "1": "Ativo",
        "2": "Cancelada",
        "3": "Formando",
        "4": "Graduado"
    }

    status = status_map.get(status_op)

    if not status:
        print("Status inválido!")
        return

    data_saida = input("Data de saída (YYYY-MM-DD ou deixe vazio): ")

    if data_entrada == "":
        data_entrada = None

    if data_saida == "":
        data_saida = None

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO universidade.vinculo
        (mat_estudante, curso, data_entrada, status, data_saida)
        VALUES (%s, %s, %s, %s, %s)
    """, (mat_estudante, curso, data_entrada, status, data_saida))

    conn.commit()
    print("Vínculo inserido com sucesso!")

    cur.close()
    conn.close()


def atualizar_vinculo():
    idvinculo = input("ID do vínculo: ")

    print("\nStatus:")
    print("1 - Ativo")
    print("2 - Cancelada")
    print("3 - Formando")
    print("4 - Graduado")

    status_op = input("Escolha: ")

    status_map = {
        "1": "Ativo",
        "2": "Cancelada",
        "3": "Formando",
        "4": "Graduado"
    }

    status = status_map.get(status_op)

    if not status:
        print("Status inválido!")
        return

    data_saida = input("Data de saída (YYYY-MM-DD ou deixe vazio): ")

    if data_saida == "":
        data_saida = None

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE universidade.vinculo
        SET status = %s,
            data_saida = %s
        WHERE idvinculo = %s
    """, (status, data_saida, idvinculo))

    conn.commit()

    if cur.rowcount > 0:
        print("Vínculo atualizado!")
    else:
        print("Vínculo não encontrado!")

    cur.close()
    conn.close()


def excluir_vinculo():
    idvinculo = input("ID do vínculo: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM universidade.vinculo
        WHERE idvinculo = %s
    """, (idvinculo,))

    conn.commit()

    if cur.rowcount > 0:
        print("Vínculo excluído!")
    else:
        print("Vínculo não encontrado!")

    cur.close()
    conn.close()