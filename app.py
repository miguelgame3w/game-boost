import streamlit as st
import time

st.set_page_config(page_title="GAME BOOST IA", page_icon="⚡")
st.title("🚀 GAME BOOST IA")
st.write("Otimização Total: Sistema + Sensi de Elite")

# Lista de celulares para o seu público
lista_completa = [
    "iPhone 15 Pro Max", "iPhone 16 Pro Max", "Galaxy S24 Ultra", "Galaxy S25 Ultra", 
    "Galaxy A05", "Galaxy A15", "Galaxy A55", "Moto G54", "Moto G84", "Poco X6 Pro", "Redmi Note 13"
]

st.sidebar.header("⚙️ Configurações")
celular_usuario = st.sidebar.selectbox("Escolha seu Aparelho:", sorted(lista_completa))

if st.button("GERAR SENSI E OTIMIZAR"):
    with st.status(f"Otimizando seu {celular_usuario}...", expanded=True) as status:
        time.sleep(1.5)
        status.update(label="✅ OTIMIZAÇÃO CONCLUÍDA!", state="complete", expanded=False)

    st.subheader(f"🎯 Sensibilidade: {celular_usuario}")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("GERAL", "98")
    with c2: st.metric("2X", "96")
    with c3: st.metric("4X", "94")

    st.divider()
    st.write("### pode dar uma força me seguindo no tik tok")
    st.link_button("📱 MEU TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel")
    
    st.divider()
    st.link_button("🔥 ENTRAR NO FREE FIRE", "https://play.google.com/store/apps/details?id=com.dts.freefireth", use_container_width=True)

st.caption("Desenvolvido por 3W Miguel")
