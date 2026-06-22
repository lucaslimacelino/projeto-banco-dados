# CRUD Relacional - PostgreSQL

## Descrição

Este projeto consiste na implementação da Parte 1 do trabalho da disciplina de Banco de Dados, utilizando PostgreSQL hospedado na AWS RDS e Python com a biblioteca psycopg2.

O sistema implementa operações CRUD para as estruturas:

* usuarios
* estudantes
* cursos
* vinculos

seguindo o modelo relacional desenvolvido na disciplina.

## Tecnologias Utilizadas

* Python
* PostgreSQL
* AWS RDS
* pgAdmin4
* psycopg2

## Estruturas Utilizadas

As tabelas principais manipuladas pelo sistema são:

* usuario
* estudante
* curso
* vinculo

Além disso, o banco contém as demais estruturas do esquema relacional:

* professor
* departamento
* projeto
* plano
* disciplina
* sala
* horario
* turma
* semestre
* leciona
* alocacao
* cursa

## Restrições Implementadas

### Chaves Primárias

As tabelas utilizam chaves primárias definidas no PostgreSQL.

Exemplos:

* usuario.cpf
* estudante.mat_estudante
* curso.idcurso
* vinculo.idvinculo

### Integridade Referencial

As relações entre tabelas foram garantidas por chaves estrangeiras.

Exemplos:

* estudante.cpf referencia usuario.cpf
* vinculo.mat_estudante referencia estudante.mat_estudante
* vinculo.curso referencia curso.idcurso

### Restrições de Domínio

O banco utiliza tipos ENUM para restringir valores válidos.

Exemplos:

* tipo_turno
* tipo_grau
* tipo_nivel
* status_estudante

### NOT NULL

Campos obrigatórios foram definidos utilizando restrições NOT NULL no PostgreSQL.

## Operações CRUD

O sistema implementa:

* INSERT
* SELECT
* UPDATE
* DELETE

para as tabelas:

* usuario
* estudante
* curso
* vinculo

## Demonstração das Operações CRUD

### CREATE (Inserção)

Exemplo:

```sql id="1n6yvt"
INSERT INTO universidade.usuario (...)
```

Efeito:

Um novo registro é inserido na tabela correspondente e pode ser visualizado no pgAdmin4.

---

### READ (Leitura)

Exemplo:

```sql id="e8lq4z"
SELECT * FROM universidade.usuario
```

Efeito:

Os registros armazenados são exibidos no sistema e no pgAdmin4.

---

### UPDATE (Atualização)

Exemplo:

```sql id="q7kv7u"
UPDATE universidade.curso
SET nome = 'Novo Nome'
```

Efeito:

O registro correspondente é atualizado no banco PostgreSQL.

---

### DELETE (Remoção)

Exemplo:

```sql id="aq11fu"
DELETE FROM universidade.usuario
```

Efeito:

O registro é removido da tabela correspondente.
