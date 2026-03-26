import streamlit as st

# Configurações do App
st.set_page_config(page_title="EcoDoa MVP", page_icon="🌱")

st.title("🌱 EcoDoa: Mural de Doações")
st.caption("📍 Centro - Itajaí, SC")

# Menu de Navegação
aba = st.tabs(["📋 Mural", "➕ Doar Item"])

with aba[0]:
    st.write("### Itens Disponíveis")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Cadeira Office**\nDoador: Carlos\nDistância: 500m")
        if st.button("Reservar Cadeira"):
            st.success("Reserva solicitada!")
    with col2:
        st.info("**Sofá 3 Lugares**\nDoador: Maria\nDistância: 1.2km")
        if st.button("Reservar Sofá"):
            st.success("Reserva solicitada!")

with aba[1]:
    st.write("### Cadastrar Doação")
    with st.form("form"):
        nome = st.text_input("O que você vai doar?")
        desc = st.text_area("Estado do item")
        if st.form_submit_button("Publicar"):
            st.balloons()
            st.success("Publicado com sucesso!")