{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "view-in-github"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vsampp/Project_Sumarize_PDF/blob/main/Project_PDF_AI.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IwQMJapBd7dc"
      },
      "outputs": [],
      "source": [
        "# *****************************************************************************\n",
        "# INSTALLATIONS\n",
        "# *****************************************************************************\n",
        "# Install SDK Google Gen AI.\n",
        "%pip -q install google-genai\n",
        "\n",
        "# Install ADK Google Agents\n",
        "%pip install -q google-adk\n",
        "\n",
        "# Install PyPDF2 Library\n",
        "%pip install -q PyPDF2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zC4CRtoxm0pL"
      },
      "outputs": [],
      "source": [
        "# *****************************************************************************\n",
        "# IMPORTS LIBRARY, SDKs, ADK AND FRAMEWORKS\n",
        "# *****************************************************************************\n",
        "from google import genai\n",
        "import os\n",
        "from google.colab import userdata\n",
        "from google.adk.agents import Agent\n",
        "from google.adk.runners import Runner\n",
        "from google.adk.sessions import InMemorySessionService\n",
        "from google.adk.tools import google_search\n",
        "from google.genai import types  # For create (Content e Part)\n",
        "import textwrap # For format output text\n",
        "from IPython.display import display, Markdown # Para exibir texto formatado no Colab\n",
        "import requests # For HTTP requests\n",
        "import warnings\n",
        "import PyPDF2 as pdf # For read PDF\n",
        "\n",
        "warnings.filterwarnings(\"ignore\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vvHd5oIfiozk"
      },
      "outputs": [],
      "source": [
        "# *****************************************************************************\n",
        "# FUNCTIONS\n",
        "# *****************************************************************************\n",
        "\n",
        "# Function for call AI Agents for utilize Runner for take prompt and get response (UTILIZAR PARA FAZER O QUIS)\n",
        "def call_agent(agent: Agent, message_text: str) -> str:\n",
        "    # Create service session in memory\n",
        "    session_service = InMemorySessionService()\n",
        "    # Create a new session (you can personalize IDs)\n",
        "    session = session_service.create_session(app_name=agent.name, user_id=\"user1\", session_id=\"session1\")\n",
        "    # Create a Runner (Agent) for set prompt and get response\n",
        "    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)\n",
        "    # Create a message content\n",
        "    content = types.Content(role=\"user\", parts=[types.Part(text=message_text)])\n",
        "\n",
        "    final_response = \"\"\n",
        "\n",
        "    # Itera assincronamente pelos eventos retornados durante a execução do agente\n",
        "    for event in runner.run(user_id=\"user1\", session_id=\"session1\", new_message=content):\n",
        "        if event.is_final_response():\n",
        "          for part in event.content.parts:\n",
        "            if part.text is not None:\n",
        "              final_response += part.text\n",
        "              final_response += \"\\n\"\n",
        "    return final_response"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ExqW4DP6orBJ"
      },
      "outputs": [],
      "source": [
        "# Function for text formart Markdown\n",
        "def to_markdown(text):\n",
        "  text = text.replace('•', '  *')\n",
        "  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S26Cm8Tto0wp"
      },
      "outputs": [],
      "source": [
        "# Function for read PDF in Python with PyPDF2\n",
        "def read_pdf(file_path):\n",
        "    try:\n",
        "        with open(file_path, 'rb') as file:\n",
        "            reader = pdf.PdfReader(file)\n",
        "            text = ''\n",
        "            for page_num in range(len(reader.pages)):\n",
        "                page = reader.pages[page_num]\n",
        "                text += page.extract_text()\n",
        "        return text\n",
        "    #except ImportError:\n",
        "        #print(\"Please install the PyPDF2 library: !pip install PyPDF2\")\n",
        "        #return None\n",
        "    except Exception as e:\n",
        "        print(f\"Error ao ler PDF: {e}\")\n",
        "        return None\n",
        "\n",
        "\n",
        "def process_pdf_with_gemini(file_path, prompt):\n",
        "\n",
        "    pdf_text = read_pdf(file_path)\n",
        "\n",
        "    if pdf_text:\n",
        "        # Combine the PDF content and the user's prompt\n",
        "        full_prompt = f\"Aqui está o conteúdo do PDF:\\n\\n{pdf_text}\\n\\n{prompt}\"\n",
        "\n",
        "        try:\n",
        "            # Use the existing clientSDK and MODEL_ID\n",
        "            response = clientSDK.models.generate_content(\n",
        "                model=MODEL_ID,\n",
        "                contents=full_prompt\n",
        "            )\n",
        "            return response.text\n",
        "        except Exception as e:\n",
        "            print(f\"Error ao gerar o conteúdo: {e}\")\n",
        "            return None\n",
        "    else:\n",
        "        return None"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HeSoLBThfrpC"
      },
      "outputs": [],
      "source": [
        "# Setting API Key do Google Gemini\n",
        "os.environ[\"GOOGLE_API_KEY\"] = userdata.get('GOOGLE_API_KEY')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pDtUAwStg2qP"
      },
      "outputs": [],
      "source": [
        "# Create Client SDK\n",
        "clientSDK = genai.Client()\n",
        "\n",
        "# Define Gemini Model\n",
        "MODEL_ID = \"gemini-2.0-flash\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wtfsrQHHj80m"
      },
      "outputs": [],
      "source": [
        "# Define prompts\n",
        "few_shot_prompt=\"\"\"\n",
        "    **Contexto e Objetivo:**\n",
        "Você é um **analista e sintetizador de documentos altamente qualificado**, com expertise no assunto do arquivo PDF fornecido.\n",
        "Sua principal missão é processar este documento para gerar um **resumo detalhado e de fácil compreensão**, mantendo a fidelidade\n",
        "ao conteúdo original.\n",
        "\n",
        "**Instruções de Processamento Detalhadas:**\n",
        "1.  **Leitura Integral e Profunda:** Leia o arquivo PDF na sua totalidade, com atenção meticulosa a cada linha, parágrafo, seção e capítulo.\n",
        "Assegure-se de compreender plenamente a estrutura, o fluxo de argumentos e as nuances do texto.\n",
        "\n",
        "2.  **Extração de Informações Essenciais:** Durante a leitura, identifique e extraia:\n",
        "    * **Tópicos Principais:** As ideias centrais de cada seção ou capítulo.\n",
        "    * **Conceitos-Chave:** Definições importantes, terminologias específicas e suas explicações.\n",
        "    * **Argumentos e Evidências:** As principais teses apresentadas e os dados ou raciocínios que as sustentam.\n",
        "    * **Exemplos Cruciais:** Ilustrações, estudos de caso ou cenários que ajudam a clarear os conceitos.\n",
        "    * **Conclusões e Recomendações:** Os pontos finais e as implicações do conteúdo.\n",
        "\n",
        "3.  **Elaboração do Resumo Detalhado:**\n",
        "    * Organize as informações extraídas de forma lógica e hierárquica, refletindo a estrutura do PDF.\n",
        "    * Para cada ponto relevante, forneça uma **explicação clara e concisa**, utilizando uma linguagem simples e acessível,\n",
        "    como se estivesse explicando o conteúdo a um público não especialista.\n",
        "    * **Mantenha o Contexto:** É crucial que a simplificação não comprometa o contexto original ou a profundidade das informações.\n",
        "    * **Inclua Exemplos Relevantes:** Incorpore os exemplos mais importantes para ilustrar os conceitos e facilitar a compreensão.\n",
        "    * **Evite Perdas:** Tenha extremo cuidado para não omitir informações críticas, detalhes importantes ou nuances significativas\n",
        "    do documento original.\n",
        "\n",
        "4.  **Formato de Saída:**\n",
        "    Apresente o resumo utilizando a seguinte estrutura em Markdown, preenchendo as seções com o conteúdo extraído:\n",
        "\n",
        "```markdown\n",
        "### Resumo Detalhado do Documento: [Título do PDF, se disponível, ou \"Documento Fornecido\"]\n",
        "\n",
        "**1. Introdução e Contexto Geral:**\n",
        "[Breve parágrafo contextualizando o documento, seu propósito e o que ele aborda.]\n",
        "\n",
        "**2. Principais Seções/Capítulos e Tópicos Abordados:**\n",
        "\n",
        "* **[Título da Seção/Capítulo 1]:**\n",
        "    * **Conceito/Ponto 1.1:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]\n",
        "    * **Conceito/Ponto 1.2:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]\n",
        "    * ... (Adicionar mais pontos conforme necessário)\n",
        "\n",
        "* **[Título da Seção/Capítulo 2]:**\n",
        "    * **Conceito/Ponto 2.1:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]\n",
        "    * **Conceito/Ponto 2.2:** [Explicação detalhada e simplificada. Incluir exemplos relevantes aqui.]\n",
        "    * ... (Adicionar mais pontos conforme necessário)\n",
        "\n",
        "* ... (Continuar para todas as seções/capítulos relevantes do PDF)\n",
        "\n",
        "**3. Conclusões Principais e Implicações:**\n",
        "[Um parágrafo final sintetizando as conclusões mais importantes do documento e suas possíveis implicações ou recomendações.]\n",
        "\n",
        "\"\"\"\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N5HQArinpt-L"
      },
      "outputs": [],
      "source": [
        "%pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rK3EzWbap-Gv",
        "outputId": "71ff2a9e-6f4f-4a42-b051-fd4c595fe64c"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2025-05-21 03:15:03.677 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.680 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.682 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.684 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.686 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.690 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.691 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.693 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.694 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.695 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.697 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 03:15:03.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "# --- Interface Streamlit ---\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "\n",
        "st.set_page_config(layout=\"centered\", page_title=\"Sumarizador de PDF com Gemini\")\n",
        "\n",
        "st.markdown(\n",
        "    \"\"\"\n",
        "    <style>\n",
        "    .main {\n",
        "        background-color: #f0f2f6;\n",
        "        padding: 2rem;\n",
        "        border-radius: 10px;\n",
        "        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n",
        "    }\n",
        "    .stButton>button {\n",
        "        background-color: #4CAF50;\n",
        "        color: white;\n",
        "        border-radius: 8px;\n",
        "        padding: 10px 20px;\n",
        "        font-size: 16px;\n",
        "        border: none;\n",
        "        cursor: pointer;\n",
        "        transition: background-color 0.3s ease;\n",
        "    }\n",
        "    .stButton>button:hover {\n",
        "        background-color: #45a049;\n",
        "    }\n",
        "    .stFileUploader {\n",
        "        border: 2px dashed #ccc;\n",
        "        border-radius: 8px;\n",
        "        padding: 20px;\n",
        "        text-align: center;\n",
        "        background-color: #fff;\n",
        "    }\n",
        "    .stTextArea textarea {\n",
        "        border-radius: 8px;\n",
        "        padding: 10px;\n",
        "        border: 1px solid #ddd;\n",
        "    }\n",
        "    .stMarkdown h3 {\n",
        "        color: #333;\n",
        "        border-bottom: 2px solid #4CAF50;\n",
        "        padding-bottom: 5px;\n",
        "        margin-top: 20px;\n",
        "    }\n",
        "    </style>\n",
        "    \"\"\",\n",
        "    unsafe_allow_html=True\n",
        ")\n",
        "\n",
        "st.title(\"📚 Sumarizador de PDF com API Gemini\")\n",
        "st.markdown(\"Faça o upload de um arquivo PDF e receba um resumo detalhado gerado pela API Gemini.\")\n",
        "\n",
        "\n",
        "st.subheader(\"Upload do Arquivo PDF\")\n",
        "uploaded_file = st.file_uploader(\"Escolha um arquivo PDF\", type=\"pdf\")\n",
        "\n",
        "if uploaded_file is not None:\n",
        "    st.success(f\"Arquivo '{uploaded_file.name}' carregado com sucesso!\")\n",
        "\n",
        "    if st.button(\"Sumarizar\"):\n",
        "        with st.spinner(\"Gerando resumo... Isso pode levar alguns momentos.\"):\n",
        "          summary_result = process_pdf_with_gemini(uploaded_file, few_shot_prompt)\n",
        "\n",
        "          if summary_result:\n",
        "              st.subheader(\"Sumarização Realizada:\")\n",
        "              st.markdown(summary_result)\n",
        "          else:\n",
        "              st.error(\"Não foi possível gerar a sumarização.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4J6qADrdqGap"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyMEdwAimpbZXrZFygBVOwJx",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
