import streamlit as st
import json
import google.generativeai as genai

# Configuração da API do Google (Insira sua API Key do Google AI Studio)
genai.configure(api_key="COLE_SUA_API_KEY_AQUI")
model = genai.GenerativeModel('gemini-pro')

st.title("TechMentor 🚀 - Seu Conselheiro de Carreira em TI")
st.write("Pergunte-me sobre trilhas de estudo ou dicas para entrevistas!")

# Carregando a Base de Conhecimento (simulando a leitura do JSON)
conhecimento = {
  "carreiras": {
    "Front-end": "HTML, CSS, JavaScript, React.",
    "Back-end": "Python, Java, C#, SQL.",
    "Dados": "Python, Pandas, SQL, Machine Learning."
  }
}

# Prompt de Sistema
prompt_sistema = f"""
Você é o TechMentor, um orientador de carreira em TI. Baseie suas respostas nesta base de conhecimento: {json.dumps(conhecimento)}.
Seja motivador e conciso. Não responda sobre temas fora de tecnologia.
"""

user_input = st.text_input("Qual é a sua dúvida de carreira?")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Pensando..."):
            prompt_completo = f"{prompt_sistema}\n\nDúvida do usuário: {user_input}"
            response = model.generate_content(prompt_completo)
            st.write(response.text)
