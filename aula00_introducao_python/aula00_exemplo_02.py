# Aula 00 - Exemplo 02: Manipulando uma Estrutura de Dados

# Este exemplo simula um pequeno programa que trabalha com uma lista de produtos.
# Bom para praticar loops, condicionais e manipulação de dicionários.

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 350.00, "categoria": "Periféricos"},
    {"id": 2, "nome": "Mouse Gamer", "preco": 150.50, "categoria": "Periféricos"},
    {
        "id": 3,
        "nome": "Monitor 24 polegadas",
        "preco": 950.00,
        "categoria": "Monitores",
    },
    {"id": 4, "nome": "Cadeira Gamer", "preco": 1250.00, "categoria": "Móveis"},
    {"id": 5, "nome": "Headset 7.1", "preco": 450.00, "categoria": "Periféricos"},
]


def filtrar_produtos_por_preco(lista_produtos, preco_maximo):
    """Retorna uma nova lista com produtos até um certo preço."""
    produtos_filtrados = []
    for produto in lista_produtos:
        if produto["preco"] <= preco_maximo:
            produtos_filtrados.append(produto)
    return produtos_filtrados


def buscar_produto_por_nome(lista_produtos, nome_busca):
    """Busca um produto pelo nome e retorna seus detalhes."""
    for produto in lista_produtos:
        # Usamos .lower() para fazer uma busca case-insensitive (não diferencia maiúsculas/minúsculas)
        if nome_busca.lower() in produto["nome"].lower():
            return produto
    return None  # Retorna None se não encontrar o produto


# --- Demonstração ---

print("--- Produtos com preço até R$ 400.00 ---")
produtos_acessiveis = filtrar_produtos_por_preco(produtos, 400.00)
for p in produtos_acessiveis:
    print(f"- {p['nome']}: R$ {p['preco']:.2f}")

print("\n--- Buscando por 'gamer' ---")
produto_encontrado = buscar_produto_por_nome(produtos, "gamer")
if produto_encontrado:
    print(f"Produto encontrado: {produto_encontrado}")
else:
    print("Nenhum produto encontrado com o termo 'gamer'.")
