# importar pandas
import pandas as pd

# Variavel recebe a lista de meses
lista_meses = ['01-Janeiro','02-Fevereiro','03-Março','04-Abril','05-Maio','06-Junho']

# For percorrendo cada arquivo
for mes in lista_meses:    
    tabela_horas = pd.read_excel(f'Arquivos/{mes}.xlsx') 
    # Variavel para contar as horas do mes   
    total_hora_mes = 0
    
    # For percorre cada linha
    for i in range(len(tabela_horas)):   

        # Verifica se a linha da hora é maior que 8
        if tabela_horas.iloc[i, 2] > 8:

            # Alimenta as variavies
            desenvolvedor = tabela_horas.iloc[i, 0]
            data_trabalhada = tabela_horas.iloc[i, 1].strftime('%d/%m/%Y')
            qtd_horas = tabela_horas.iloc[i, 2]-8            

            total_hora_mes = total_hora_mes+qtd_horas            

            # Output Desenvolver, data e quantidade de horas extras
            print(f'Desenvolvedor: {desenvolvedor} | Data: {data_trabalhada} | Horas Extras: {qtd_horas}')
                
    # Condição para exibir a descrição do mês
    if mes[0:2] == '01':
        descricao_mes = 'Janeiro'
    elif mes[0:2] == '02':
        descricao_mes = 'Fevereiro'
    elif mes[0:2] == '03':
        descricao_mes = 'Março'
    elif mes[0:2] == '04':
        descricao_mes = 'Abril'
    elif mes[0:2] == '05':
        descricao_mes = 'Maio'
    elif mes[0:2] == '06':
        descricao_mes = 'Junho'                

    # Output total de horas no mês
    if total_hora_mes > 0:
        print(f'Total de Horas no mês de {descricao_mes}: {total_hora_mes} \n')
    else:
        print(f'Não foi feitas horas extras para o mês de {descricao_mes} \n')

    