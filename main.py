import streamlit as st
from openai import OpenAI

st.write("# Chatbot com IA")

# Campo na barra lateral para o usuário inserir a própria chave da OpenAI
st.sidebar.title("Configuração")
api_key_usuario = st.sidebar.text_input("Insira sua OpenAI API Key", type="password")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

# Exibe o histórico existente
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # Verifica se o usuário inseriu a chave antes de chamar a API
    if not api_key_usuario:
        st.error("Por favor, insira sua API Key da OpenAI na barra lateral para continuar.")
    else:
        # Inicializa o cliente com a chave fornecida pelo usuário
        modelo_ia = OpenAI(api_key=api_key_usuario)

        st.chat_message("user").write(texto_usuario)
        mensagem_usuario = {"role": "user", "content": texto_usuario}
        st.session_state["lista_mensagens"].append(mensagem_usuario)

        resposta_ia = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-4o-mini"
        )

        texto_resposta_ia = resposta_ia.choices[0].message.content

        st.chat_message("assistant").write(texto_resposta_ia)
        mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)