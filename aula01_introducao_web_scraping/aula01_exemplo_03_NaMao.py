# Parsing manual de web scraping

import requests

# 1. URL do site que queremos acessar.
# Usaremos o 'books.toscrape.com', um site feito para praticar scraping.
URL = "https://books.toscrape.com/"

print(f"Iniciando a requisição para: {URL}")

try:
    response = requests.get(URL, timeout=10) 
    response.raise_for_status()  
    print("Requisição bem-sucedida! Status Code:", response.status_code)
    html_content = response.text

except requests.exceptions.RequestException as e:
  
    print(f"Ocorreu um erro na requisição: {e}")


# ==========================================================================================
# Abordagem 1: Parsing "na Mão" com Métodos de String
# ==========================================================================================

print("\n--- 1. Iniciando Parsing 'na Mão' ---")
print("Objetivo: Extrair o título e o preço de cada livro.")

livros_extraidos_manual = []

# O HTML de cada livro está dentro de uma tag '<article class="product_pod">'
# Vamos usar isso como nosso ponto de partida.
cursor = 0
while True:
    # Encontra o início do bloco do próximo livro
    inicio_bloco = html_content.find('<article class="product_pod">', cursor)
    
    # Se não encontrar mais, saímos do loop
    if inicio_bloco == -1:
        break
    
    # A partir do início do bloco, encontramos seu fim
    fim_bloco = html_content.find('</article>', inicio_bloco)
    
    # "Fatiamos" o HTML para ter apenas o conteúdo de um livro
    html_livro = html_content[inicio_bloco:fim_bloco]
    
    # --- Extraindo o TÍTULO ---
    # O título completo está no atributo 'title' de uma tag <a>
    marcador_titulo = 'title="'
    inicio_titulo = html_livro.find(marcador_titulo) + len(marcador_titulo)
    fim_titulo = html_livro.find('">', inicio_titulo)
    titulo = html_livro[inicio_titulo:fim_titulo]
    
    # --- Extraindo o PREÇO ---
    # O preço está dentro de uma tag <p class="price_color">
    # marcador_preco = '<p class="price_color">Â£' # Incluímos o símbolo da moeda
    # inicio_preco = html_livro.find(marcador_preco) + len(marcador_preco)
    # fim_preco = html_livro.find('</p>', inicio_preco)
    # preco_str = html_livro[inicio_preco:fim_preco]

    # dados = {'titulo': titulo, 'preco': preco_str}
    
    dados = {'titulo': titulo}
    print(titulo)

    livros_extraidos_manual.append(dados)
    
    # Movemos o cursor para o final do bloco que acabamos de analisar
    cursor = fim_bloco

print(f"\n✅ Foram extraídos {len(livros_extraidos_manual)} livros manualmente.")

for livro in livros_extraidos_manual:
    print(livro)

