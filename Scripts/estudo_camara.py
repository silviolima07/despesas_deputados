from config import client # lib config has lib Grog

from tools_dep import  merge_data # tool_dep all API to bring data
import pandas as pd

def list_to_string(lst):
    # Convert each item to string before joining
    return ', '.join([str(item) for item in lst]) 

def save_report_to_markdown(content, filename="report.md"):
    with open(filename, 'w',  encoding='utf-8') as f:
        f.write(content)
        print("Arquivo report.md salvo")
              
def save_plot_code(content, filename):
    # Remove linhas que começam com ```
    filtered_content = '\n'.join([line for line in content.splitlines() if not line.startswith('```')])

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(filtered_content)
        print(f"Arquivo {filename} salvo")

df = merge_data()

print("Dataset lido")
# Contar quantos deputados/nome cada partido possue.
temp = df[['partido', 'nome']]

# Agrupar por deputado - 511 - apenas 10 maiores
df_partido = df.groupby(['partido'])['Valor (R$)'].sum().reset_index()
dF_partido = df_partido.sort_values(by='Valor (R$)', ascending=False)

# Criar contexto para ser inserido na questao
partes_partido = df_partido.columns.str.split(',')


llm = client # Groq
MODEL= "llama-3.1-8b-instant"

pagamentos_efetuados_partidos = [f"{list_to_string(partes_partido[0])}:{list_to_string(registro[partes_partido[0]])}, {list_to_string(partes_partido[1])}:{list_to_string(registro[partes_partido[1]])}" for _, registro in df_partido.iterrows()]

# Prompts
questao_partidos = """
Ignore any previous datasets used and code created.
Follow this instructions only.
Write Python code to create a dashboard using Streamlit that includes bar and pie graphs 
from the provided dataset. Do all import needs to run the code. 
Use st.selectbox to choose the graph type. 
All graphs must use font size of 16. Bar graph must be plotted in horizontal. 
Shoud include y-axis with parties names and 'Valor (R$)' in x=axis. 
All axis labels must use font size of 16, graphs must have a figure size of (20,10). 
The pie chart must have options labels and explode Pie graph must show top 10 expenses 
and use field 'Valor (R$)' to select the expenses. Title of pie graph must be 'Top 10 Despesas por partido'. 
Title of bar graph must be 'Valor (R$) x Partido'. 
Ensure that only Python commands are saved, and no comments should appear at the end of the file. 
Nothing be included after the line that starts with 'st.pyplot'."
Only Python commands and statements must be present in response.
Use columns 'partido', 'Valor (R$)'.    
"""


def generate_decision(questao, despesas):
    input_text = f"Questao: {questao}\n\nPagamentos:{' '.join(despesas)}"

    print("Input_text:", input_text)
  
    result = llm.chat.completions.create(
    messages=[
      {"role": "system", 
       "content": "You are a Senior Data Scientist with extensive experience in data analysis and visualization"
       },
      {"role": "user", 
       "content": input_text,
       }
    ],
    model=MODEL,
  )
  
    return result.choices[0].message.content

response_partido = generate_decision(questao_partidos, pagamentos_efetuados_partidos)

#print(response_top10_dep)

# Salvar o relatório em markdown
save_report_to_markdown(response_partido)


# Salvar plot code
save_plot_code(response_partido, 'questao_partido.py')

input_filename  = 'questao_partido.py'
output_filename = 'questao_partido.py'
 
  
  