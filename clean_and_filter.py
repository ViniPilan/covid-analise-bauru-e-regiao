import pandas as pd
import numpy as np


def correcao(nome):
    if nome == 'AvarÃ©':
        return 'Avaré'
    elif nome == 'LenÃ§Ã³is Paulista':
        return 'Lençóis Paulista'
    elif nome == 'SÃ£o Manuel':
        return 'São Manuel'
    else:
        return nome
    

if __name__ == '__main__':
    
    cidades = ['Bauru', 'Botucatu', 'AvarÃ©', 'Lins', 'LenÃ§Ã³is Paulista', 'SÃ£o Manuel', 'Agudos', 'Barra Bonita', 'Itatinga']

    try:
        df = pd.read_csv('Dados/export.csv', encoding='utf-8')
        df = df.query('UF == "SP" and Município in @cidades').reset_index()
        df = df[['Município', 'Data', 'Casos Acumulados', 'Casos Novos', 'Óbitos Acumulados', 'Óbitos novos']]

        df['Casos Acumulados'] = df['Casos Acumulados'].astype(int)
        df['Casos Novos'] = df['Casos Novos'].astype(int)
        df['Óbitos Acumulados'] = df['Óbitos Acumulados'].astype(int)
        df['Óbitos novos'] = df['Óbitos novos'].astype(int)

        df['Município'] = df['Município'].apply(correcao) 

        df.to_csv('Dados/cidades.csv', encoding='utf-8', index=False)

        print('cidades.csv criado com sucesso...')

    except:
        print('Erro...')

    


