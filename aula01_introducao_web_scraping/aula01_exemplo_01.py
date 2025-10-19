# Aula 1: Fazendo nossa primeira requisição web com a biblioteca 'requests'.

import requests

# 1. URL do site que queremos acessar.
# Usaremos o 'books.toscrape.com', um site feito para praticar scraping.
URL = "https://books.toscrape.com/"

print(f"Iniciando a requisição para: {URL}")

try:
    # 2. Fazendo a requisição GET para a URL.
    # A requisição GET é o que o seu navegador faz quando você digita um endereço e aperta Enter.
    # O 'timeout' é uma boa prática para evitar que seu script fique "preso" para sempre
    # se o site demorar muito para responder.
    response = requests.get(URL, timeout=10)

    # 3. Verificando se a requisição foi bem-sucedida.
    # Códigos de status HTTP:
    # - 200: OK (Tudo certo)
    # - 404: Not Found (Página não encontrada)
    # - 403: Forbidden (Acesso negado)
    # - 500: Internal Server Error (Erro no servidor)
    response.raise_for_status()  # Isso vai gerar um erro se o status não for 2xx (sucesso).

    print("Requisição bem-sucedida! Status Code:", response.status_code)

    # 3.1. Exibindo alguns detalhes da resposta
    print("\n--- Detalhes da Resposta ---")
    print(dir(response))  # Mostra os atributos e métodos do objeto response
    print("\nCabeçalhos da Resposta:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")        
        #input("Pressione Enter para continuar ...")
    print("-" * 30)
    
    print("\nConteúdo da página (primeiros 500 caracteres):")
    print(response.text[:1000])  # Mostra os primeiros 1000 caracteres do HTML        
    print("-" * 30)

    # fazendo uma pausa antes de salvar, pressinte Enter para continuar
    input("Pressione Enter para salvar o conteúdo HTML em 'pagina.html'...")



    # 4. Salvando o conteúdo da página em um arquivo HTML.
    # 'response.text' contém o HTML completo da página como uma string.
    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("O conteúdo HTML foi salvo no arquivo 'pagina.html'.")

except requests.exceptions.RequestException as e:
    # Captura qualquer erro que possa ocorrer durante a requisição (ex: sem internet, URL errada).
    print(f"Ocorreu um erro na requisição: {e}")
