* **Passo a passo (API)**:

    * Entre no diretório **api-desafio**:
        * ```cd api-desafio```

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
