# Aula 3: Organizando e Salvando Nossos Tesouros

**Objetivo da Aula:** Estruturar os dados coletados em um formato limpo (lista de dicionários), salvá-los em um arquivo JSON e revisar o projeto completo.

---

### Parte 1: Estruturando os Dados (30 min)

1.  **Recap da Aula 2**
    -   Conseguimos extrair títulos e preços, mas eles são apenas impressos no terminal.
    -   Como podemos usar esses dados depois? Precisamos de uma estrutura.

2.  **Dicionários Python para Organização**
    -   Um dicionário é perfeito para representar um item com várias características (chave-valor).
    -   Em vez de apenas imprimir, vamos criar um dicionário para cada livro.

    ```python
    livro_dados = {
        'titulo': 'A Light in the Attic',
        'preco': 51.77,
        'avaliacao': 3
    }
    ```

3.  **Listas de Dicionários**
    -   Para guardar todos os livros, criaremos uma lista vazia no início do script.
    -   A cada livro que nosso loop encontra, criamos o dicionário correspondente e o adicionamos a essa lista usando `.append()`.

    ```python
    lista_de_livros = []
    # ... dentro do loop ...
    livro_dados = {'titulo': titulo, 'preco': preco}
    lista_de_livros.append(livro_dados)
    ```
    -   Ao final, teremos uma única variável (`lista_de_livros`) contendo todos os dados de forma organizada.

4. **Limpando e Convertendo os Dados**
    -   Muitas vezes, os dados que extraímos vêm "sujos". O preço vem com "£", e a avaliação vem como texto ("Three").
    -   É uma ótima prática limpar esses dados durante a extração.
    -   **Preço:** Podemos remover o "£" e converter a string para um número (float).
    -   **Avaliação:** Podemos criar um "mapa" (um dicionário) para converter o texto da avaliação ("One", "Two", ...) para um número (1, 2, ...).
        ```python
        mapa_avaliacao = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        texto_avaliacao = "Three" # Extraído do HTML
        numero_avaliacao = mapa_avaliacao.get(texto_avaliacao, 0) # 0 como padrão se não encontrar
        ```
    - Isso torna nossos dados finais muito mais valiosos para análises e processamento posterior.


---

### Parte 2: Mão na Massa - Salvando em JSON

1.  **O que é JSON? (JavaScript Object Notation)**
    -   É um formato de texto leve e universal, ideal para troca de dados entre sistemas.
    -   É muito fácil de ler tanto para humanos quanto para máquinas.
    -   A estrutura de "lista de dicionários" do Python é convertida quase que diretamente para o formato JSON.

2.  **Módulo `json` do Python**
    -   O Python tem um módulo embutido chamado `json` para trabalhar com este formato.
    -   **Abra e analise os arquivos `aula03_exemplo_01.py` e `aula03_exemplo_02.py`**.
    -   Usaremos `with open(...)` para abrir um arquivo de forma segura (ele fecha o arquivo automaticamente).
    -   O comando `json.dump()` "despeja" nossa lista de dicionários Python diretamente no arquivo, no formato JSON.
        -   `json.dump(dados, arquivo, ...)`
        -   `ensure_ascii=False`: Garante que caracteres especiais como 'ç' e 'ã' sejam salvos corretamente.
        -   `indent=2`: Formata o arquivo JSON com indentação, tornando-o muito mais fácil de ler.

3.  **Execute o script:** `python aula03_exemplo_01.py`
    -   Após a execução, um novo arquivo chamado `livros.json` será criado.
    -   Abra-o e veja seus dados coletados, limpinhos e organizados!

---

### Parte 3: Revisão e Próximos Passos

1.  **Revisão do Fluxo Completo**
    -   `requests.get()`: Faz a requisição e obtém o HTML.
    -   `BeautifulSoup()`: Cria um objeto "sopa" para analisar o HTML.
    -   `soup.find_all()`: Encontra todos os elementos de interesse (os livros).
    -   **Loop `for`**: Itera sobre cada elemento encontrado.
    -   `elemento.find()`: Busca dados específicos (título, preço) dentro de cada elemento.
    -   **Dicionário**: Organiza os dados de um único item.
    -   **Lista**: Agrupa todos os dicionários (todos os itens).
    -   `json.dump()`: Salva a lista final em um arquivo `.json`.

2.  **Desafios e Ferramentas Avançadas**
    -   **Paginação:** E se quisermos os livros da página 2, 3, 4...? Teríamos que criar um loop que muda a URL a cada iteração.
    -   **JavaScript:** Muitos sites modernos carregam dados com JavaScript após a página carregar. `requests` não executa JavaScript, então o HTML que ele baixa pode vir "vazio".
    -   **Bloqueios:** Fazer muitas requisições rápidas pode fazer o site te bloquear.
    -   **Soluções:** Para esses casos mais complexos, existem ferramentas mais avançadas como `Selenium` (que automatiza um navegador real, executando JavaScript) e `Scrapy` (um framework completo para projetos de scraping maiores).

