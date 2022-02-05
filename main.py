# importar pandas
import pandas as pd

# Variavel recebe a lista de meses
lista_meses = ['01-Janeiro','02-Fevereiro']

# For percorrendo cada arquivo
for mes in lista_meses:    
    tabela_horas = pd.read_excel(f'Arquivos/{mes}.xlsx')    
    
    for i in range(len(tabela_horas)):        
        if tabela_horas.iloc[i, 2] > 8:
            desenvolvedor = tabela_horas.iloc[i, 0]
            data_trabalhada = tabela_horas.iloc[i, 1]
            qtd_horas = tabela_horas.iloc[i, 2]
            print(f'Data: {data_trabalhada} Horas: {qtd_horas}')