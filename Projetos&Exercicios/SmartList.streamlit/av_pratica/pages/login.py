import streamlit as st
import time

st.markdown("""
<style>
    section[data-testid="stSidebar"],
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Login - SmartList",
    page_icon="🔐",
    initial_sidebar_state="collapsed"
)

estados_iniciais = {
    "usuarios": [],
    "usuario_logado": False,
    "login_usuario_auto": "",
    "login_senha_auto": "",
    "mostrando_spinner": False,
    "ultimo_usuario": ""
}

for chave, valor in estados_iniciais.items():
    if chave not in st.session_state:
        st.session_state[chave] = valor

if st.session_state.usuario_logado:
    st.switch_page("pages/itens.py")

st.title("🔐 Acesso à sua conta")

if st.session_state.mostrando_spinner:
    st.text_input("Nome de usuário", value=st.session_state.ultimo_usuario, disabled=True, key="usuario_disabled")
    st.text_input("Senha", value="••••••••", type="password", disabled=True, key="senha_disabled")
    
    st.success(f"✅ Login bem-sucedido! Bem-vindo(a), {st.session_state.usuario_nome}!")
    
    with st.spinner("Carregando seu dashboard..."):
        time.sleep(1.5)
    
    st.session_state.usuario_logado = True
    st.session_state.mostrando_spinner = False
    st.rerun()

else:
    st.write("Entre com seu usuário e senha para continuar usando o SmartList.")
    
    with st.form("form_login", clear_on_submit=False):
        usuario_input = st.text_input("Nome de usuário", value=st.session_state.login_usuario_auto)
        senha_input = st.text_input("Senha", type="password", value=st.session_state.login_senha_auto)
        entrar = st.form_submit_button("Entrar", type="primary")
    
    if entrar:
        usuario = next(
            (u for u in st.session_state.usuarios 
             if u["usuario"] == usuario_input and u["senha"] == senha_input),
            None
        )
        
        if usuario:
            st.session_state.usuario_nome = usuario["nome"]
            st.session_state.login_usuario_auto = usuario_input
            st.session_state.login_senha_auto = senha_input
            st.session_state.ultimo_usuario = usuario_input
            st.session_state.mostrando_spinner = True
            st.rerun()
        else:
            st.error("❌ Credenciais inválidas. Tente novamente.")

    st.markdown("---")
    st.write("Ainda não possui uma conta?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 Cadastre-se", use_container_width=True):
            st.switch_page("pages/cadastro.py")
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True):
            st.switch_page("smartlist.py")