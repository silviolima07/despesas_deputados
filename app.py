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
total_gasto = numerize.numerize(total_gasto)

st.markdown("## Relatório de Despesas")
st.markdown("### Fonte: https://dadosabertos.camara.leg.br/")

st.subheader(f'Total de gastos declarados: R${total_gasto}')
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


