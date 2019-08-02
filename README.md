# Meus estudos

Códigos criados por mim durante estudos ou durante o desenvolvimento de alguns trabalhos.

## Python

Funções e scripts Python voltados principalmente para manipulação de dados e Data Science.

* ### [select in](https://github.com/guilherme-pio/estudos/blob/master/Python/select_in.py)
Função que faz vários SELECTs em lotes para retornar dados filtrados.

Exemplo: num arquivo excel existem milhares de CPFs de clientes. É necessário consultar informações cadastrais destes clientes no banco de dados. Para realizar a consulta, criei esta função que cria várias querys em lotes para gerar vários selects e appenda os resultados numa tabela vazia.

```
#Query do banco de dados onde estão as informações a serem buscadas. No exemplo, informações de clientes.
query = 'SELECT CPF, NOME, DTA_NASCIMENTO, SEXO FROM dbo.CLIENTES WHERE CPF IN ({0)}'

#Driver de conexão ao DB
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=test;DATABASE=test;UID=user;PWD=password')

#Lista com os itens a serem filtrados na query. No caso, há três CPFs para exemplo, porém espera-se milhares de itens.
lista_pes = ['12345678911', '11122233345', '98765432112']

#Lista vazia que receberá os dados do SELECT.
lista_destino = []

#Quantidade de itens da lista_pes por query.
chunk = 1000

select_in(query, connection, lista_pes, lista_destino, chunk=1000)
```

Neste caso, após rodar a função, a lista destino receberá tuplas com os dados de CPF, nome, data de nascimento e sexo.

```
lista_destino =   [('12345678911', 'ANOTONIO DA SILVA', '1960-01-01', 'MASCULINO'),
                  ('11122233345', 'MARIA JOSÉ', '1950-06-02', 'FEMININO'),
                  ('98765432112', 'REGIS TADEU', '1955-03-25', 'MASCULINO')]
```

* ### [Dados Comissão de Valores Mobiliários](https://github.com/guilherme-pio/estudos/blob/master/Python/cvm.py)

Busca dados históricos de fundos da CVM.
