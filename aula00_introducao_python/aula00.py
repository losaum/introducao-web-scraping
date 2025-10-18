# Aula 00: Exemplos Básicos de Python para Programadores

# 1. Variáveis e Tipos de Dados
# Python tem tipagem dinâmica. Você não precisa declarar o tipo.
nome_curso = "Web Scraping com Python"  # String (str)
ano = 2024  # Integer (int)
versao = 1.0  # Float (float)
ativo = True  # Boolean (bool)

print("--- Variáveis e Tipos ---")
# f-strings (strings formatadas) são a maneira moderna e fácil de incluir variáveis em strings.
print(f"Curso: {nome_curso}")
print(f"Ano: {ano}")
print("-" * 20)

# 2. Estruturas de Dados

# Listas (mutáveis, ordenadas, como arrays)
bibliotecas = ["requests", "beautifulsoup4", "lxml"]
bibliotecas.append("json")  # Adiciona um item ao final da lista

print("\n--- Listas ---")
print(f"Bibliotecas que usaremos: {bibliotecas}")
print(f"A primeira biblioteca é: {bibliotecas[0]}")

# Dicionários (mutáveis, pares de chave-valor, como hashmaps ou objects)
aluno = {"nome": "Alex", "experiencia": "JavaScript", "nivel": "Pleno"}
aluno["nivel"] = "Sênior"  # Atualiza um valor

print("\n--- Dicionários ---")
print(f"Dados do aluno: {aluno}")
print(f"A experiência do aluno é em: {aluno['experiencia']}")
print("-" * 20)

# for key, value in aluno.items():
#   print(key, value)

# 3. Funções e Estruturas de Controle


def verificar_biblioteca(nome_biblioteca, lista_de_bibliotecas):
    """Uma função simples que verifica se um item existe em uma lista."""
    if nome_biblioteca in lista_de_bibliotecas:
        return f"Sim, '{nome_biblioteca}' está na lista!"
    else:
        return f"Não, '{nome_biblioteca}' não foi encontrada."


print("\n--- Funções e Condicionais ---")
print(verificar_biblioteca("requests", bibliotecas))
print(verificar_biblioteca("selenium", bibliotecas))

print("\n--- Loop For ---")
# O loop 'for' é muito poderoso para iterar sobre itens
for lib in bibliotecas:
    print(f"Instalando a biblioteca: {lib}...")

print("\nAquecimento concluído! Estamos prontos para a Aula 01.")
