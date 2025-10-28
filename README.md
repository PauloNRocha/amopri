# AMOPRI – Sistema Web para Associação de Moradores (MVP)

Sistema web para a AMOPRI – Associação de Moradores Princesa Isabel. Foca em cadastro de associados, geração e controle de faturas mensais, relatórios básicos e operação via Django Admin. Este repositório implementa o MVP com base robusta para evoluir em integrações (PIX/boleto), API e área do associado.

## Visão Geral
- Cadastro de associados com dados de contato e endereço.
- Faturas mensais (status: Aberta, Paga, Atrasada, Cancelada) e baixa manual de pagamentos.
- Admin com filtros, busca, e ações em massa (marcar pago/cancelar).
- Testes automatizados e CI GitHub Actions (checks e pytest).

Status atual: v0.3.0 (MVP com modelos, admin e testes de fumaça).

## Stack
- Backend: Python 3.12 + Django 5 + Django Rest Framework (base para APIs futuras)
- Banco: SQLite (dev) ou PostgreSQL (produção via `DATABASE_URL`)
- Testes: pytest + pytest-django
- CI: GitHub Actions (workflow em `.github/workflows/ci.yml`)

## Estrutura de Pastas
```
backend/
  manage.py
  amopri/
    settings.py
    urls.py
    wsgi.py
    asgi.py
  associados/
    models.py
    admin.py
    apps.py
    migrations/
    services/
    management/commands/
    tests/
deploy/
  docker-compose.yml
  Dockerfile.web
  Dockerfile.worker
  nginx.conf
  env.example
docs/
  README.md
  ERD.png
```

## Pré‑requisitos
- Python 3.12+
- pip + venv (ou pyenv)
- (Opcional) Docker + Docker Compose

## Como rodar em desenvolvimento
1) Criar e ativar ambiente virtual
```
python3 -m venv .venv
source .venv/bin/activate
```

2) Instalar dependências
```
pip install -r backend/requirements.txt
# (opcional – testes)
pip install -r backend/requirements-dev.txt
```

3) Variáveis de ambiente
- O projeto lê variáveis via `django-environ`. Por padrão, tenta carregar `deploy/env.example`.
- Opcional: crie um arquivo dedicado e aponte para ele, por exemplo:
```
cp deploy/env.example deploy/env
export AMOPRI_ENV_FILE="$(pwd)/deploy/env"
```
Valores úteis:
```
SECRET_KEY=troque-esta-chave
DEBUG=1
# Para PostgreSQL, use um DATABASE_URL (senão, cai no SQLite local)
# DATABASE_URL=postgres://usuario:senha@localhost:5432/amopri
ALLOWED_HOSTS=*
DEFAULT_MONTHLY_FEE=30.00
DEFAULT_DUE_DAY=10
```

4) Banco de dados
```
python backend/manage.py migrate
python backend/manage.py createsuperuser
```

5) Executar
```
python backend/manage.py runserver 0.0.0.0:8000
```
Acesse `http://localhost:8000/admin/` e entre com o superusuário criado.

## Testes
```
pytest
```
O conjunto inicial inclui testes de fumaça para o app `associados`.

## Deploy (Docker – exemplo mínimo)
Arquivos de `deploy/` estão preparados para um Compose simples. Exemplo base para web:
```
version: "3.9"
services:
  web:
    build:
      context: ..
      dockerfile: deploy/Dockerfile.web
    environment:
      DJANGO_SETTINGS_MODULE: backend.amopri.settings
      SECRET_KEY: troque-esta-chave
      DEBUG: "0"
      # DATABASE_URL: postgres://usuario:senha@db:5432/amopri
    command: bash -lc "python backend/manage.py migrate && gunicorn backend.amopri.wsgi:application -b 0.0.0.0:8000"
    ports:
      - "8000:8000"
```
Ajuste `DATABASE_URL` e adicione serviços de banco/proxy conforme sua infra.

## Roadmap (próximos passos)
- Serviço e comando de geração mensal de faturas (`services/billing.py` + `generate_invoices`).
- Exportações CSV e telas de relatórios no admin.
- Integrações de pagamentos (PIX/Boleto) e webhooks.
- API DRF para futura área do associado (Next.js).

## LGPD (resumo)
- Dados coletados: nome, endereço, telefone(s), e‑mail.
- Finalidade: administração da associação e cobranças.
- Segurança: controle de acesso por perfis, HTTPS no deploy, backups, logs.

## Contribuindo
Contribuições são bem‑vindas! Abra issues/PRs descrevendo motivação e escopo. Para desenvolvimento, garanta `pytest` verde antes do PR.

---

© AMOPRI. Este repositório contém o MVP técnico do sistema interno da associação.
