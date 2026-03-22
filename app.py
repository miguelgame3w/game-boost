import streamlit as st
import time
import random

# Configurações de Design
st.set_page_config(page_title="GAME BOOST IA - V2", page_icon="🎯", layout="centered")

# CSS para deixar o site com cara de Aplicativo de Elite
st.markdown("""
    <style>
    .main { background-color: #06090f; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff0000, #ff4b4b);
        color: white;
        border: none;
        padding: 15px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(255, 0, 0, 0.4);
    }
    .stSelectbox, .stCheckbox { color: #ffffff; }
    h1 { color: #ff4b4b; text-align: center; text-shadow: 2px 2px #000; }
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ GAME BOOST IA: PRO")
st.write("---")

# --- SISTEMA DE SELEÇÃO ---
col1, col2 = st.columns(2)
with col1:
    marca = st.selectbox("Marca do Celular:", ["Apple", "Samsung", "Xiaomi/Poco", "Motorola", "Realme", "Outros"])
with col2:
    # Lista dinâmica baseada na marca
    if marca == "Apple": dispositivos = ["iPhone 13", "iPhone 14", "iPhone 15 Pro", "iPhone 16 Pro Max"]
    elif marca == "Samsung": dispositivos = ["Galaxy A05", "Galaxy A15", "Galaxy A55", "Galaxy S24 Ultra", "Galaxy S25 Ultra"]
    elif marca == "Xiaomi/Poco": dispositivos = ["Poco X6 Pro", "Poco F6", "Redmi Note 13", "Xiaomi 14 Ultra"]
    else: dispositivos = ["Moto G84", "Edge 50 Pro", "Realme 12 Pro+", "Rog Phone 8"]
    
    celular = st.selectbox("Modelo:", dispositivos)

st.subheader("🛠️ Módulos de Injeção")
c_boost1, c_boost2, c_boost3 = st.columns(3)
with c_boost1: boost_fps = st.checkbox("🔥 FPS UNLOCK")
with c_boost2: boost_sensi = st.checkbox("🎯 SENSI 2.0")
with c_boost3: boost_net = st.checkbox("🌐 PING ZERO")

# --- EXECUÇÃO ---
if st.button("INJETAR OTIMIZAÇÃO NO SISTEMA"):
    with st.status("🔍 Analisando Hardware...", expanded=True) as status:
        time.sleep(1)
        st.write(f"📁 Acessando registros do {celular}...")
        time.sleep(0.8)
        if boost_fps: st.write("🚀 Desbloqueando limite de 120 FPS..."); time.sleep(0.5)
        if boost_sensi: st.write("🎯 Calibrando touch screen..."); time.sleep(0.5)
        st.write("✅ Scripts injetados com sucesso!")
        status.update(label="🚀 OTIMIZAÇÃO CONCLUÍDA!", state="complete", expanded=False)

    st.balloons()
    
    # --- RESULTADOS ESTILO PAINEL ---
    st.markdown("### 📊 Resultado da Calibração")
    
    # Lógica de Sensi Aleatória mas "Realista"
    s1, s2, s3, s4 = st.columns(4)
    with s1: st.metric("GERAL", f"{random.randint(95, 100)}")
    with s2: st.metric("RED DOT", f"{random.randint(94, 99)}")
    with s3: st.metric("2X", f"{random.randint(92, 98)}")
    with s4: st.metric("4X", f"{random.randint(90, 96)}")

    st.success(f"**DPI RECOMENDADA:** {random.choice([580, 600, 620, 710, 800])}")
    
    st.divider()
    
    # --- BOTÕES SOCIAIS ---
    st.write("#### 🔗 Links Oficiais")
    btn1, btn2 = st.columns(2)
    with btn1:
        st.link_button("📱 SEGUE NO TIKTOK", "https://www.tiktok.com/@3wmiguel", use_container_width=True)
    with btn2:
        st.link_button("🎮 ABRIR FREE FIRE", "https://play.google.com/store/apps/details?id=com.dts.freefireth", use_container_width=True)

st.markdown("<br><center><p style='color: gray;'>Versão 2.4.0 Patch Note | Desenvolvido por 3W Miguel</p></center>", unsafe_allow_html=True)
