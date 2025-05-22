# -*- coding: utf-8 -*-
"""
Study Project: Summarize texts, articles, and physical and digital notes
Created by: Victor Sampaio

"""

# *****************************************************************************
# IMPORTS LIBRARY, SDKs, ADK AND FRAMEWORKS
# *****************************************************************************
import streamlit as st
from google import genai
import os
import tempfile
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # For create (Content e Part)
import textwrap # For format output text
import requests # For HTTP requests
import warnings
import PyPDF2 as pdf # For read PDF

warnings.filterwarnings("ignore")

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************

# Function for call AI Agents for utilize Runner for take prompt and get response (UTILIZAR PARA FAZER O QUIS)
def call_agent(agent: Agent, message_text: str) -> str:
    # Create service session in memory
    session_service = InMemorySessionService()
    # Create a new session (you can personalize IDs)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Create a Runner (Agent) for set prompt and get response
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Create a message content
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""

    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

# Function for read PDF in Python with PyPDF2
def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = pdf.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error ao ler PDF: {e}")
        return None

# Function for process PDF in API Google Gemini for execute especific prompt
def process_pdf_with_gemini(file_path, prompt):
    pdf_text = read_pdf(file_path)
    if pdf_text:
        # Combine the PDF content and the user's prompt
        full_prompt = f"Aqui está o conteúdo do PDF:\n\n{pdf_text}\n\n{prompt}"
        try:
            # Use the existing clientSDK and MODEL_ID
            response = clientSDK.models.generate_content(
                model=MODEL_ID,
                contents=full_prompt
            )
            return response.text
        except Exception as e:
            st.markdown(f"Error ao gerar o conteúdo: {e}")
            return None
    else:
        return None

# *****************************************************************************
# GOOGLE API KEY
# *****************************************************************************

try:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Erro: A chave da API do Gemini (GOOGLE_API_KEY) não foi encontrada nos segredos do Streamlit.")
    st.stop()

# Create Client SDK
clientSDK = genai.Client()

# Define Gemini Model will be used
MODEL_ID = "gemini-2.0-flash"

# *****************************************************************************
# PROMPTS
# *****************************************************************************

few_shot_prompt_sumarize="""
    **Contexto e Objetivo:**
Você é um **analista e sintetizador de documentos altamente qualificado**, com expertise no assunto do arquivo PDF fornecido.
Sua principal missão é processar este documento para gerar um **resumo detalhado e de fácil compreensão**, mantendo a fidelidade
ao conteúdo original.

**Instruções de Processamento Detalhadas:**
1.  **Leitura Integral e Profunda:** Leia o arquivo PDF na sua totalidade, com atenção meticulosa a cada linha, parágrafo, seção e capítulo.
Assegure-se de compreender plenamente a estrutura, o fluxo de argumentos e as nuances do texto.

2.  **Extração de Informações Essenciais:** Durante a leitura, identifique e extraia:
    * **Tópicos Principais:** As ideias centrais de cada seção ou capítulo.
    * **Conceitos-Chave:** Definições importantes, terminologias específicas e suas explicações.
    * **Argumentos e Evidências:** As principais teses apresentadas e os dados ou raciocínios que as sustentam.
    * **Exemplos Cruciais:** Ilustrações, estudos de caso ou cenários que ajudam a clarear os conceitos.
    * **Conclusões e Recomendações:** Os pontos finais e as implicações do conteúdo.

3.  **Elaboração do Resumo Detalhado:**
    * Organize as informações extraídas de forma lógica e hierárquica, refletindo a estrutura do PDF.
    * Para cada ponto relevante, forneça uma **explicação clara e concisa**, utilizando uma linguagem simples e acessível,
    como se estivesse explicando o conteúdo a um público não especialista.
    * **Mantenha o Contexto:** É crucial que a simplificação não comprometa o contexto original ou a profundidade das informações.
    * **Inclua Exemplos Relevantes:** Incorpore os exemplos mais importantes para ilustrar os conceitos e facilitar a compreensão.
    * **Evite Perdas:** Tenha extremo cuidado para não omitir informações críticas, detalhes importantes ou nuances significativas
    do documento original.

4.  **Formato de Saída:**
    Apresente o resumo utilizando a seguinte estrutura em Markdown, preenchendo as seções com o conteúdo extraído:

```markdown
### Resumo Detalhado do Documento: [Título do PDF, se disponível, ou "Documento Fornecido"]

**1. Introdução e Contexto Geral:**
[Breve parágrafo contextualizando o documento, seu propósito e o que ele aborda.]

**2. Principais Seções/Capítulos e Tópicos Abordados:**

* **[Título da Seção/Capítulo 1]:**
    * **Conceito/Ponto 1.1:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]
    * **Conceito/Ponto 1.2:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]
    * ... (Adicionar mais pontos conforme necessário)

* **[Título da Seção/Capítulo 2]:**
    * **Conceito/Ponto 2.1:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]
    * **Conceito/Ponto 2.2:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]
    * ... (Adicionar mais pontos conforme necessário)

* ... (Continuar para todas as seções/capítulos relevantes do PDF)

**3. Conclusões Principais e Implicações:**
[Um parágrafo final sintetizando as conclusões mais importantes do documento e suas possíveis implicações ou recomendações.]

"""

# *****************************************************************************
# INTERFACE STREAMLIT
# *****************************************************************************

st.set_page_config(layout="centered", page_title="Sistema de processamento de PDF's com AI")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
  
    .stFileUploader {
        border: 2px dashed #ccc;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        background-color: #fff;
    }
    .stTextArea textarea {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ddd;
    }
    .stMarkdown h3 {
        color: #333;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Revisar PDF's com Google Gemini")
st.subheader("Revise seus textos, artigos, anotações físicas e digitais com resumos gerados pela Google Gemini")
st.markdown("Faça o upload de seu arquivo PDF:")
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
st.markdown("CUIDADO: O arquivo será enviado ao Google, portanto, NÃO ENVIE ARQUIVOS COM DADOS PESSOAIS. Use por sua própria responsabilidade.")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
        st.success(f"PDF '{uploaded_file.name}' carregado com sucesso!")

    if st.button("Resumir"):
        with st.spinner("Gerando resumo... Isso pode levar alguns momentos."):
          summary_result = process_pdf_with_gemini(tmp_file_path, few_shot_prompt_sumarize)

          if summary_result:
              st.subheader("Resumo finalizado, aproveite:")
              st.markdown(summary_result)
              try:
                os.remove(tmp_file_path)
              except OSError as e:
                st.warning(f"Não foi possível remover o arquivo temporário {tmp_file_path}: {e}")
          else:
              st.error("Não foi possível gerar o resumo!")
