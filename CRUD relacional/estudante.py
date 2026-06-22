from conexao import conectar

def listar_estudantes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT mat_estudante, cpf, mc, ano_ingresso
        FROM universidade.estudante
        ORDER BY mat_estudante
    """)

    for e in cur.fetchall():
        print(e)

    cur.close()
    conn.close()


def inserir_estudante():
    mat_estudante = input("Matrícula do estudante: ")
    cpf = input("CPF do usuário já cadastrado: ")
    mc = input("MC: ")
    ano_ingresso = input("Ano de ingresso: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO universidade.estudante
        (mat_estudante, cpf, mc, ano_ingresso)
        VALUES (%s, %s, %s, %s)
    """, (mat_estudante, cpf, mc, ano_ingresso))

    conn.commit()
    print("Estudante inserido com sucesso!")

    cur.close()
    conn.close()


def atualizar_estudante():
    mat_estudante = input("Matrícula do estudante: ")
    mc = input("Novo MC: ")
    ano_ingresso = input("Novo ano de ingresso: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE universidade.estudante
        SET mc = %s,
            ano_ingresso = %s
        WHERE mat_estudante = %s
    """, (mc, ano_ingresso, mat_estudante))

    conn.commit()

    if cur.rowcount > 0:
        print("Estudante atualizado!")
    else:
        print("Estudante não encontrado!")

    cur.close()
    conn.close()


def excluir_estudante():
    mat_estudante = input("Matrícula do estudante: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM universidade.estudante
        WHERE mat_estudante = %s
    """, (mat_estudante,))

    conn.commit()

    if cur.rowcount > 0:
        print("Estudante excluído!")
    else:
        print("Estudante não encontrado!")

    cur.close()
    conn.close()