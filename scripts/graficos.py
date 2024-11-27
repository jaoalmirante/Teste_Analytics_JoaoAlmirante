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
    tendencia[coluna_receita] = tendencia[coluna_receita].round(2)
    return tendencia

def calcular_vendas_por_categoria(df, coluna_categoria, coluna_receita):
    """Calcula as vendas totais por categoria."""
    vendas_categoria = df.groupby(coluna_categoria)[coluna_receita].sum().reset_index()
    vendas_categoria[coluna_receita] = vendas_categoria[coluna_receita].round(2)
    return vendas_categoria

def produtos_mais_vendidos(df, coluna_produto, coluna_quantidade, top_n=5):
    """Retorna os produtos mais vendidos."""
    top_produtos = df.groupby(coluna_produto)[coluna_quantidade].sum().nlargest(top_n).reset_index()
    return top_produtos


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


def criar_grafico_vendas_por_categoria(df, coluna_categoria, coluna_receita):
    """Cria um gráfico de barras mostrando vendas por categoria."""
    plt.figure(figsize=(10, 6))
    plt.bar(df[coluna_categoria], df[coluna_receita], color='teal')
    plt.title('Vendas por Categoria', fontsize=16)
    plt.xlabel('Categoria', fontsize=12)
    plt.ylabel('Receita (em R$)', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()

def criar_grafico_top_produtos(df, coluna_produto, coluna_quantidade):
    """Cria um gráfico de barras para os produtos mais vendidos."""
    plt.figure(figsize=(10, 6))
    plt.barh(df[coluna_produto], df[coluna_quantidade], color='orange')
    plt.title('Top Produtos Mais Vendidos', fontsize=16)
    plt.xlabel('Quantidade Vendida', fontsize=12)
    plt.ylabel('Produto', fontsize=12)
    plt.gca().invert_yaxis()  # Inverte a ordem dos produtos para uma melhor visualização
    plt.tight_layout()
    plt.show()


def processar_dados_vendas(caminho_entrada, caminho_saida):
    """Processa os dados de vendas, incluindo cálculo de receita, tendência e análises adicionais."""
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

    # Análises adicionais
 # Análises adicionais
    vendas_categoria = calcular_vendas_por_categoria(df, coluna_categoria='Categoria', coluna_receita='Receita')
    top_produtos = produtos_mais_vendidos(df, coluna_produto='Produto', coluna_quantidade='Quantidade')

    # Criar gráficos
    criar_grafico_tendencia(tendencia_vendas, coluna_periodo='MesAno', coluna_receita='Receita')
    criar_grafico_vendas_por_categoria(vendas_categoria, coluna_categoria='Categoria', coluna_receita='Receita')
    criar_grafico_top_produtos(top_produtos, coluna_produto='Produto', coluna_quantidade='Quantidade')

# Executar o processamento
if __name__ == "__main__":
    caminho_entrada = "data/data_clean.csv"
    caminho_saida = "data/tendencia_vendas.csv"
    processar_dados_vendas(caminho_entrada, caminho_saida)
