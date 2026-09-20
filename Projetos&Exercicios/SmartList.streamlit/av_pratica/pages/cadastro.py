import streamlit as st
import re
import time

st.markdown("""
<style>
    section[data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Cadastro", page_icon="📝")

if st.session_state.get("usuario_logado", False):
    st.switch_page("pages/itens.py")

if "usuarios" not in st.session_state:
    st.session_state.usuarios = []

st.title("Criar nova conta")
st.write("Preencha os dados abaixo para cadastrar seu acesso ao SmartList.")

if st.session_state.get("mostrando_spinner_cadastro", False):
    st.text_input("Nome completo", value=st.session_state.get("ultimo_nome", ""), disabled=True)
    st.text_input("Usuário", value=st.session_state.get("ultimo_usuario_cad", ""), disabled=True)
    st.text_input("Senha", value="••••••••", type="password", disabled=True)
    st.success("✅ Cadastro realizado com sucesso!")
    
    with st.spinner("Redirecionando para o login..."):
        time.sleep(1.5)
    
    st.session_state.mostrando_spinner_cadastro = False
    st.switch_page("pages/login.py")
else:
    nome = st.text_input("Nome completo", key="nome_input")
    usuario = st.text_input("Usuário", key="usuario_input")
    senha = st.text_input("Senha", type="password", key="senha_input")
    
    if senha:
        confirmar_senha = st.text_input("Confirmar senha", type="password", key="confirmar_input")

    nivel = ""
    senha_valida = True
    mensagem_erro_senha = ""
    
    if senha:
        senha_limpa = senha.strip()
        tamanho = len(senha_limpa)

        tem_maiuscula = bool(re.search(r"[A-Z]", senha_limpa))
        tem_minuscula = bool(re.search(r"[a-z]", senha_limpa))
        tem_numero = bool(re.search(r"\d", senha_limpa))
        tem_especial = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]', senha_limpa))

        tipos = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])

        senhas_muito_fracas = ['12345678', 'password', 'senha123', 'qwerty123', 'admin123']
        padrao_muito_fraco = (
            senha_limpa.lower() in senhas_muito_fracas or
            bool(re.match(r'^\d+$', senha_limpa)) or
            bool(re.match(r'^[a-zA-Z]+$', senha_limpa))
        )

        if tamanho < 8:
            nivel = "Muito fraca"
            senha_valida = False
            mensagem_erro_senha = "A senha deve ter no mínimo 8 caracteres."
        elif padrao_muito_fraco:
            nivel = "Muito fraca"
            senha_valida = False
            mensagem_erro_senha = "Senha muito comum ou usa apenas um tipo de caractere."
        elif tipos < 2:
            nivel = "Muito fraca"
            senha_valida = False
            mensagem_erro_senha = "Use pelo menos 2 tipos de caracteres diferentes."
        elif tipos == 2:
            nivel = "Fraca"
        elif tipos == 3:
            nivel = "Moderada"
        else:
            nivel = "Forte"

        if nivel == "Muito fraca":
            st.caption("Força da senha: 🔴 **Muito fraca** - Não atende aos requisitos mínimos")
        elif nivel == "Fraca":
            st.caption("Força da senha: 🔴 **Fraca**")
        elif nivel == "Moderada":
            st.caption("Força da senha: 🟡 **Moderada**")
        else:
            st.caption("Força da senha: 🟢 **Forte**")

    erros = []
    
    if nome:
        nome_limpo = nome.strip()
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome_limpo):
            erros.append("O nome deve conter apenas letras e espaços.")
        elif len(nome_limpo) < 3:
            erros.append("O nome deve ter pelo menos 3 caracteres.")
    
    if usuario:
        usuario_limpo = usuario.strip()
        if not re.match(r"^[a-zA-Z0-9_]+$", usuario_limpo):
            erros.append("O usuário só pode conter letras, números e _.")
        elif len(usuario_limpo) < 6:
            erros.append("O usuário deve ter no mínimo 6 caracteres.")
    
    if senha:
        if not senha_valida:
            erros.append(mensagem_erro_senha)
    
    if 'confirmar_senha' in locals() and senha != confirmar_senha:
        erros.append("As senhas não coincidem.")

    for erro in erros:
        st.error(erro)

    if st.button("Cadastrar", type="primary"):
        campos_vazios = []
        if not nome: campos_vazios.append("Nome completo")
        if not usuario: campos_vazios.append("Usuário")
        if not senha: campos_vazios.append("Senha")
        if 'confirmar_senha' not in locals() or not confirmar_senha: 
            campos_vazios.append("Confirmar senha")
        
        if campos_vazios:
            st.error(f"Preencha os campos: {', '.join(campos_vazios)}")
            st.stop()
        
        if erros:
            st.stop()

        usuario_limpo = usuario.strip()
        if any(u["usuario"] == usuario_limpo for u in st.session_state.usuarios):
            st.error("Este nome de usuário já está cadastrado.")
            st.stop()

        st.session_state.usuarios.append({
            "nome": nome.strip().title(),
            "usuario": usuario_limpo,
            "senha": senha
        })
        
        st.session_state.update({
            "login_usuario_auto": usuario_limpo,
            "login_senha_auto": senha,
            "ultimo_nome": nome.strip().title(),
            "ultimo_usuario_cad": usuario_limpo,
            "ultimo_nivel_senha": nivel,
            "mostrando_spinner_cadastro": True
        })
        
        st.rerun()
    
    st.markdown("---")
    st.write("Já possui uma conta?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ir para login", use_container_width=True):
            st.switch_page("pages/login.py")
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True):
            st.switch_page("smartlist.py")