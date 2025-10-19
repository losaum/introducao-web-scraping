# Aula 3: Estruturando os dados e salvando em um arquivo JSON.

import requests
from bs4 import BeautifulSoup
import json  # Importando o módulo para trabalhar com JSON
import os

URL = "https://books.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Mapa para converter a classe da avaliação em um número
MAPA_AVALIACAO = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def extrair_dados_livros(url):
    """
    Função que extrai os dados dos livros de uma URL e retorna uma lista de dicionários.
    """
    try:
        print(f"Buscando dados em: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        livros = soup.find_all("article", class_="product_pod")
        dados_livros = []  # 1. Criamos uma lista vazia para armazenar os dados

        for livro in livros:
            titulo_tag = livro.find("h3").find("a")
            titulo = titulo_tag["title"]

            preco_tag = livro.find("p", class_="price_color")
            # Limpando o preço: remove o símbolo '£' e converte para float
            preco_str = preco_tag.text.strip().replace("Â£", "")
            preco = float(preco_str)

            # Extraindo a avaliação
            # A avaliação está na classe de uma tag <p>, ex: <p class="star-rating Three">
            avaliacao_tag = livro.find("p", class_="star-rating")
            # A classe é uma lista, ex: ['star-rating', 'Three']. Pegamos o segundo item.
            texto_avaliacao = avaliacao_tag["class"][1]
            # Convertemos o texto para número usando nosso mapa
            avaliacao_num = MAPA_AVALIACAO.get(texto_avaliacao, 0)  # 0 se não encontrar

            # 2. Para cada livro, criamos um dicionário com seus dados
            livro_info = {"titulo": titulo, "preco": preco, "avaliacao": avaliacao_num}
            # 3. Adicionamos o dicionário à nossa lista
            dados_livros.append(livro_info)
        return dados_livros

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
        return None


def salvar_em_json(dados, nome_arquivo):
    """
    Salva uma lista de dicionários em um arquivo JSON.
    """
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        # 4. Usamos json.dump() para salvar os dados no arquivo
        # ensure_ascii=False garante a codificação correta de caracteres especiais.
        # indent=2 formata o JSON para ser legível.
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"Dados salvos com sucesso no arquivo '{caminho_arquivo}'!")


if __name__ == "__main__":
    dados_extraidos = extrair_dados_livros(URL)
    if dados_extraidos:
        print(f"\nForam extraídos dados de {len(dados_extraidos)} livros.")
        salvar_em_json(dados_extraidos, "livros.json")

        print("\n--- Exemplos de dados extraídos ---")
        for livro in dados_extraidos[:5]:  # Mostra os primeiros 5 livros como exemplo
            print(livro)    
            
