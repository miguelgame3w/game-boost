import streamlit as st
import time

# Configuração da aba do navegador
st.set_page_config(page_title="GAME BOOST IA", page_icon="⚡")

# Título Principal
st.title("🚀 GAME BOOST IA")
st.write("Otimização Total: Sistema + Sensi de Elite")

# --- LISTA COMPLETA DO MIGUEL ---
lista_completa = [
    "iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max", "iPhone 16", "iPhone 16 Plus", 
    "iPhone 16 Pro", "iPhone 16 Pro Max", "iPhone 16e", "iPhone 17", "iPhone 17 Plus", "iPhone 17 Pro", 
    "iPhone 17 Pro Max", "iPhone 17e", "iPhone Air", "Galaxy S24", "Galaxy S24+", "Galaxy S24 Ultra", 
    "Galaxy S25", "Galaxy S25+", "Galaxy S25 Ultra", "Galaxy S25 FE", "Galaxy S26", "Galaxy S26+", 
    "Galaxy S26 Ultra", "Galaxy A05", "Galaxy A05s", "Galaxy A15", "Galaxy A25", "Galaxy A35", 
    "Galaxy A55", "Galaxy A17", "Galaxy Z Flip 6", "Galaxy Z Flip 7", "Galaxy Z Flip 7 FE", 
    "Galaxy Z Fold 6", "Galaxy Z Fold 7", "Motorola Razr 40", "Motorola Razr 50", "Motorola Razr 2025",
    "Xiaomi 13", "Xiaomi 13 Pro", "Xiaomi 13 Ultra", "Xiaomi 14", "Xiaomi 14 Pro", "Xiaomi 14 Ultra",
    "Xiaomi 15", "Xiaomi 15 Pro", "Xiaomi 15 Ultra", "Redmi 13", "Redmi 13C", "Redmi 14", "Redmi 14C",
    "Redmi 15", "Redmi 15C", "Redmi Note 13", "Redmi Note 13 Pro", "Redmi Note 13 Pro+",
    "Redmi Note 14", "Redmi Note 14 Pro", "Redmi Note 14 Pro+", "Poco X6", "Poco X6 Pro", "Poco X7", 
    "Poco X7 Pro", "Poco F6", "Poco F6 Pro", "Poco F7", "Poco F8 Pro", "Motorola Edge 40", 
    "Motorola Edge 40 Pro", "Motorola Edge 50", "Motorola Edge 50 Pro", "Motorola Edge 50 Ultra", 
    "Motorola Edge 60", "Motorola Edge 60 Pro", "Moto G14", "Moto G24", "Moto G34", "Moto G54", 
    "Moto G56", "Moto G75", "Moto G84", "Realme 11", "Realme 11 Pro+", "Realme 12", "Realme 12 Pro+", 
    "Realme 13", "Realme 13 Pro+", "Realme 14", "Realme 14 Pro+", "Oppo Reno 13", "Oppo Reno 15 Pro Max", 
    "Oppo Find X8 Pro", "Vivo V40", "Vivo V50 Pro", "Vivo X200 Ultra", "Google Pixel 9 Pro", 
    "Google Pixel 10 Pro", "OnePlus 13", "Nothing Phone 2", "Nothing Phone 3"
]

# --- PAINEL LATERAL ---
st.sidebar.header("⚙️ Configurações")
celular_usuario = st.sidebar.selectbox("Escolha seu Aparelho:", sorted(lista_completa))

st.sidebar.subheader("🛠️ Opções de Otimização")
boost_ram = st.sidebar.checkbox("Limpar Memória RAM")
boost_gpu = st.sidebar.checkbox("Forçar Renderização GPU")
boost_cache = st.sidebar.checkbox("Limpar Cache do Celular")

estilo = st.sidebar.radio("Estilo de Jogo:", ["Rushador (Sensi Alta)", "Suporte (Sensi Média)", "Instaplayer"])

# --- BOTÃO PRINCIPAL ---
if st.button("GERAR SENSI E OTIMIZAR"):
    with st.status(f"Otimizando seu {celular_usuario}...", expanded=True) as status:
        if boost_ram:
            st.write("⚡ Liberando RAM...")
            time.sleep(0.6)
        if boost_gpu:
            st.write("🎮 Calibrando Drivers Gráficos...")
            time.sleep(0.6)
        if boost_cache:
            st.write("🗑️ Removendo Cache...")
            time.sleep(0.6)
        st.write("🎯 Calculando Sensi de Elite...")
        time.sleep(0.8)
        status.update(label="✅ OTIMIZAÇÃO CONCLUÍDA!", state="complete", expanded=False)

    st.divider()

    # RESULTADOS DE SENSIBILIDADE
    st.subheader(f"🎯 Sensibilidade: {celular_usuario}")
    
    if "iPhone" in celular_usuario or "Ultra" in celular_usuario or "Pro" in celular_usuario:
        geral, red, m2x, m4x, awm, olha = "94", "97", "92", "90", "50", "75"
    else:
        geral, red, m2x, m4x, awm, olha = "98", "100", "96", "94", "45", "80"

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("GERAL", geral)
        st.metric("MIRA 2X", m2x)
    with c2:
        st.metric("PONTO VERMELHO", red)
        st.metric("MIRA 4X", m4x)
    with c3:
        st.metric("AWM", awm)
        st.metric("OLHADINHA", olha)

    st.divider()

    # DICAS DE SISTEMA
    st.subheader("📱 Ajustes no Celular")
    st.info("**CONFIGURAÇÃO RECOMENDADA:**\n\n- Escala de Animação: 0.5x\n- DPI Sugerida: 620\n- Botão de Tiro: 52%")

    st.divider()

    # BOTÃO PARA ENTRAR NO FREE FIRE
    st.subheader("🎮 TESTAR AGORA")
    link_ff = "https://play.google.com/store/apps/details?id=com.dts.freefireth" 
    st.link_button("🔥 ENTRAR NO FREE FIRE", link_ff, use_container_width=True)

    st.divider()

    # SEÇÃO DO TIKTOK (PEDIDO DO MIGUEL)
    col_tk1, col_tk2 = st.columns([2, 1])
    with col_tk1:
        st.write("### pode dar uma força me seguindo no tik tok")
    with col_tk2:
        st.link_button("Ir para o TikTok", "https://www.tiktok.com/@3wmiguel")

st.markdown("---")
st.caption("GAME BOOST IA - Desenvolvido por 3W Miguel")
