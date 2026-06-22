from conexao import conectar

def listar_usuarios():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT cpf, nome, data_nascimento, email, telefone, login, senha
        FROM universidade.usuario
        ORDER BY nome
    """)

    for u in cur.fetchall():
        print(u)

    cur.close()
    conn.close()


def inserir_usuario():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    data_nascimento = input("Data nascimento (YYYY-MM-DD): ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    login = input("Login: ")
    senha = input("Senha: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO universidade.usuario
        (cpf, nome, data_nascimento, email, telefone, login, senha)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        cpf,
        nome,
        data_nascimento,
        [email],
        [telefone],
        login,
        senha
    ))

    conn.commit()
    print("Usuário inserido com sucesso!")

    cur.close()
    conn.close()


def atualizar_usuario():
    cpf = input("CPF do usuário: ")
    nome = input("Novo nome: ")
    login = input("Novo login: ")
    senha = input("Nova senha: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE universidade.usuario
        SET nome = %s,
            login = %s,
            senha = %s
        WHERE cpf = %s
    """, (nome, login, senha, cpf))

    conn.commit()

    if cur.rowcount > 0:
        print("Usuário atualizado!")
    else:
        print("Usuário não encontrado!")

    cur.close()
    conn.close()


def excluir_usuario():
    cpf = input("CPF do usuário: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM universidade.usuario
        WHERE cpf = %s
    """, (cpf,))

    conn.commit()

    if cur.rowcount > 0:
        print("Usuário excluído!")
    else:
        print("Usuário não encontrado!")

    cur.close()
    conn.close()