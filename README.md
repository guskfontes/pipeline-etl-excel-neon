# pipeline-etl-excel-neon
# 🚀 Pipeline ETL: Do Excel para a Nuvem com Python e SQL

Este projeto é um pipeline de Engenharia de Dados completo que automatiza o processamento de doações da Associação ASSP.

## 🎯 O Desafio
A associação controlava doações manualmente em Excel, o que gerava:
- Erros de digitação e dados "sujos".
- Duplicidade de pagamentos.
- Dificuldade para cruzar quem pagou com a lista de sócios ativos.

## 🛠️ A Solução
Desenvolvi uma automação em **Python** que atua como um processo ETL (Extract, Transform, Load):
1.  **Extract:** Lê as planilhas de Associados e Doações (`pandas`).
2.  **Transform:**
    - Cruza os dados usando o email como chave (VLOOKUP via código).
    - Valida integridade (se o doador não existe, a doação não entra).
    - Remove duplicidades e padroniza formatos.
3.  **Load:** Insere os dados limpos em um banco de dados **PostgreSQL** na nuvem (Neon Tech).

## 💻 Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **Bibliotecas:** Pandas, SQLAlchemy, Psycopg2
- **Banco de Dados:** PostgreSQL (Neon Serverless)
- **Editor:** VS Code

## ⚙️ Como rodar este projeto
1.  Clone o repositório.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure sua conexão com o banco no arquivo `etl_assp.py`.
4.  Execute o script:
    ```bash
    python etl_assp.py
    ```

---
*Projeto desenvolvido por Gustavo Fontes.*
