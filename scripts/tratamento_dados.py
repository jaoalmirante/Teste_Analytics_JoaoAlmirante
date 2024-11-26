import pandas as pd
from translate import Translator
from word2number import w2n


def carregar_dados(caminho_arquivo):
    """Carrega os dados do arquivo CSV."""
    return pd.read_csv(caminho_arquivo)


def interpolar_valores_nulos(df, coluna, metodo='linear'):
    """Realiza interpolação para valores nulos de uma coluna específica."""
    df[coluna].interpolate(method=metodo, inplace=True)
    return df


def traduzir_coluna(df, coluna, idioma_origem='pt', idioma_destino='en'):
    """Traduz os valores de uma coluna usando a biblioteca Translator."""
    translator = Translator(to_lang=idioma_destino, from_lang=idioma_origem)
    df[coluna] = df[coluna].apply(lambda x: translator.translate(x))
    df[coluna] = df[coluna].apply(lambda x: 'seven' if x == 'sete' else x)
    return df


def converter_texto_para_numero(df, coluna):
    """Converte valores textuais em uma coluna para números."""
    def convert_number(value):
        try:
            return w2n.word_to_num(value)
        except:
            try:
                return int(value)
            except:
                return None

    df[coluna] = df[coluna].apply(convert_number)
    return df


def filtrar_por_data(df, coluna_data, inicio, fim):
    """Filtra o DataFrame para incluir apenas os registros dentro de um intervalo de datas."""
    df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
    df = df.dropna(subset=[coluna_data])  # Remove linhas com datas inválidas
    return df[(df[coluna_data] >= inicio) & (df[coluna_data] <= fim)]


def salvar_dados(df, caminho_arquivo):
    """Salva o DataFrame em um arquivo CSV."""
    df.to_csv(caminho_arquivo, index=False)


def processar_dados(caminho_entrada, caminho_saida):
    """Processa os dados, aplicando todas as transformações necessárias."""
    # Carregar dados
    df = carregar_dados(caminho_entrada)

    # Interpolar valores nulos na coluna 'Preço'
    df = interpolar_valores_nulos(df, coluna='Preço')

    # Traduzir e converter valores da coluna 'Quantidade'
    df = traduzir_coluna(df, coluna='Quantidade')
    df = converter_texto_para_numero(df, coluna='Quantidade')

    # Filtrar dados por data e valores nulos na coluna 'Preço'
    df = df[df['Preço'].notnull()]
    df_filtrado = filtrar_por_data(df, coluna_data='Data', inicio="2023-01-01", fim="2023-12-31")

    # Salvar dados processados
    salvar_dados(df_filtrado, caminho_saida)


# Executar o processamento
if __name__ == "__main__":
    caminho_entrada = "data/vendas_simuladas.csv"
    caminho_saida = "data/data_clean.csv"
    processar_dados(caminho_entrada, caminho_saida)