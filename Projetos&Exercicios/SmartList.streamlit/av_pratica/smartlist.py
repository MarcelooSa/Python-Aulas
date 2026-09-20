### Página 1 — Cadastro de Usuário (Página Independente)
#
#* Função: Local exclusivo para cadastrar novos usuários do sistema.
#* Campos sugeridos:
# * Nome completo
# * E-mail
# * Senha
#* Ação: Adicionar usuário à memória do sistema (lista de usuários).
#* Resultado: Garantir que cada usuário tenha uma conta para acessar o sistema.
import streamlit as st

st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SmartList - Início",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if st.session_state.get("usuario_logado", False):
    st.switch_page("pages/itens.py")

st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
    </style>
""", unsafe_allow_html=True)

st.title("🛒 SmartList")
st.subheader("Sua lista de compras inteligente")

st.write(
    """
    O **SmartList** ajuda você a organizar suas compras do dia a dia, controlar gastos
    e visualizar melhor seu orçamento.
    """
)

st.markdown("---")

st.header("✨ Funcionalidades")

st.write(
    """
    - Cadastrar itens (nome, quantidade, preço estimado)  
    - Calcular o valor total da compra  
    - Avisar se passou do orçamento definido  
    - Exportar automaticamente em Excel  
    - Comparar gastos com meses anteriores  
    - E muito mais!  
    """
)

st.markdown("---")

st.write("### Acesse sua conta ou crie uma nova")

col1, col2 = st.columns(2)

with col1:
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/login.py")

with col2:
    if st.button("Cadastre-se", use_container_width=True):
        st.switch_page("pages/cadastro.py")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    with st.expander("💡 **Benefícios de usar**", expanded=False):
        st.write("""
        **💰 Economia de dinheiro**  
        Controle seus gastos e evite compras desnecessárias.
        
        **⏰ Economia de tempo**  
        Listas organizadas = menos tempo no mercado.
        
        **📈 Educação financeira**  
        Aprenda sobre seus hábitos de consumo.
        
        **📱 Praticidade**  
        Acesse suas listas de qualquer dispositivo.
        
        **🎯 Foco nas compras**  
        Não esqueça mais itens importantes.
        """)

with col2:
    with st.expander("❓ **Perguntas frequentes**", expanded=False):
        st.write("""
        **É gratuito?**  
        Sim, o SmartList é totalmente gratuito.
        
        **Precisa instalar?**  
        Não, basta acessar pelo navegador.
        
        **Meus dados estão seguros?**  
        Sim, seus dados ficam salvos localmente.
        
        **Posso usar no celular?**  
        Sim, funciona em qualquer dispositivo.
        """)

st.markdown("---")

st.caption("© 2025 SmartList")