from etl import ler_empresas_carregar_dados

ler_empresas_carregar_dados(
    pasta='data',
    format_saida=['parquet']
)