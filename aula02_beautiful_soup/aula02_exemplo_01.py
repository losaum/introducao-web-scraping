# Aula 2: Usando Beautiful Soup para extrair dados de um HTML.

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

print(f"Buscando dados em: {URL}")

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    # 1. Criar o objeto BeautifulSoup
    # Passamos o conteúdo HTML da resposta e o 'parser' que queremos usar.
    # 'lxml' é uma ótima opção por ser rápido e robusto.
    soup = BeautifulSoup(response.text, "lxml")

    print("HTML analisado com sucesso!\n")
    print("--- DADOS EXTRAÍDOS ---")

    # 2. Encontrar todos os elementos que contêm as informações dos livros.
    # Inspecionando a página, vemos que cada livro está em um <article class="product_pod">.
    # 'find_all' retorna uma lista de todas as tags que correspondem ao critério.
    livros = soup.find_all("article", class_="product_pod")

    # 3. Iterar sobre a lista de livros para extrair os dados de cada um.
    for livro in livros:
        # Dentro de cada 'article' (livro), vamos procurar o título e o preço.

        # O título está dentro de uma tag <h3>, dentro de uma tag <a>.
        # Usamos .find() para navegar na estrutura. O '.text' pega o conteúdo textual.
        # O '.strip()' remove espaços em branco extras do início e do fim.
        titulo_tag = livro.find("h3").find("a")
        titulo = titulo_tag[
            "title"
        ]  # O título completo está no atributo 'title' da tag <a>

        # O preço está dentro de uma tag <p> com a classe 'price_color'.
        preco_tag = livro.find("p", class_="price_color")
        preco = preco_tag.text.strip()

        # Imprimir os dados de forma organizada.
        print(f"Título: {titulo}")
        print(f"Preço: {preco}")
        print("-" * 20)  # Linha separadora

    print(f"\nTotal de {len(livros)} livros encontrados na página.")


except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
except Exception as e:
    print(f"Ocorreu um erro ao processar os dados: {e}")
