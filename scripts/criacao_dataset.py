import random
from datetime import datetime
import pandas as pd
import numpy as np
from faker import Faker
from num2words import num2words


def configurar_faker():
    """Inicializa e retorna o gerador de dados falsos."""
    return Faker()


def gerar_dados_falsos(num_registros, periodo_inicio, periodo_fim, produtos_categorias):
    """
    Gera um conjunto de dados simulados baseado nas configurações fornecidas.

    Args:
        num_registros (int): Número de registros a serem gerados.
        periodo_inicio (datetime.date): Data de início do período.
        periodo_fim (datetime.date): Data de término do período.
        produtos_categorias (list): Lista de tuplas com produtos e categorias.

    Returns:
        list: Lista de dicionários contendo os dados simulados.
    """
    faker = configurar_faker()
    dados = []

    for i in range(1, num_registros + 1):
        produto, categoria = random.choice(produtos_categorias)
        data = faker.date_between(start_date=periodo_inicio, end_date=periodo_fim)
        quantidade = random.randint(1, 20)
        preco = round(random.uniform(50, 5000), 2)  # Preços variando entre 50 e 5000
        dados.append({
            "ID": i,
            "Data": data,
            "Produto": produto,
            "Categoria": categoria,
            "Quantidade": quantidade,
            "Preço": preco
        })

    return dados


def criar_dataframe(dados):
    """Cria e retorna um DataFrame a partir da lista de dados fornecida."""
    return pd.DataFrame(dados)


def baguncar_dados(df):
    """
    Introduz erros simulados no DataFrame para testes e validação.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame modificado com erros introduzidos.
    """
    # Introduzir valores nulos na coluna 'Preço'
    df.loc[random.sample(range(len(df)), 2), 'Preço'] = np.nan

    # Introduzir datas inválidas na coluna 'Data'
    df.loc[random.sample(range(len(df)), 2), 'Data'] = '2024-31-01'

    # Converter algumas quantidades para texto
    for idx in random.sample(range(len(df)), 2):
        df.at[idx, 'Quantidade'] = num2words(df.at[idx, 'Quantidade'], lang='pt-BR')

    return df


def salvar_csv(df, caminho_arquivo):
    """Salva o DataFrame em um arquivo CSV."""
    df.to_csv(caminho_arquivo, index=False)


def gerar_dataset(caminho_saida):
    """
    Gera um dataset de vendas simuladas, bagunça os dados e salva em CSV.

    Args:
        caminho_saida (str): Caminho do arquivo CSV para salvar os dados.
    """
    # Configurações básicas
    num_registros = 50
    periodo_inicio = datetime.strptime('2023-01-01', '%Y-%m-%d').date()
    periodo_fim = datetime.strptime('2023-12-31', '%Y-%m-%d').date()
    produtos_categorias = [
        ("Notebook", "Eletrônicos"),
        ("Smartphone", "Eletrônicos"),
        ("Geladeira", "Eletrodomésticos"),
        ("Microondas", "Eletrodomésticos"),
        ("Sofá", "Móveis"),
        ("Cadeira Gamer", "Móveis"),
        ("Tênis Esportivo", "Calçados"),
        ("Sandália", "Calçados"),
        ("Camiseta", "Vestuário"),
        ("Calça Jeans", "Vestuário"),
    ]

    # Gerar dados simulados
    dados = gerar_dados_falsos(num_registros, periodo_inicio, periodo_fim, produtos_categorias)

    # Criar DataFrame
    df = criar_dataframe(dados)

    # Bagunçar os dados
    df = baguncar_dados(df)

    # Salvar no arquivo CSV
    salvar_csv(df, caminho_saida)

    # Exibir as primeiras linhas do DataFrame
    print(df.head())


# Executar o script
if __name__ == "__main__":
    caminho_saida = "data/vendas_simuladas.csv"
    gerar_dataset(caminho_saida)