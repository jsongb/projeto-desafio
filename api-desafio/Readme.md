# Projeto Desafio (Api do projeto)

Foi usado Docker com o objetivo de compatibilidade.

## Requisitos para executar o projeto

- Docker

    https://docs.docker.com/desktop/

    
- Make (opcional)

    ```apt-get install make```
#
## Como executar o projeto?

### Use um dos comandos abaixo

* ```make start```

    *Obs: para executar o Makefile é necessário instalar o **make***

* Ou execute o script abaixo:

    * Linux: 
        
        ```. start.sh```


    * Windows: 
        
        ```start.bat```
        
* Ou execute os comandos abaixo em sequência

    ```docker compose build```

    ```docker compose run api python manage.py migrate```

    ```docker compose run api python manage.py migrate api```

    ```docker compose run api python manage.py initadmin```

    ```docker compose up -d```

    *Obs: Verifique a versão do docker instalada pois há uma diferença no **alias** em versões atuais (use **docker-compose** ou **docker compose {V2}**).

#
## A api ficará disponível em http://localhost:8000/api/


