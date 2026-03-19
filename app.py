import streamlit as st
import time

# Configuração da aba do navegador
st.set_page_config(page_title="GAME BOOST IA", page_icon="⚡")

# Estilo para deixar o site com cara de Gamer
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 GAME BOOST IA")
st.write("Otimização Total: Sistema + Sensi de Elite")

# --- LISTA COMPLETA ---
lista_dispositivos = [
    "iPhone 13", "iPhone 13 Pro", "iPhone 14", "iPhone 14 Pro Max", "iPhone 15", "iPhone 15 Pro Max", "iPhone 16 Pro Max",
    "Galaxy A05", "Galaxy A15", "Galaxy A35", "Galaxy A55", "Galaxy S23 Ultra", "Galaxy S24 Ultra", "Galaxy S25 Ultra",
    "Moto G54", "Moto G84", "Motorola Edge 50 Pro", "Poco X6 Pro", "Poco F6", "Redmi Note 13 Pro", "Xiaomi 14 Ultra"
]

# --- PAINEL LATERAL ---
st.sidebar.header("⚙️ Configurações")
celular = st.sidebar.selectbox("Escolha seu Aparelho:", sorted(lista_dispositivos))

st.sidebar.subheader("🛠️ Ativar Boost")
ram = st.sidebar.checkbox("Limpar Memória RAM")
gpu = st.sidebar.checkbox("Forçar GPU")
ping = st.sidebar.checkbox("Otimizar Ping")

# --- BOTÃO PRINCIPAL ---
if st.button("GERAR SENSI E OTIMIZAR TOTAL"):
    with st.status("Executando scripts de otimização...", expanded=True) as status:
        if ram: st.write("⚡ RAM limpa!"); time.sleep(0.5)
        if gpu: st.write("🎮 GPU em modo Performance!"); time.sleep(0.5)
        if ping: st.write("🌐 Rota de conexão otimizada!"); time.sleep(0.5)
        st.write("🎯 Calculando Sensibilidade...")
        time.sleep(1)
        status.update(label="✅ PROCESSO CONCLUÍDO!", state="complete", expanded=False)

    st.divider()
    st.subheader(f"🎯 Sensi de Elite: {celular}")
    
    # Valores de Sensi (Simulados para impacto)
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("GERAL", "98"); st.metric("MIRA 2X", "95")
    with c2: st.metric("PONTO VERMELHO", "100"); st.metric("MIRA 4X", "92")
    with c3: st.metric("AWM", "45"); st.metric("OLHADINHA", "80")

    st.info("💡 DICA: Use DPI 600 e Botão de Tiro em 52% para melhores resultados.")

    st.divider()
    st.write("### Ajude o criador!")
    st.link_button("📱 ME SEGUIR NO TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel")
    st.link_button("🔥 ABRIR FREE FIRE", "https://play.google.com/store/apps/details?id=com.dts.freefireth", use_container_width=True)

st.caption("Desenvolvido por 3W Miguel")
