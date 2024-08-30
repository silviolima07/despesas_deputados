# config.py
from langchain_openai import ChatOpenAI
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

# Obter a chave da API OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
gpt4o = ChatOpenAI(model_name='gpt-4o')

# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llama3 = ChatGroq(
            api_key=GROQ_API_KEY,
            model= "lama-3.1-70b-versatile"   #"llama3-70b-8192"
        )
# Groq

client = Groq()
