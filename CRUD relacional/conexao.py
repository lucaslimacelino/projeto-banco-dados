import psycopg2

def conectar():
    return psycopg2.connect(
        host="database-1.ccaudxd34hv8.us-east-1.rds.amazonaws.com",
        database="postgres",
        user="professor",
        password="professor",
        port=5432
    )