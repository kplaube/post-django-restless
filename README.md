# post-django-restless

Um exemplo de como utilizar o Django com a biblioteca Restless.

Para instalar todas as dependências, utilize a task `setup` do `Makefile`:

```
$ make setup
```

Para rodar:

```
$ make run
```

Para testar os endpoints utilize o `curl`:

```
$ curl -X GET http://localhost:8000/movies/
$ curl -X GET http://localhost:8000/movies/7e383f9c-5dc4-4b0d-9864-71e05a5d271b/
$ curl -X POST -H "Content-Type: application/json" -d '{"title": "just a test", "description": "foo bar"}'
$ curl -X PUT -H "Content-Type: application/json" -d '{"title": "Zombieland", "description": "So much fun"}'
$ curl -X DELETE http://localhost:8000/movies/bd02d0eb-4b75-4bfe-8222-ba24f7a1cad4/
```
