# config.py
import os
from dotenv import load_dotenv

from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Groq

client = Groq()
