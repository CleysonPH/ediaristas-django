# Projeto Backend E-Diaristas em Django

Projeto realizado durante a imerssão Multi Stack da [TreinaWeb](https://treinaweb.com.br/).

## Dependências de Produção

- Django
- django-adminlte3
- django-bootstrap4

## Dependências de Desenvolvimento

- poetry
- black

## Requisitos

- Python 3.8 ou superior

## Como testar esse projeto na minha máquina?

Clone este repositório e ente na pasta do projeto

```bash
git clone https://github.com/CleysonPH/ediaristas-django.git
cd ediaristas-django
```

Crie um novo ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual

```bash
source .venv/bin/activate
```

Instale as dependências do projeto

```sh
pip install -r requirements.txt
```

Altere as configurações do BD no arquivo `settings.py`
```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ediaristas",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "ediaristas_user",
        "PASSWORD": "ediaristas_password",
    }
}
```

Crie o banco de dados

```sh
python manage.py migrate
```

Execute o servidor de desenvolvimento do Django

```sh
python manage.py runserver
```

E então acessar a aplicação em http://localhost:8000/

## Como contribuir com o projeto?

Para contribuir com o projeto, faça um clone, crie um ambiente virtual com o poetry e instale as dependências de desenvolvimento

```bash
git clone https://github.com/CleysonPH/ediaristas-django.git
cd ediaristas-django
poetry install
```