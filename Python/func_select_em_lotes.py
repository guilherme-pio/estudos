
import pyodbc

def select_in(query, connection, lista_pes, lista_destino, chunk=1000):
    """
    Utiliza uma como filtro para conseguir dados em outra lista.
    Parameters
    ----------
    query : str
    Query SQL com o parâmetro ' IN ({0}) para a variável que representa um filtro.
    Exemplo: 'SELECT NUM_PES FROM GDB2PRO.PESSOA WHERE NUM_PES IN ({0})
    connection : SQLAlchemy connectable(engine/connection), database string URI,
    or sqlite3 DBAPI2 connection
    Conexão ao DB.
    Exemplo: mb.con_work()
    lista_pes : list
    É a lista que contem a lista das variáveis a serem filtradas na query.
    Exemplo: lista contendo CPFs de pessoas
    lista_destino : list
    É o nome da lista que receberá os dados retornados da query.
    Geralmente é uma lista em branco.
    chunk : int, default: 1000
    É o tamanho dos lotes de buscas.
    """
    #Caso a base a ser filtrada possua menos de 1000 registros, cria-se uma query única, sem a necessidade de múltiplas consultas
    if len(lista_pes) < 1000:
        y = len(lista_pes)
        q = query.format(', '.join('?' for _ in lista_pes[:y]))
        cursor = connection.cursor()
        cursor.execute(q, lista_pes[:y])
        try:
            cursor.fetchone()[1]
            for row in cursor:
                lista_destino.append(row)
        except:
            for row in cursor:
                lista_destino.append(row[0])   
                
    else:
    #Cria querys de 1.000 em 1.000 itens para serem filtrados e appenda os resultados em uma lista vazia
        for i in range(1, round( len(lista_pes) / chunk) + 1):
            x = i * chunk
            y = -chunk
            y += x
            chunks = [(y, x)]

            for x, y in chunks:
                if y < len(lista_pes):
                    q = query.format(', '.join('?' for _ in lista_pes[x:y]))
                else:
                    q = query.format(', '.join('?' for _ in lista_pes[x:len(lista_pes)]))
                
                cursor = connection.cursor()
                
                try:
                    cursor.execute(q, lista_pes[x:y])
                except:
                    cursor.execute(q, lista_pes[x:len(lista_pes)])
                    
                try:
                    cursor.fetchone()[1]
                    for row in cursor:
                        lista_destino.append(row)
                except:
                    for row in cursor:
                        lista_destino.append(row[0])                    
                    
        #Como a consulta anterior cria de 1.000 em 1.000, esta verifica se faltaram itens no loop anterior e appenda o restante
        final = [(chunks[0][-1], len(lista_pes))]
        try:
            for x, y in final:
                q = query.format(', '.join('?' for _ in lista_pes[x:y]))
                cursor = connection.cursor()
                cursor.execute(q, lista_pes[x:y])
                
                try:
                    cursor.fetchone()[1]
                    for row in cursor:
                        lista_destino.append(row)
                except:
                    for row in cursor:
                        lista_destino.append(row[0])                     
        except:
            pass
