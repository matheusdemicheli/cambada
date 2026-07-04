# Cambada

Aplicação Django simples com API para frases históricas.

## Rodando com Docker

```bash
docker compose up --build
```

A aplicação ficará disponível em http://localhost:8000.

## Variáveis de ambiente

Copie o arquivo de exemplo e ajuste os valores:

```bash
cp django/.env.example django/.env
```

## Deploy

O projeto já inclui:
- Dockerfile para o backend Django
- docker-compose.yml para execução local
- Procfile para ambientes compatíveis com Procfile
- configuração de estáticos com WhiteNoise
- render.yaml para deploy no Render

### Render

1. Crie um serviço Web no Render apontando para este repositório.
2. O arquivo render.yaml já define build, release e start commands.
3. Ajuste as variáveis de ambiente no painel do Render, especialmente:
   - SECRET_KEY
   - DEBUG=False
   - ALLOWED_HOSTS=seu-app.onrender.com
   - CSRF_TRUSTED_ORIGINS=https://seu-app.onrender.com
   - DATABASE_URL=postgres://... (fornecida automaticamente pelo Render se você adicionar um PostgreSQL)

## Testes

```bash
cd django
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test frases_historicas.tests
```
