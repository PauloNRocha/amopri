# Changelog

## 0.2.1 - 2024-10-27
- Ajuste para garantir que os diretórios raiz e `backend/` sejam adicionados ao `PYTHONPATH` (manage.py/conftest), permitindo importar `backend.amopri` em execuções locais e na pipeline.
- Atualização das referências de configuração (settings, ASGI/WSGI, pytest) para o pacote `backend.amopri`.


## 0.2.0 - 2024-10-27
- Adição de `backend/requirements-dev.txt` com dependências de testes (pytest e pytest-django).
- Configuração do ambiente de testes via `pytest.ini` e `conftest.py` para reconhecer o pacote Django.
- Criação do workflow de CI `.github/workflows/ci.yml` executando `manage.py check` e `pytest`.

## 0.1.2 - 2024-10-27
- Correção no carregamento das configurações `DEFAULT_MONTHLY_FEE` e `DEFAULT_DUE_DAY`, evitando uso de métodos inexistentes em `django-environ`.

## 0.1.1 - 2024-10-27
- Configuração inicial do projeto Django: `manage.py`, arquivos `settings`, `urls`, `wsgi` e `asgi`.
- Ajuste do app `associados` com `AppConfig` e módulo de URLs básico.
- Definição de dependências principais no `backend/requirements.txt`.
- Leituras de configuração via variáveis de ambiente com `django-environ`.

## 0.1.0 - 2024-10-27
- Criação da estrutura inicial de diretórios e arquivos vazios para o projeto Django, incluindo backend, deploy e docs.
- Adição deste arquivo de changelog para rastrear futuras alterações.
- Inclusão de `.gitignore` com regras padrão para Python/Django e ferramentas comuns.
