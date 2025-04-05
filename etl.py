import pandas as pd
import os
import glob

def consolidar_csv(pasta='data'):
    """
    Lê todos os arquivos CSV na pasta especificada, consolida as informações
    em um único DataFrame e retorna o resultado.
    """
    # 1. Encontrar arquivos CSV na pasta
    arquivos_csv = glob.glob(os.path.join(pasta, '*.csv'))
    
    if not arquivos_csv:
        raise FileNotFoundError(f"Nenhum arquivo CSV encontrado na pasta '{pasta}'.")

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

if __name__ == "__main__":
    df_final = consolidar_csv()
    df_final