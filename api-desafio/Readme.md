
# Especificações da API Rest
Endpoints da api de usuário (CRUD)

* Cadastro (Método POST)
    * Endpoint
        * ```/api/user/```
    * Formato do dado a ser enviado
        * {
            "name":"",
            "email":"",
            "born_date":"YYYY-MM-DD",
            "password":"########"
        }

* Listagem (Método GET)
    * Endpoint
        * ```/api/user/```

* Edição (Método PUT)
    * Endpoint
        * ```/api/user/<pk:register>/```
    * Formato do dado a ser enviado
        * {
            "name":"",
            "email":"",
            "born_date":"YYYY-MM-DD",
            "password":"########"
        }
* Exclusão (Método DELETE)
    * Endpoint
        * ```/api/user/<pk:register>/```

#

# Passo a passo para executar o servidor (API) (sem Docker):

* Crie uma **virtual env** com o Python:
    * ```python3 -m venv .venv```

* Ative a **virtual env**:
    * Linux: ```source .venv/bin/active```
    * Windows: ```.venv\Scripts\activate.bat```

* Instale os **requirements.txt**:
    * ```pip install -r requirements.txt```

* Aplique as migrações:
    * ```python manage.py migrate```

* Execute o servidor:
    * ```python manage.py runserver 0.0.0.0:8000```


