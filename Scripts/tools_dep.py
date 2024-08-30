import requests
import pandas as pd
import time

def get_id(nome):
    """get id of a deputy from his name

    Args:
        nome : nome do deputado

    Returns:
        id : id do deputado
    """
    nome = nome.replace(" ", "_")
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?nome={}".format(nome)
    print("URL para obter ID:", url)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    print("\nResponse:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        if data['dados']:  # Verifica se a lista de 'dados' não está vazia
            id = data['dados'][0]['id']
            return id
        else:
            print("Nenhum deputado encontrado com o nome fornecido.")
            return None
    else:
        print("Erro ao acessar a API:", response.status_code)
        return None

def get_deputados():
    """ Lista de deputados na atual legislatura

    Returns:
        lista: lista de deputados
    """
    
    lista_id = []
    lista_nome = []
    lista_partido = []
    lista_uf = []
    lista_email = []
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
    #print("URL lista:", url)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    #print("\nResponse:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        total = len(data['dados'])
        print("Total de deputados:", total)
        if data['dados']:  # Verifica se a lista de 'dados' não está vazia
            print("Coletando dados de deputados...")
            n=1
            for descricao in data['dados']:
                id = descricao.get('id', 'N/A')
                lista_id.append(id)
                nome = descricao.get('nome', 'N/A')
                lista_nome.append(nome)
                siglaPartido = descricao.get('siglaPartido', 'N/A')
                lista_partido.append(siglaPartido)
                siglaUf = descricao.get('siglaUf', 'N/A')
                lista_uf.append(siglaUf)
                email = descricao.get('email', 'N/A')
                lista_email.append(email)
                
                """
                print(n," of ", total )
                print(f"id: {id}")
                print(f"Nome do Deputado: {nome}")
                print(f"Sigla do partido: {siglaPartido}")
                print(f"Sigla da UF: {siglaUf}")
                print(f"E-mail: {email}") 
                n+=1 
                print("-" * 40)
                """
                
            if lista_id:
                data = {'id':lista_id,
                        'nome': lista_nome,
                        'partido': lista_partido,
                        'uf':lista_uf,
                        'email': lista_email}
                df_dep = pd.DataFrame(data)
                #print(df_dep)
    
                df_dep.to_csv('df_dep.csv', index=False)  
                print("Created dataframe df_dep.csv")  
            
    
        else:
            print("Nenhuma informacao encontrada.")
    else:
        print("Erro ao acessar a API:", response.status_code)
    

def get_desp_dep(id_deputado):
    url = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas"
    print("URL para obter despesas:", url)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    
    lista_tipo_desp = []
    lista_data_doc= []
    lista_nome_for = []
    lista_valor_doc = []
    
    if response.status_code == 200:
        data = response.json()
        if data['dados']:  # Verifica se a lista de 'dados' não está vazia
            print("Coletando dados de deputados...")
            for despesa in data['dados']:
                tipo_despesa = despesa.get('tipoDespesa', 'N/A')
                lista_tipo_desp.append(tipo_despesa)
                data_documento = despesa.get('dataDocumento', 'N/A')
                lista_data_doc.append(data_documento)
                nome_fornecedor = despesa.get('nomeFornecedor', 'N/A')
                lista_nome_for.append(nome_fornecedor)
                valor_documento = despesa.get('valorDocumento', 'N/A')
                lista_valor_doc.append(valor_documento)
                
                print(f"Tipo de Despesa: {tipo_despesa}")
                print(f"Data do Documento: {data_documento}")
                print(f"Nome do Fornecedor: {nome_fornecedor}")
                print(f"Valor do Documento: R${valor_documento:.2f}")
                print("-" * 40)
            return lista_tipo_desp, lista_data_doc, lista_nome_for, lista_valor_doc  
        else:
            print("Nenhuma despesa encontrada para o deputado com o ID fornecido.")
    else:
        print("Erro ao acessar a API:", response.status_code)
        
        

def get_all_desp():
    #url = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas"
    #print("URL para obter despesas:", url)
    
    temp = pd.DataFrame()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    df = pd.read_csv('df_dep.csv')
    
    total = len(df['id'])
    n = 1
    
    for index, row in df.iterrows():
        
        url = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{row['id']}/despesas"
        
        response = requests.get(url, headers=headers)
        
        time.sleep(1)
        lista_id = []
        lista_tipo_desp = []
        lista_data_doc= []
        lista_nome_for = []
        lista_valor_doc = []
    
        if response.status_code == 200:
            data = response.json()
            if data['dados']:  # Verifica se a lista de 'dados' não está vazia
                
                print(n,'of', total)
                print("Deputado:", row['nome'])
                for despesa in data['dados']:
                    tipo_despesa = despesa.get('tipoDespesa', 'N/A')
                    lista_tipo_desp.append(tipo_despesa)
                    data_documento = despesa.get('dataDocumento', 'N/A')
                    lista_data_doc.append(data_documento)
                    nome_fornecedor = despesa.get('nomeFornecedor', 'N/A')
                    lista_nome_for.append(nome_fornecedor)
                    valor_documento = despesa.get('valorDocumento', 'N/A')
                    lista_valor_doc.append(valor_documento)
                    
                    lista_id.append(row['id'])
                    
                   # print(f"Tipo de Despesa: {tipo_despesa}")
                   # print(f"Data do Documento: {data_documento}")
                   # print(f"Nome do Fornecedor: {nome_fornecedor}")
                   # print(f"Valor do Documento: R${valor_documento:.2f}")
                    #print("-" * 40)
                
                if tipo_despesa:
                    data = {'id':lista_id,
                        'Tipo_despesa': lista_tipo_desp,
                        'Data': lista_data_doc,
                        'Fornecedor':lista_nome_for,
                        'Valor (R$)': lista_valor_doc}
                
                    df_desp = pd.DataFrame(data)
                    temp = pd.concat([temp, df_desp])
                    
    
                    #df_desp.to_csv('df_desp.csv', index=False)  
                    #print("Created dataframe df_desp.csv")      
                  
            else:
                print("Nenhuma despesa encontrada para o deputado com o ID fornecido.")
        else:
            print("Erro ao acessar a API:", response.status_code)
        
        n+=1
    
    temp.to_csv('df_desp.csv', index=False)
    print("Created dataframe df_desp.csv")

def merge_data():
    df1 = pd.read_csv('df_desp.csv')
    df1['id'] = df1['id'].astype('Int64')
    #print('\ndespesas:',df1.shape)
    #print(df1.columns)

    df2 = pd.read_csv('df_dep.csv')
    df2['id'] = df2['id'].astype('Int64')
    #print('deputados:',df2.shape)
    #print(df2.columns)

    df = pd.merge(df1, df2, on='id')
    #print('\ndf:', df.shape)
    df.to_csv('dep.csv', index=False)
    #print(df.head())
    #print('dep.csv:', df.columns)

    
    return df

#get_deputados()

#get_all_desp()

# merge_data()





