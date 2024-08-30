import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from numerize import numerize


html_page_title = """
     <div style="background-color:black;padding=50px">
         <p style='text-align:center;font-size:45px;font-weight:bold'>Câmara dos Deputados</p>
     </div>
               """               
st.markdown(html_page_title, unsafe_allow_html=True)

df = pd.read_csv("df_partido.csv")

df.sort_values('Valor (R$)',inplace=True)

total_gasto = df['Valor (R$)'].sum()
total_gasto2 = numerize.numerize(total_gasto)

st.markdown("## Relatório de Despesas")
st.markdown("### Fonte: https://dadosabertos.camara.leg.br/")

st.sidebar.markdown("### Menu")
option = st.sidebar.selectbox("Menu", ["Analises", 'About'], label_visibility='hidden')
    
if option == 'Analises':
    st.markdown("# Análises")
    st.subheader(f'Total de gastos declarados: R${total_gasto2}')
    st.subheader(f'Periodo: de janeiro até mês atual')
    st.markdown('##### Data de extração via API: 27/08/2024')

    # Transformação de 'Valor (R$)' em 'Valor'
    df['Valor'] = df['Valor (R$)'].apply(numerize.numerize)

    # Adicionando estilo CSS
    html = df.to_html(index=False, classes='table table-striped')

    # Exibindo com Streamlit
    st.markdown("""
    <style>
        .table {
            width: 100%;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)



    st.markdown("# Despesas declaradas por partidos")
    st.markdown("#### K = Mil / M = Milhoes / B = Bilhoes")

    st.markdown(html, unsafe_allow_html=True)


    #graph_type1 = st.selectbox("Choose the graph type", ["Bar", "Pie"])
    fig1, ax1 = plt.subplots(figsize=(15,10))



    #if graph_type1 == "Bar":

    ax1.barh(df['partido'], df['Valor'], color='red')
    ax1.set_xlabel("Valor", fontsize=20)
    ax1.set_ylabel("Partido", fontsize=24)
    ax1.set_title("\nPartidos x Despesa\n", fontsize=22)
    ax1.tick_params(axis='x', labelsize=18)  # Tamanho das fontes dos ticks do eixo x
    ax1.tick_params(axis='y', labelsize=18)  # Tamanho das fontes dos ticks do eixo y
    ax1.set_xticks(ax1.get_xticks()) 
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=18)
   
    plt.tight_layout()
    st.pyplot(fig1)

    st.write(" ") 
    st.write(" ")     
   

    import matplotlib.pyplot as plt

    # Supondo que você já tenha um DataFrame df com as colunas 'Valor (R$)' e 'partido'
    # Filtrando os top 10 partidos com maior valor de despesa
    top_10 = df.nlargest(10, "Valor (R$)")

    # Configurando o gráfico de pizza
    fig2, ax2 = plt.subplots(figsize=(20, 10))

    # Criando o gráfico de pizza com labels maiores e explosão da maior fatia
    wedges, texts, autotexts = ax2.pie(
        top_10["Valor (R$)"], 
        labels=top_10["partido"], 
        explode=[0.1 if i == 0 else 0 for i in range(len(top_10))], 
        autopct='%1.1f%%', 
        startangle=90,
        textprops={'fontsize': 16}  # Tamanho dos labels
    )

    # Aumentando o tamanho dos labels manualmente
    for text in texts:
        text.set_fontsize(18)  # Tamanho dos labels

    # Aumentando o tamanho dos percentuais manualmente
    for autotext in autotexts:
        autotext.set_fontsize(18)  # Tamanho dos percentuais

    # Configurando o título do gráfico
    ax2.set_title("Top 10 Partidos x Despesa", fontsize=22)

    # Exibindo o gráfico
    st.pyplot(fig2)

    ############################################################
      
    st.markdown("# Top 10 Despesas: Deputados")

    df = pd.read_csv('top10_dep.csv')
    df.sort_values('Valor (R$)',inplace=True)

    # Transformação de 'Valor (R$)' em 'Valor'
    df['Valor'] = df['Valor (R$)'].apply(numerize.numerize)

    # Adicionando estilo CSS
    html2 = df.to_html(index=False, classes='table table-striped')

    # Exibindo com Streamlit
    st.markdown("""
    <style>
        .table {
            width: 100%;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(html2, unsafe_allow_html=True)



    #graph_dep = st.selectbox("Choose the graph type", ["Bar", "Pie"])
    fig1, ax1 = plt.subplots(figsize=(15,10))


    #if graph_dep == "Bar":
    ax1.barh(df['nome'], df['Valor'], color='red')
    ax1.set_xlabel("Valor", fontsize=20)
    ax1.set_ylabel("Deputado", fontsize=24)
    ax1.set_title("\nTop 10 Deputados x Despesa\n", fontsize=22)
    ax1.tick_params(axis='x', labelsize=18)  # Tamanho das fontes dos ticks do eixo x
    ax1.tick_params(axis='y', labelsize=18)  # Tamanho das fontes dos ticks do eixo y

    ax1.set_xticks(ax1.get_xticks()) 
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=18)
    st.pyplot(fig1)

    st.write(" ") 
    st.write(" ") 
    
    #elif graph_dep == "Pie":

    import matplotlib.pyplot as plt

    # Supondo que você já tenha um DataFrame df com as colunas 'Valor (R$)' e 'nome'
    # Filtrando os top 10 partidos com maior valor de despesa
    top_10 = df.nlargest(10, "Valor (R$)")

    # Configurando o gráfico de pizza
    fig2, ax2 = plt.subplots(figsize=(20, 10))

    # Criando o gráfico de pizza com labels maiores e explosão da maior fatia
    wedges, texts, autotexts = ax2.pie(
        top_10["Valor (R$)"], 
        labels=top_10["nome"], 
        explode=[0.1 if i == 0 else 0 for i in range(len(top_10))], 
        autopct='%1.1f%%', 
        startangle=90,
        textprops={'fontsize': 16}  # Tamanho dos labels
    )

    # Aumentando o tamanho dos labels manualmente
    for text in texts:
        text.set_fontsize(18)  # Tamanho dos labels

    # Aumentando o tamanho dos percentuais manualmente
    for autotext in autotexts:
        autotext.set_fontsize(18)  # Tamanho dos percentuais

    # Configurando o título do gráfico
    ax2.set_title("\n\nTop 10 Deputados x Despesa\n", fontsize=22)

    # Exibindo o gráfico
    st.pyplot(fig2)

    ################################################################
    st.write(" ") 
    st.write(" ")

    st.markdown("# Checar despesas de Deputado")

    df = pd.read_csv("dep.csv")

    lista_dep = df['nome'].unique()
    st.markdown("### Selecione um Deputado")
    nome_dep = st.selectbox("Selecione um deputado", lista_dep, label_visibility='hidden')

    if st.button('Enviar'):
    
        temp_desp = df.loc[df.nome == nome_dep].reset_index()
        partido = temp_desp.partido.astype('string')
        total_gasto = temp_desp['Valor (R$)'].sum()
        total_gasto = numerize.numerize(total_gasto)
    
        st.subheader("Deputado: "+nome_dep)
        st.subheader("Partido: "+partido[0])
        st.subheader(f'Total de gastos declarados: R${total_gasto}')
    
    
        temp_desp = temp_desp.groupby(['Tipo_despesa', 'Data', 'Fornecedor'])['Valor (R$)'].sum().reset_index().sort_values(by='Valor (R$)')
        #temp_desp = temp_desp[['Tipo_despesa', 'Data', 'Fornecedor', 'Valor (R$)']]
        # Adicionando estilo CSS
        html3 = temp_desp.to_html(index=False, classes='table table-striped')

        # Exibindo com Streamlit
        st.markdown("""
        <style>
            .table {
                width: 100%;
                font-size: 18px;
            }
        </style>
        """, unsafe_allow_html=True)
        st.markdown(html3, unsafe_allow_html=True)
    
        # Agrupamento por Fornecedor
        temp_forn = temp_desp.groupby('Fornecedor')['Valor (R$)'].sum().reset_index().sort_values(by='Valor (R$)')
        fig3, ax3 = plt.subplots(figsize=(20,10))

        #if graph_dep == "Bar":
        ax3.barh(temp_forn['Fornecedor'], temp_forn['Valor (R$)'], color='red')
        ax3.set_xlabel("Valor (R$)", fontsize=20)
        ax3.set_ylabel("Fornecedor", fontsize=24)
        ax3.set_title("\nGasto por Fornecedor\n", fontsize=22)
        ax3.tick_params(axis='x', labelsize=18)  # Tamanho das fontes dos ticks do eixo x
        ax3.tick_params(axis='y', labelsize=18)  # Tamanho das fontes dos ticks do eixo y

        st.pyplot(fig3)

        st.write(" ") 
        st.write(" ") 
    
if option == 'About':
    st.markdown("# About:")
    st.markdown("### Este projeto apresenta dados de despesas declaradas por partidos e deputados da Câmara de Deputados do Brasil.")
    st.markdown("### Dados obtidos através de APIs disponibilizados no site da câmara.")
    st.markdown("### Um modelo llama acessado via Groq, escreveu o código Python com Streamlit.")   
    st.markdown("### Github: https://github.com/silviolima07/despesas_deputados")    
    
    
    
    


