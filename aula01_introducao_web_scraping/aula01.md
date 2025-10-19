# Aula 1: Web Scraping

**Título:** Web Scraping com Python: Beautiful Soup e Requests

**Objetivo da Aula:** Entender os conceitos fundamentais de web scraping, configurar o ambiente de desenvolvimento e realizar a primeira coleta de dados de uma página web usando a biblioteca `requests`.

links:
- https://realpython.com/python-web-scraping-practical-introduction/
- https://kinsta.com/pt/blog/o-que-e-web-scraping/
- https://medium.com/@nluizsoliveira/introdu%C3%A7%C3%A3o-a-web-scraping-principais-casos-abordagens-e-ferramental-9ffc6459626f

---

### Parte 1: Boas-vindas e Teoria 

1.  **O que é Web Scraping?**
    -   **Definição:** É o processo de usar "robôs" (scripts) para coletar dados de forma automatizada de sites na internet.
    -   **Analogia:** Imagine que, em vez de você copiar e colar manualmente o preço de 100 produtos de um site, um programa faz isso para você em segundos.
    -   **Aplicações:** Monitoramento de preços, geração de leads, análise de sentimento em notícias, pesquisa acadêmica, etc.

2.  **A Ética do Web Scraping**
    -   **Seja um bom vizinho:** Não sobrecarregue o servidor do site com muitas requisições em um curto espaço de tempo. Isso pode derrubar o site.
    -   **`robots.txt`:** Muitos sites têm um arquivo chamado `www.exemplo.com/robots.txt`. Ele informa quais partes do site os robôs podem ou não acessar. **Sempre verifique e respeite este arquivo!**
    -   **Termos de Serviço:** Verifique os Termos de Serviço do site para ver se eles proíbem a coleta automatizada de dados.
    -   **Dados Sensíveis:** Nunca colete dados pessoais ou informações privadas.

3.  **Como a Web Funciona (Brevemente)**
    -   **Cliente-Servidor:** Seu navegador (cliente) faz uma **requisição** (request) a um servidor onde o site está hospedado.
    -   **Resposta (Response):** O servidor envia de volta uma **resposta**, que geralmente contém o código-fonte da página em HTML.
    -   **HTML (HyperText Markup Language):** É a linguagem de marcação que estrutura o conteúdo de uma página (títulos, parágrafos, links, imagens). Nosso objetivo é extrair dados desse HTML.

---

### Parte 2: Preparando o Terreno com Poetry 

1.  **Revisão da Configuração**
    -   Na Aula 00, já preparamos nosso ambiente. Vamos apenas garantir que tudo está no lugar.
    -   Abra seu terminal na pasta do projeto (`introducao-web-scraping`).

    ```bash
    # Ative o ambiente virtual gerenciado pelo Poetry
    poetry shell
    ```
    -   As bibliotecas `requests`, `beautifulsoup4` e `lxml` já foram instaladas com o comando `poetry add`.

---
 
### Parte 3: Mão na Massa - Nossa Primeira Coleta!

Vamos criar nosso primeiro script para buscar o conteúdo HTML de uma página. Usaremos o site `https://books.toscrape.com/`, que foi criado especificamente para praticar web scraping.

1.  **Headers HTTP: O `User-Agent`**
    -   Quando um navegador acessa um site, ele envia "cabeçalhos" (headers) com informações, como qual navegador ele é (`User-Agent`).
    -   Muitos sites bloqueiam requisições que não têm um `User-Agent` de um navegador comum, pois identificam como um robô.
    -   É uma **excelente prática** sempre incluir um `User-Agent` em nossas requisições para parecermos mais "humanos".
    -   ```python
      HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
      response = requests.get(URL, headers=HEADERS)
      ```
2.  **Criando e Executando o Script**
    -   **Crie o arquivo `aula01_exemplo_01.py`** na pasta `aula01`.
2.  **Escreva o código abaixo**.
3.  **Execute o script** no terminal com o comando: `python aula01_exemplo_01.py`

O script irá fazer uma requisição ao site e, se tudo der certo, salvará o conteúdo HTML completo em um arquivo chamado `pagina.html` dentro da pasta `aula01`. Abra este arquivo no seu navegador para ver que é uma cópia local da página!

**Próximos Passos:** Vamos aprender a "ler" esse HTML com a biblioteca Beautiful Soup para extrair apenas as informações que nos interessam, como os títulos e preços dos livros.

---

### Desafio

- Modifique o script para acessar a página de uma categoria específica, por exemplo, "Travel" (`http://books.toscrape.com/catalogue/category/books/travel_2/index.html`).
- Tente acessar um site que você usa no dia a dia (como um portal de notícias) e salve o HTML dele. Observe as diferenças na estrutura.