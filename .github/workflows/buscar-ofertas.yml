name: Buscar ofertas

on:
  workflow_dispatch:
  schedule:
    - cron: "0 */6 * * *"

jobs:
  buscar:
    runs-on: ubuntu-latest

    steps:
      - name: Baixar projeto
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Executar buscador
        run: python main.py
