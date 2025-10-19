# Aula 00 - Exemplo 03: Mini-tutorial de Pandas
#
# Pandas é a biblioteca mais poderosa e popular em Python para análise e manipulação de dados.
# Ela introduz duas estruturas de dados principais: Series (1D) e DataFrame (2D, como uma tabela/planilha).
#
# Para executar este script, você precisará adicionar o pandas e outras bibliotecas ao seu projeto.
# Com o Poetry, execute no terminal:
# poetry add pandas openpyxl lxml
#
# - pandas: A biblioteca principal.
# - openpyxl: Necessário para o pandas ler e escrever arquivos Excel (.xlsx).
# - lxml: Uma das bibliotecas que o pandas pode usar para ler tabelas de HTML (já instalamos antes).

import pandas as pd
import requests
import io
import os

# --- 1. Criando um DataFrame do zero ---
print("--- 1. Criando um DataFrame ---")
dados = {
    "Nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "Idade": [28, 35, 22, 45],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"],
}
df_manual = pd.DataFrame(dados)
print("DataFrame criado manualmente:")
print(df_manual)
print("-" * 30)


# --- 2. Informações básicas sobre o DataFrame ---
print("\n--- 2. Informações Básicas ---")
print("Cabeçalho (5 primeiras linhas):")
print(df_manual.head())  # Mostra as 5 primeiras linhas
print("\nInformações gerais (tipos de dados, etc):")
df_manual.info()
print("\nEstatísticas descritivas (para colunas numéricas):")
print(df_manual.describe())
print("-" * 30)


# --- 3. Lendo dados de um CSV ---
# Para este exemplo, vamos simular um arquivo CSV usando uma string.
# O `io.StringIO` faz com que o pandas leia a string como se fosse um arquivo.
print("\n--- 3. Lendo de um CSV (simulado) ---")
csv_data = """id,produto,preco,em_estoque
101,Laptop,4500.00,True
102,Mouse,89.90,True
103,Monitor,1200.50,False
104,Teclado,250.00,True
"""
df_csv = pd.read_csv(io.StringIO(csv_data))
print("DataFrame lido do CSV:")
print(df_csv)
print("-" * 30)


# --- 4. Selecionando e Filtrando Dados ---
print("\n--- 4. Selecionando e Filtrando ---")
# Selecionando uma coluna (retorna uma Series)
produtos = df_csv["produto"]
print("Coluna 'produto':")
print(produtos)

# Filtrando linhas com base em uma condição
produtos_caros = df_csv[df_csv["preco"] > 1000]
print("\nProdutos com preço maior que 1000:")
print(produtos_caros)
print("-" * 30)


# --- 5. Lendo tabelas de uma página Web ---
print("\n--- 5. Lendo tabela da Web ---")
url_wiki = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"

# 1. Criamos um cabeçalho (header) que simula um acesso via navegador Chrome
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 2. Fazemos a requisição usando a biblioteca requests com o nosso 'disfarce'
    print("Fazendo requisição para a URL com headers...")
    response = requests.get(url_wiki, headers=headers)
    
    # Isso vai gerar um erro se a página não for encontrada ou se o acesso for bloqueado
    response.raise_for_status()
    print("Página baixada com sucesso!")

    # 3. Agora, entregamos o CONTEÚDO HTML baixado para o pandas ler
    # Usamos o 'match' para garantir que pegamos a tabela certa
    lista_de_dfs = pd.read_html(response.text, match="População")
    
    print(f"Encontrada {len(lista_de_dfs)} tabela(s) no HTML com a palavra 'População'.")
    
    df_populacao = lista_de_dfs[0]
    
    print("\n--- Tabela encontrada com sucesso! ---")
    print(df_populacao.head())

# Capturando erros de forma mais específica
except requests.exceptions.RequestException as e:
    print(f"ERRO DE CONEXÃO: Não foi possível baixar a página. Erro: {e}")
except ValueError as e:
    print(f"ERRO DO PANDAS: A tabela com o texto 'População' não foi encontrada no HTML. O site pode ter mudado. Erro: {e}")
except IndexError:
    print("ERRO DE ÍNDICE: O pandas não retornou nenhuma tabela. Verifique o HTML da página.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
print("-" * 30)


# --- 6. Salvando dados em arquivos ---
# Vamos salvar o DataFrame da população em CSV e Excel.
print("\n--- 6. Salvando em arquivos ---")

# Define o caminho para a pasta de saída
output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)  # Cria a pasta se não existir

caminho_csv = os.path.join(output_dir, "populacao_brasil.csv")
caminho_excel = os.path.join(output_dir, "populacao_brasil.xlsx")


# Salvando em CSV
# index=False evita que o índice do DataFrame seja salvo como uma coluna no arquivo
df_populacao.to_csv(caminho_csv, encoding="utf-8")
print(f"DataFrame salvo em CSV: {caminho_csv}")

# Salvando em Excel (requer a biblioteca openpyxl)
df_populacao.to_excel(caminho_excel, sheet_name="População")
print(f"DataFrame salvo em Excel: {caminho_excel}")
