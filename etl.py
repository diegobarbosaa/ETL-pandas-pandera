import pandas as pd
import os
import glob

def consolidar_csv(path: str) -> pd.DataFrame:
    """
    Lê todos os arquivos CSV na pasta especificada, consolida as informações
    em um único DataFrame e retorna o resultado.
    """
    # 1. Encontrar arquivos CSV na pasta
    arquivos_csv = glob.glob(os.path.join(path, '*.csv'))
    
    if not arquivos_csv:
        raise FileNotFoundError(f"Nenhum arquivo CSV encontrado na pasta '{path}'.")

    # 2. Ler todos os CSVs
    colunas = [
        "CNPJ_BASICO",
        "RAZAO_SOCIAL_NOME_EMPRESARIAL",
        "NATUREZA_JURIDICA",
        "QUALIFICACAO_DO_RESPONSAVEL",
        "CAPITAL_SOCIAL",
        "PORTE_DA_EMPRESA",
        "ENTE_FEDERATIVO_RESPONSAVEL"
    ]

    dataframes = [
        pd.read_csv(
            arquivo,
            sep=';',
            encoding='latin1',
            names=colunas
        )
        for arquivo in arquivos_csv
    ]

    # 3. Concatenar os DataFrames
    df_consolidado = pd.concat(dataframes, ignore_index=True)
    
    return df_consolidado


def carregar_dados(df: pd.DataFrame, formatos_saida: list):
    """
    Carregar o DataFrame em diferentes formatos de arquivo.
    """
    if 'csv' in formatos_saida:
        df.to_csv('dados_consolidados_empresas.csv', index=False)
    if 'parquet' in formatos_saida:
        df.to_parquet('dados_consolidados_empresas.parquet', index=False)
    if 'json' in formatos_saida:
        df.to_json('dados_consolidados_empresas.json', orient='records')
    if 'xlsx' in formatos_saida:
        df.to_excel('dados_consolidados_empresas.xlsx', index=False)

if __name__ == "__main__":
    pasta='data'
    df_consolidado = consolidar_csv(path=pasta)
    format_saida: list = ['json']
    carregar_dados(df_consolidado, format_saida)
    print(f"Dados consolidados e salvos em {format_saida}.")