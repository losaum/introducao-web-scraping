# Aula 00: Aquecimento com Python e Configuração com Poetry

**Título:** Web Scraping Fácil com Python: Beautiful Soup e Requests

**Objetivo da Aula:** Apresentar os conceitos essenciais de Python para programadores de outras linguagens e configurar o ambiente de desenvolvimento usando Poetry.

---

### Parte 1: Python para Programadores

Se você já programa em linguagens como Java, C#, JavaScript ou PHP, vai se sentir em casa com Python. A principal diferença é a simplicidade e a legibilidade.

1.  **Sintaxe e Indentação:**
    -   Python não usa `{}` para delimitar blocos de código. Em vez disso, ele usa **indentação** (espaços no início da linha). Isso força um código mais limpo e organizado.
    -   O fim de uma instrução é simplesmente o fim da linha (não precisa de `;`).

2.  **Variáveis e Tipagem Dinâmica:**
    -   Você não declara o tipo de uma variável. O tipo é inferido no momento da atribuição.
    -   `nome = "Alice"` (string)
    -   `idade = 30` (integer)
    -   `altura = 1.75` (float)
    -   `eh_programador = True` (boolean)

3.  **Estruturas de Dados Essenciais:**
    -   **Listas (`list`):** Equivalente a arrays dinâmicos.
        -   `frutas = ["maçã", "banana", "laranja"]`
        -   `frutas.append("uva")`
        -   `primeira_fruta = frutas[0]`
    -   **Dicionários (`dict`):** Equivalente a hashmaps, mapas ou objetos.
        -   `pessoa = {"nome": "Beto", "idade": 42}`
        -   `print(pessoa["nome"])`

4.  **Estruturas de Controle:**
    -   **Condicionais (`if/elif/else`):**
        ```python
        if idade < 18:
            print("Menor de idade")
        elif idade >= 65:
            print("Idoso")
        else:
            print("Adulto")
        ```
    -   **Loops (`for`):** Ideal para iterar sobre listas e outros iteráveis.
        ```python
        for fruta in frutas:
            print(f"Eu gosto de {fruta}") # f-strings (com o 'f' antes da string) são ótimas para formatar!
        ```

5.  **Funções (`def`):**
    -   A palavra-chave para definir uma função é `def`.
        ```python
        def saudacao(nome):
            return f"Olá, {nome}!"

        mensagem = saudacao("Carlos")
        print(mensagem)
        ```

---

### Parte 2: Ambiente Profissional com Poetry 

Vamos esquecer `pip` e `requirements.txt` por um momento. O **Poetry** é uma ferramenta moderna que gerencia o ambiente virtual e as dependências do seu projeto de forma integrada.

1.  **O que é o Poetry?**
    -   É um gerenciador de dependências e empacotamento.
    -   Ele cria um ambiente virtual isolado para seu projeto automaticamente.
    -   Ele garante que todos que usarem o projeto terão exatamente as mesmas versões das bibliotecas, evitando o "na minha máquina funciona".

2.  **Instalando o Poetry:**
    -   Siga as instruções de instalação no site oficial: https://python-poetry.org/docs/#installation
    -   Normalmente, para macOS, Linux ou WSL (Windows), o comando é:
        ```bash
        curl -sSL https://install.python-poetry.org | python3 -
        ```

3.  **Criando e Configurando Nosso Projeto:**
    -   Abra seu terminal e vamos criar o projeto do zero com Poetry.

    ```bash
    # 1. Crie um novo projeto com Poetry. Isso cria a estrutura de pastas.
    poetry new introducao-web-scraping
    # Ou, se quiser iniciar um psrojeto na pasta em que você já está.
    poetry init	
    
    # 2. Entre na pasta do projeto.
    cd introducao-web-scraping

    # 3. Adicione as bibliotecas que vamos usar no curso.
    # O Poetry vai baixar as bibliotecas, adicioná-las ao arquivo de configuração (pyproject.toml)
    # e criar o ambiente virtual se ele não existir.
    poetry add requests beautifulsoup4 lxml
    
    # Para os exemplos com Pandas, também precisaremos de:
    poetry add pandas openpyxl
    
    # 4. Ative o ambiente virtual gerenciado pelo Poetry.
    # Seu terminal agora mostrará que você está dentro do ambiente.
    poetry shell
    ```

4.  **Executando um Script:**
    -   Com o ambiente ativado (`poetry shell`), você pode executar seus scripts Python normalmente.
    -   Por exemplo, para executar um script:
        ```bash
        # Certifique-se de que o arquivo está na pasta correta
        python aula00_introducao_python/aula00.py
        ```

**Pronto!** Nosso ambiente está configurado de forma profissional. Na próxima aula, começaremos a fazer o web scraping de verdade.

**Se quiser, já pode abrir o VSCode com o interpretador atual com o comando:** 
```bash
    code .
```