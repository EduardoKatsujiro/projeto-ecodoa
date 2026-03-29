import streamlit as st

# 1. Inicialização da Memória (Só acontece uma vez)
if 'lista_doacoes' not in st.session_state:
    st.session_state.lista_doacoes = [
        {"item": "Cadeira Office", "doador": "Carlos R.", "distancia": "500m", "status": "Disponível"},
        {"item": "Sofá 3 Lugares", "doador": "Maria S.", "distancia": "1.2km", "status": "Disponível"}
    ]

# Função para adicionar o item (Executa ANTES de recarregar a página)
def adicionar_item():
    item = st.session_state.temp_item
    nome = st.session_state.temp_nome
    bairro = st.session_state.temp_bairro
    
    if item and nome:
        nova_doacao = {
            "item": item,
            "doador": nome,
            "distancia": f"Bairro: {bairro}",
            "status": "Disponível"
        }
        st.session_state.lista_doacoes.append(nova_doacao)
        st.toast(f"✅ {item} cadastrado com sucesso!")

# Configurações de Design
st.set_page_config(page_title="EcoDoa - Itajaí", page_icon="🌱")
st.title("🌱 EcoDoa - Itajaí")

# 2. Navegação por Abas
aba1, aba2 = st.tabs(["📋 Mural de Itens", "➕ Cadastrar Doação"])

with aba1:
    st.header("Itens Perto de Você")
    # Loop para mostrar os itens (do mais novo para o mais antigo)
    for i, d in enumerate(reversed(st.session_state.lista_doacoes)):
        # Ajustando o índice original por causa do 'reversed'
        idx_original = len(st.session_state.lista_doacoes) - 1 - i
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"📦 {d['item']}")
                st.write(f"👤 Doador: {d['doador']} | 📍 {d['distancia']}")
                st.write(f"Status: **{d['status']}**")
            with col2:
                if d['status'] == "Disponível":
                    if st.button(f"Reservar", key=f"btn_{idx_original}"):
                        st.session_state.lista_doacoes[idx_original]['status'] = "RESERVADO"
                        st.rerun()
                else:
                    st.error("Reservado")

with aba2:
    st.header("O que você deseja desapegar?")
    # Campos de entrada vinculados ao estado temporário
    st.text_input("Nome do objeto", key="temp_item")
    st.text_input("Seu nome", key="temp_nome")
    st.selectbox("Bairro", ["Centro", "Fazenda", "Vila Operária", "Cordeiros"], key="temp_bairro")
    
    # Botão que chama a função de adicionar antes de qualquer coisa
    st.button("Publicar Doação agora", on_click=adicionar_item)
    
    st.info("Após clicar em 'Publicar', verifique a aba 'Mural de Itens'.")
