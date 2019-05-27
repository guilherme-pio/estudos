import pyodbc

lote = 1000 #Quantidade de buscas por consulta

#Cria conexão com o DB
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=SERVIDOR;"
                        "Database=DB_NAME;"
                        "Trusted_Connection=yes;")

#Query SQL que será executada para buscar os endereços
query = 'SELECT CPF, ENDERECO FROM ENDERECOS WHERE CPF IN ({0})'

#Lista de pessoas com CPFs distintos
lista_pes = list(str(x) for x in pd.unique(df['CPF'][0:2000]))

#Lista vazia onde serão inseridas as informações
lista_destino = []


#Cria os lotes das consultas, como um slicer. Ex: [0:1000] e assim vai até o tamanho total da base
for i in range(1, round(len(lista_pes) / lote) + 1): #lista_pes = lista com os cpfs que quero filtrar na consulta. Exemplo: [12345678901, 12345678902, ...]
    y = i * lote
    x = -lote
    x += y
    lotes = [(x, y)]
    
    #Itera pelos agrupamentos de slicers criados. Ex: [0:1000], [1000:2000]...
    for x, y in lotes:
        query_nova = query.format(', '.join('?' for _ in lista_pes[x:y])) #Insere ? de acordo com a quantidade fornecida nos lotes. Exemplo: SELECT * FROM TABELA WHERE CPF IN (?, ?, ?, ... 1000x)
        cursor = connection.cursor() #Cria cursor da conexão com o DB
        cursor.execute(query_nova, lista_pes[x:y]) #Executa a nova query trazendo apenas 1000 pessoas por vez 
        for row in cursor:
            lista_destino.append(row) #Insere na tabela os dados de CPF e ENDEREÇO

            
#Realiza o mesmo processo acima pro resto da base. Ex: se a minha lista_pes tiver 300.070 pessoas, o processo acima não pega as últimas 70 pessoas por causa do arredondamento. Logo esta parte final busca este restante.
final = [(lotes[0][-1], len(lista_pes))]
for x, y in final:
    query_nova = query.format(', '.join('?' for _ in lista_pes[x:y]))
    cursor = connection.cursor()
    cursor.execute(query_nova, lista_pes[x:y])
    for row in cursor:
        lista_destino.append(row)   
