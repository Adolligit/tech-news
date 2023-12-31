import sys


# Requisito 12
def analyzer_menu():
    """Abrindo PR"""
    c = 'Selecione uma das opções a seguir:\n '\
        '0 - Popular o banco com notícias;\n '\
        '1 - Buscar notícias por título;\n '\
        '2 - Buscar notícias por data;\n '\
        '3 - Buscar notícias por tag;\n '\
        '4 - Buscar notícias por categoria;\n '\
        '5 - Listar top 5 notícias;\n '\
        '6 - Listar top 5 categorias;\n '\
        '7 - Sair.\n'

    arr = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a tag:",
        "Digite a categoria:",
        "",
        "",
    ]

    try:
        print(arr[int(input(c))-1])
    except (ValueError, IndexError):
        print("Opção inválida", file=sys.stderr)
