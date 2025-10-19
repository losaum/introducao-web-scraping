# Aula 02 - Exemplo 02: Extraindo Links de Categorias

# Este script foca em extrair uma lista de links de uma página.
# O objetivo é coletar todas as categorias de livros da barra lateral.
# Isso ensina a:
# 1. Encontrar um contêiner específico (a lista de categorias).
# 2. Navegar dentro desse contêiner para encontrar todos os links.
# 3. Extrair tanto o texto do link (nome da categoria) quanto o atributo `href` (o link em si).

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    # 1. Encontrar o contêiner da lista de categorias.
    # Inspecionando a página, vemos que está dentro de uma <div> com a classe 'side_categories'.
    sidebar = soup.find("div", class_="side_categories")

    # 2. Dentro do sidebar, encontramos a lista `<ul>` e depois todos os itens `<li>`.
    # O seletor CSS `ul > li > a` seria uma alternativa (veremos seletores CSS mais tarde).
    category_tags = sidebar.find("ul").find_all("a")

    print("--- Categorias de Livros Encontradas ---\n")
    for tag in category_tags:
        nome_categoria = tag.text.strip()
        link_parcial = tag["href"]
        # O link no site é relativo ('catalogue/category/books/travel_2/index.html').
        # Vamos construir o link completo.
        link_completo = URL + link_parcial
        print(f"Categoria: {nome_categoria} -> Link: {link_completo}")

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")
