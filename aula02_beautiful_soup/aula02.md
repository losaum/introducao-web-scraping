# Aula 2: Decifrando o HTML com Beautiful Soup 

**Objetivo da Aula:** Aprender a usar a biblioteca `BeautifulSoup` para analisar (fazer o "parse") do código HTML e extrair informações específicas, como títulos, preços e links.

---

### Parte 1: Recap e Introdução ao Beautiful Soup 

1.  **O que é o Beautiful Soup? (10 min)**
    -   É uma biblioteca Python para "puxar" dados de arquivos HTML e XML.
    -   Ela cria uma "árvore" de objetos Python a partir do HTML, o que torna a navegação e a busca por elementos muito mais fácil do que trabalhar com o texto puro.
    -   Ela não baixa a página da internet, apenas interpreta o HTML que já temos (obtido com o `requests`).

2.  **Instalando e Configurando**
    -   Na Aula 00, já instalamos as bibliotecas necessárias (`beautifulsoup4` e `lxml`) com o Poetry.
    -   O `lxml` é o "analisador" (parser) que o Beautiful Soup usará para ler o HTML. Ele é muito rápido e eficiente.
    -   **Nosso fluxo completo agora é:** `requests` (baixa o HTML) -> `BeautifulSoup` com `lxml` (interpreta o HTML).

---

### Parte 2: Navegando na "Sopa" de Tags

Vamos usar o `aula02_exemplo_01.py` para praticar. O script já combina os passos da Aula 1 com os novos conceitos.

1.  **Criando o Objeto `Soup`**
    -   A primeira coisa a fazer é passar o conteúdo HTML para o `BeautifulSoup`.
    -   `soup = BeautifulSoup(response.text, 'lxml')`

2.  **Encontrando Elementos (Tags)**
    -   Para encontrar informações, precisamos inspecionar o HTML da página no navegador (clique com o botão direito -> "Inspecionar") para descobrir as tags e classes dos elementos que queremos.

    -   **`soup.find('tag_name')`**: Encontra a **primeira** ocorrência de uma tag.
        -   *Exemplo:* `soup.find('h1')` vai encontrar o primeiro título principal da página.

    -   **`soup.find_all('tag_name')`**: Encontra **todas** as ocorrências de uma tag e retorna uma lista.
        -   *Exemplo:* `soup.find_all('a')` vai encontrar todos os links da página.

3.  **Filtrando por Atributos**
    -   Achar todas as tags `<a>` pode não ser útil. Queremos ser mais específicos.
    -   Podemos passar um dicionário `attrs` para filtrar por atributos como `class`, `id`, `href`, etc.
    -   *Exemplo:* No site `books.toscrape.com`, cada livro está dentro de um `<article class="product_pod">`.
        -   `soup.find_all('article', attrs={'class': 'product_pod'})`

4.  **Extraindo o Conteúdo**
    -   Uma vez que temos um elemento (uma tag), como pegamos o que está dentro dele?
    -   **`.text`**: Retorna o texto visível dentro da tag.
        -   *Exemplo:* Se `tag = <p>Olá Mundo</p>`, então `tag.text` retorna `"Olá Mundo"`.
    -   **`.get('attribute_name')`**: Retorna o valor de um atributo.
        -   *Exemplo:* Se `tag = <a href="link.html">Clique aqui</a>`, `tag.get('href')` retorna `"link.html"`.

---

### Parte 3: Mão na Massa - Coletando Dados dos Livros

1.  **Abra o arquivo `aula02_exemplo_01.py`**.
2.  **Analise o código:**
    -   Ele faz a requisição (como na Aula 1).
    -   Cria o objeto `soup`.
    -   Encontra todos os "cards" de livros usando `find_all`.
    -   Para cada livro encontrado, ele entra nesse "pedaço" de HTML e busca:
        -   O título, que está dentro de uma tag `<h3>` e depois `<a>`.
        -   O preço, que está dentro de um `<p class="price_color">`.
    -   Imprime as informações de forma organizada.
3.  **Execute o script:** `python exemplo_aula02.py`

Você verá no terminal uma lista com o título e o preço de cada livro da primeira página!

---

### Desafio (Opcional)
- Inspecione a página e descubra como a avaliação (as estrelas) de cada livro é representada no HTML.
- Modifique o script `exemplo_aula02.py` para extrair e imprimir também a avaliação de cada livro. Dica: a informação está em uma classe dentro de uma tag `<p>`.

