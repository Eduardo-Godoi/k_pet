# KenziePet

Kenzie pet é um sistema desenvolvido para PetShops, com intuito de guardar as informações dos animais atendidos.

## Como Instalar?

Para instalar, é necessário clonar o projeto e fazer instalação das dependências.

- ### Clonando o Projeto:

  git clone https://gitlab.com/<your_user>/kenzie_pet.git

- ### Entrar na pasta:

  cd kenzie_pet

- ### Entrar no ambiente virtual:
  source venv/bin/activate

* ### Instalando as Depenências:
  pip install -r requirements.txt

**Apos ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:**

- pythom manage.py migrate

**Para iniciar a aplicação insira o comando abixo em seu terminal**

- python manage.py runserver

## Rotas

**GET /api/animals/**

Rota responsavel por retornar todos animais cadastrados.

RESPONSE STATUS -> HTTP 200 (ok)

Response:

```json
[
  {
    "id": 1,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 2,
        "characteristic": "medio porte"
      }
    ]
  },
  {
    "id": 2,
    "name": "Hanna",
    "age": 1.0,
    "weight": 20.0,
    "sex": "femea",
    "group": {
      "id": 2,
      "name": "gato",
      "scientific_name": "felis catus"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 3,
        "characteristic": "felino"
      }
    ]
  }
]
```

**GET /api/animals/<<int:animal_id>>/**
Rota retorna as informações do animal com id igual ao passado na rota.

RESPONSE STATUS -> HTTP 200 (ok)

Response:

```json
{
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```

**POST /api/animals/**

Rota para a criação de informações de animais.

RESPONSE STATUS -> HTTP 201 (created)

Body:

```json
{
  "name": "Bidu",
  "age": 1,
  "weight": 30,
  "sex": "macho",
  "group": {
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "characteristic": "peludo"
    },
    {
      "characteristic": "medio porte"
    }
  ]
}
```

Response:

```json
{
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```

**DELETE /api/animals/<int:animal_id>/**

Rota par deletar informações de um animal.

Não há conteúdo no retorno da requisição.

RESPONSE STATUS -> HTTP 204 (no content)

## **Tecnologias Utilizadas**

- Django

* Django Rest Framework
* SQLite
