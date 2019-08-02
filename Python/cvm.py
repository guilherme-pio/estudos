import pandas as pd
import requests

#Traz um registro qualquer para obter os nomes das colunas
teste = requests.get('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_201906.csv').content.decode('utf-8')

#cria um df
df = pd.read_table(pd.compat.StringIO(teste),sep=';')

#limpa a tabela e mantem as colunas
df.drop(df.index, inplace=True)

#Cria uma lista com os anos. No site da CVM dizia que só tinha até 2017
anos = [str(ano) for ano in range(2017,2020)]

#Cria lista vazia de meses
meses = []

#Cria lista dos meses em str com 0 antes
for mes in range(1,13):
    if len(str(mes)) == 1:
        mes = '0' + str(mes)
        meses.append(mes)
    else:
        meses.append(str(mes))
        

#Faz as requisições e appenda no df
for ano in anos:
    for mes in meses:
        try:
            req = requests.get('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_' + ano + mes + '.csv').content.decode('utf-8')
            df_req = pd.read_table(pd.compat.StringIO(req),sep=';')
            df = df.append(df_req)
        except:
            pass
            
 #A partir daí vc exporta ou insere num db...
