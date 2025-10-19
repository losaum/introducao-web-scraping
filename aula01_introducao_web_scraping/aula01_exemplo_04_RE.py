# Parsing com regex (Expressões Regulares)

import requests
import re

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
# Abordagem 2: Parsing com Expressões Regulares (Regex)
# ==========================================================================================
print("\n--- 2. Iniciando Parsing com Expressões Regulares (Regex) ---")

# Criamos um padrão (pattern) que descreve a estrutura que queremos encontrar.
# Os parênteses ( ) criam "grupos de captura" para extrair os dados.
# title="([^"]+)" -> Captura qualquer coisa que não seja aspas duplas dentro do atributo title.
# .*? -> Pula qualquer caractere, de forma "não gulosa", até encontrar o próximo marcador.
# price_color">£([\d.]+) -> Captura um ou mais dígitos (\d) ou pontos (.) após o símbolo da libra.
padrao = re.compile(
    r'title="([^"]+)".*?<p class="price_color">.£([\d.]+)</p>',
    re.DOTALL  # Flag para fazer o '.' corresponder também a quebras de linha
)

# Usamos findall para encontrar TODAS as ocorrências do padrão no HTML
matches = padrao.findall(html_content)

print(f"\n✅ Regex encontrou {len(matches)} correspondências.")
print("Amostra das 3 primeiras (o resultado é uma lista de tuplas):")
print(matches[:3])

# Vamos formatar a saída para ficar mais clara
livros_extraidos_regex = []
for match in matches:
    titulo = match[0]
    preco = float(match[1])
    livros_extraidos_regex.append({'titulo': titulo, 'preco': preco})


for livro in livros_extraidos_regex:
    print(livro)