# Projeto Banco de Dados - PostgreSQL e MongoDB

## Descrição

Projeto desenvolvido para a disciplina de Banco de Dados, contendo:

* Parte 1: implementação de CRUD relacional utilizando PostgreSQL;
* Parte 2: implementação de CRUD NoSQL utilizando MongoDB.

Os sistemas foram desenvolvidos em Python e hospedados na AWS.

---

# Estrutura do Projeto

```text id="rmyjxh"
projeto-banco-dados/
│
├── CRUD relacional/
│
├── CRUD MongoDB/
│
└── README.md
```

---

# Parte 1 - PostgreSQL

A Parte 1 utiliza PostgreSQL hospedado na AWS RDS.

O sistema implementa operações CRUD para:

* usuarios
* estudantes
* cursos
* vinculos

utilizando:

* psycopg2
* pgAdmin4
* PostgreSQL

---

# Parte 2 - MongoDB

A Parte 2 utiliza MongoDB hospedado na AWS EC2.

O modelo relacional foi mapeado para MongoDB, onde:

* tabelas foram representadas como collections;
* registros foram representados como documentos JSON;
* chaves primárias foram representadas pelo campo `_id`;
* integridade referencial foi garantida pela aplicação.

O sistema implementa CRUD para:

* usuarios
* estudantes
* cursos
* vinculos

utilizando:

* pymongo
* MongoDB Compass
* MongoDB

---

# Tecnologias Utilizadas

* Python
* PostgreSQL
* MongoDB
* AWS RDS
* AWS EC2
* pgAdmin4
* MongoDB Compass
* psycopg2
* pymongo

---

# Objetivo

O projeto teve como objetivo comparar os modelos:

* relacional;
* NoSQL orientado a documentos;

além de implementar operações CRUD e representar estruturas de banco de dados em diferentes SGBDs.
