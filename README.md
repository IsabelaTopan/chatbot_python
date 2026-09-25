Chatbot com IA e Streamlit

Um aplicativo de chat simples e interativo, desenvolvido durante a Jornada Python da Hashtag Treinamentos, construído com Python, Streamlit e a API da OpenAI. O projeto mantém o histórico de conversas durante a sessão e permite que qualquer usuário utilize sua própria chave de API da OpenAI através da barra lateral.

Funcionalidades

Interface Intuitiva: Interface de chat limpa e amigável utilizando os componentes nativos do Streamlit (st.chat_input e st.chat_message).

Histórico de Conversa: Gerenciamento de estado de sessão (st.session_state) para manter o contexto do diálogo.

Entrada Segura de Chave API: Permite que os usuários insiram suas próprias chaves de API com segurança na barra lateral (campo do tipo senha), sem necessidade de expor credenciais no código-fonte.

Tratamento de Erros: Exibição de avisos caso o usuário tente enviar uma mensagem sem ter configurado a chave.