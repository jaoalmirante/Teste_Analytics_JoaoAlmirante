import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados(caminho_arquivo):
    """Carrega os dados de um arquivo CSV."""
    return pd.read_csv(caminho_arquivo)


def calcular_receita(df, coluna_quantidade, coluna_preco, coluna_receita):
    """Calcula a receita multiplicando quantidade pelo preço."""
    df[coluna_receita] = df[coluna_quantidade] * df[coluna_preco]
    return df


def limpar_e_processar_datas(df, coluna_data):
    """Converte a coluna de data para datetime e remove valores inválidos."""
    df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
    return df.dropna(subset=[coluna_data])


def remover_nulos(df, coluna):
    """Remove linhas com valores nulos em uma coluna específica."""
    return df[df[coluna].notnull()]


def adicionar_mes_ano(df, coluna_data, nova_coluna):
    """Adiciona uma coluna com o período no formato Mês/Ano."""
    df[nova_coluna] = df[coluna_data].dt.to_period('M').astype(str)
    return df


def calcular_tendencia_vendas(df, coluna_periodo, coluna_receita):
    """Calcula a tendência de vendas agrupando por período e somando a receita."""
    tendencia = df.groupby(coluna_periodo)[coluna_receita].sum().reset_index()
    tendencia[coluna_receita] = tendencia[coluna_receita].round(2)  # Formata para 2 casas decimais
    return tendencia


def salvar_dados(df, caminho_arquivo):
    """Salva o DataFrame em um arquivo CSV."""
    df.to_csv(caminho_arquivo, index=False)


def criar_grafico_tendencia(df, coluna_periodo, coluna_receita):
    """Cria um gráfico de linha mostrando a tendência de vendas ao longo do tempo."""
    plt.figure(figsize=(10, 6))
    plt.plot(df[coluna_periodo], df[coluna_receita], marker='o', linestyle='-', color='b')
    plt.title('Tendência de Vendas ao Longo do Tempo', fontsize=16)
    plt.xlabel('Período (Mês/Ano)', fontsize=12)
    plt.ylabel('Receita (em R$)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()


def processar_dados_vendas(caminho_entrada, caminho_saida):
    """Processa os dados de vendas, incluindo cálculo de receita e tendência."""
    # Carregar dados
    df = carregar_dados(caminho_entrada)

    # Calcular receita
    df = calcular_receita(df, coluna_quantidade='Quantidade', coluna_preco='Preço', coluna_receita='Receita')

    # Limpar e processar datas
    df = limpar_e_processar_datas(df, coluna_data='Data')

    # Remover valores nulos em colunas relevantes
    df = remover_nulos(df, coluna='Preço')

    # Adicionar coluna de mês/ano
    df = adicionar_mes_ano(df, coluna_data='Data', nova_coluna='MesAno')

    # Calcular tendência de vendas
    tendencia_vendas = calcular_tendencia_vendas(df, coluna_periodo='MesAno', coluna_receita='Receita')

    # Salvar resultados
    salvar_dados(tendencia_vendas, caminho_saida)

    # Criar gráfico de tendência
    criar_grafico_tendencia(tendencia_vendas, coluna_periodo='MesAno', coluna_receita='Receita')


# Executar o processamento
if __name__ == "__main__":
    caminho_entrada = "data/data_clean.csv"
    caminho_saida = "data/tendencia_vendas.csv"
    processar_dados_vendas(caminho_entrada, caminho_saida)