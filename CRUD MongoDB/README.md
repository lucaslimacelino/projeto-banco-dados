# CRUD MongoDB - Projeto Banco de Dados

## Descrição

Este projeto consiste na implementação da Parte 2 do trabalho da disciplina de Banco de Dados, utilizando MongoDB hospedado na AWS EC2 e Python com a biblioteca pymongo.

O modelo relacional foi mapeado para o MongoDB, onde:

* tabelas foram representadas como collections;
* registros foram representados como documentos JSON;
* chaves primárias foram representadas pelo campo `_id`;
* chaves estrangeiras foram tratadas manualmente no código da aplicação.

## Collections Representadas

* usuarios
* estudantes
* cursos
* vinculos
* professores
* departamentos
* projetos
* planos
* disciplinas
* salas
* horarios
* turmas
* semestres
* leciona
* alocacoes
* cursas

## Restrições Implementadas

### Restrição de chave

As chaves primárias foram garantidas pelo campo `_id` do MongoDB e por índices únicos.

### Integridade referencial

Como o MongoDB não implementa chaves estrangeiras automaticamente, as verificações foram realizadas no código Python antes das inserções e atualizações.

Exemplos:

* verificação se usuário existe antes de inserir estudante;
* verificação se estudante e curso existem antes de inserir vínculo.

### Restrição de domínio

Os campos `grau`, `turno`, `nivel` e `status` utilizam menus fixos no sistema, evitando valores inválidos.

### Restrição NOT NULL

Os principais campos obrigatórios são solicitados durante as operações do CRUD.

## Operações CRUD

O sistema implementa:

* insert_one()
* find()
* update_one()
* delete_one()

para as collections:

* usuarios
* estudantes
* cursos
* vinculos

## Tecnologias Utilizadas

* Python
* MongoDB
* MongoDB Compass
* AWS EC2
* pymongo

* ## Demonstração das Operações CRUD

### CREATE (Inserção)

Exemplo de inserção de usuário:

```python
colecao.insert_one(usuario)
```

Efeito no MongoDB Compass:

Um novo documento é criado na collection `usuarios`.

Exemplo:

```json
{
  "_id": 99999999999,
  "nome": "Lucas",
  "login": "lucas"
}
```

---

### READ (Leitura)

Exemplo:

```python
colecao.find()
```

Efeito no MongoDB Compass:

Os documentos armazenados na collection são exibidos no sistema e podem ser visualizados no Compass.

---

### UPDATE (Atualização)

Exemplo:

```python
colecao.update_one(
    {"_id": 1},
    {"$set": {"nome": "Novo Nome"}}
)
```

Efeito no MongoDB Compass:

O documento correspondente é atualizado automaticamente na collection.

---

### DELETE (Remoção)

Exemplo:

```python
colecao.delete_one({"_id": 1})
```

Efeito no MongoDB Compass:

O documento é removido da collection e deixa de aparecer no banco de dados.

