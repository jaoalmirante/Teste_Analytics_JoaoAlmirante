from criacao_dataset import gerar_dataset
from tratamento_dados import processar_dados
from graficos import processar_dados_vendas

def executar_pipeline():
    """
    Executa o pipeline completo:
    1. Gera dados simulados.
    2. Processa e limpa os dados.
    3. Analisa os dados e calcula tendências.
    """
    # Passo 1: Gerar dados simulados
    print("Gerando dados simulados...")
    caminho_dados_simulados = "vendas_simuladas.csv"
    gerar_dataset(caminho_dados_simulados)

    # Passo 2: Processar e limpar os dados
    print("Processando e limpando os dados...")
    caminho_dados_limpos = "data_clean.csv"
    processar_dados(caminho_dados_simulados, caminho_dados_limpos)

    # Passo 3: Analisar os dados e calcular tendências
    print("Analisando os dados e calculando tendências...")
    caminho_tendencia_vendas = "tendencia_vendas.csv"
    processar_dados_vendas(caminho_dados_limpos, caminho_tendencia_vendas)

    print("Pipeline concluído! Arquivos gerados:")
    print(f"- Dados simulados: {caminho_dados_simulados}")
    print(f"- Dados limpos: {caminho_dados_limpos}")
    print(f"- Tendência de vendas: {caminho_tendencia_vendas}")


# Executar o pipeline
if __name__ == "__main__":
    executar_pipeline()
