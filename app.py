import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE
# ==============================================================================
st.set_page_config(
    page_title="🛡️ SENSI XIT PRO",
    page_icon="😈",
    layout="centered"
)

# ==============================================================================
# 2. CSS AVANÇADO - ANIMAÇÕES, RAIOS E BOTÕES ROXOS
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO NEON VERMELHO PULSANTE */
    .xit-title-glow {
        color: #ff0000; text-align: center; font-weight: 800; font-size: 45px;
        text-transform: uppercase; text-shadow: 0 0 15px #ff0000;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

    /* --- ANIMAÇÃO DE RAIOS ROXOS --- */
    @keyframes lightning {
        0%, 100% { opacity: 0; }
        10%, 90% { opacity: 0; }
        11%, 13%, 15% { opacity: 1; text-shadow: 0 0 20px #7f00ff, 0 0 40px #7f00ff; }
    }
    .raios {
        position: fixed; top: 10%; left: 50%; transform: translateX(-50%);
        font-size: 100px; color: #7f00ff; z-index: 999;
        pointer-events: none; animation: lightning 3s infinite;
    }

    /* --- BOTÕES DE SELEÇÃO (Lógica de Cor Roxa) --- */
    .stButton > button {
        background-color: #1a1e29; color: #888; border-radius: 12px;
        border: 1px solid #2a2f3f; font-weight: bold; transition: all 0.3s;
        width: 100%;
    }
    
    /* Quando o botão é o selecionado (Lógica via Python abaixo) */
    .stButton > button[kind="primary"] {
        background-color: #7f00ff !important; color: white !important;
        border: none !important; box-shadow: 0 0 15px #7f00ff;
    }

    /* BARRAS DE SENSI */
    .sensi-container {
        background-color: #161a25; border-radius: 15px; padding: 20px;
        border: 1px solid #1e2230; margin-top: 20px;
    }
    .bar-bg { background-color: #2a2f3f; border-radius: 10px; height: 12px; width: 100%; }
    .bar-fill {
        background: linear-gradient(90deg, #7f00ff, #ff0000);
        height: 100%; border-radius: 10px; box-shadow: 0 0 10px #7f00ff;
    }
    .status-badge {
        color: #00ff00; padding: 5px 12px; border-radius: 8px;
        border: 1px solid #00ff00; font-size: 12px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LÓGICA DE MEMÓRIA (BOTÕES ROXOS)
# ==============================================================================
if 'plataforma' not in st.session_state:
    st.session_state.plataforma = "ANDROID"

# Título
st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.write("###")

# --- AS 3 OPÇÕES (ANDROID, iOS, PC) ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("ANDROID", type="primary" if st.session_state.plataforma == "ANDROID" else "secondary"):
        st.session_state.plataforma = "ANDROID"
        st.rerun()
with col2:
    if st.button("iOS", type="primary" if st.session_state.plataforma == "iOS" else "secondary"):
        st.session_state.plataforma = "iOS"
        st.rerun()
with col3:
    if st.button("PC/EMU", type="primary" if st.session_state.plataforma == "PC" else "secondary"):
        st.session_state.plataforma = "PC"
        st.rerun()

# --- INPUTS ---
st.write("###")
modelo = st.text_input("MODELO DO DISPOSITIVO", placeholder=f"Ex: {st.session_state.plataforma} Gaming")

c_h1, c_h2 = st.columns(2)
with c_h1: ram = st.selectbox("MEMÓRIA RAM", ["4 GB", "6 GB", "8 GB", "12 GB", "16 GB+"])
with c_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 256 GB")

st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("MIRA NÃO PASSAR (XIT)")

st.write("---")

# ==============================================================================
# 4. GERAÇÃO COM ANIMAÇÃO DE RAIOS E CAPETINHA
# ==============================================================================
if st.button("🚀 GERAR CONFIGURAÇÃO", use_container_width=True, type="primary"):
    if not modelo:
        st.error("Digite o modelo!")
    else:
        # Efeito de Raios e Capetinha antes de mostrar
        st.markdown('<div class="raios">⚡😈⚡</div>', unsafe_allow_html=True)
        with st.spinner("Injetando Scripts..."):
            time.sleep(2)
        
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        
        # Banner de Status
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <span style="color:white; font-size:20px; font-weight:bold;">😈 {modelo.upper()}</span>
                <span class="status-badge">XIT ATIVADO</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Sensis Geradas
        itens = ["GERAL", "RED DOT", "MIRA 2X", "MIRA 4X"]
        for item in itens:
            val = random.randint(160, 199)
            perc = (val/200)*100
            st.markdown(f'''
                <div style="display:flex; justify-content:space-between; color:white; font-size:14px; margin-bottom:5px;">
                    <span>{item}</span><span>{val}</span>
                </div>
                <div class="bar-bg"><div class="bar-fill" style="width:{perc}%;"></div></div><br>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("Configuração Mítica Injetada!")

st.markdown("<p style='text-align:center; color:#333; font-size:10px; margin-top:50px;'>3W MIGUEL XIT ENGINE © 2026</p>", unsafe_allow_html=True)
