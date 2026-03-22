import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE
# ==============================================================================
st.set_page_config(
    page_title="🛡️ SENSI XIT PRO",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CSS AVANÇADO - ANIMAÇÕES E DESIGN HYPE
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO NEON PULSANTE */
    .xit-title-glow {
        color: #ff0000;
        text-align: center;
        font-weight: 800;
        font-size: 45px;
        text-transform: uppercase;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.7; } 100% { opacity: 1; } }

    /* --- ANIMAÇÃO NOS BOTÕES (RESOLUÇÃO) --- */
    div.stButton > button {
        background-color: #1a1e29;
        color: #888;
        border-radius: 12px;
        border: 1px solid #2a2f3f;
        font-weight: bold;
        transition: all 0.3s ease-in-out; /* Transição suave */
    }

    /* Efeito ao passar o mouse */
    div.stButton > button:hover {
        border-color: #7f00ff;
        color: white;
        transform: translateY(-2px); /* Sobe um pouquinho */
        box-shadow: 0 5px 15px rgba(127, 0, 255, 0.2);
    }

    /* Efeito ao clicar */
    div.stButton > button:active {
        transform: scale(0.95); /* Diminui levemente como se afundasse */
        background-color: #7f00ff !important;
    }

    /* BOTÃO GERAR (ESTILO ESPECIAL) */
    .btn-final > div > button {
        background-color: #7f00ff;
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(127, 0, 255, 0.4);
    }
    .btn-final > div > button:hover {
        background-color: #9133ff;
        box-shadow: 0 6px 20px rgba(127, 0, 255, 0.6);
    }

    /* CONTAINER DE SENSI E BARRAS */
    .sensi-container {
        background-color: #161a25;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #1e2230;
    }
    .status-banner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        border-bottom: 1px solid #2a2f3f;
        padding-bottom: 10px;
    }
    .status-badge {
        color: #00ff00;
        padding: 5px 15px;
        border-radius: 8px;
        font-weight: bold;
        border: 1px solid #00ff00;
        background: rgba(0, 255, 0, 0.05);
    }
    .bar-bg { background-color: #2a2f3f; border-radius: 10px; height: 12px; width: 100%; }
    .bar-fill {
        background: linear-gradient(90deg, #7f00ff, #ff0000);
        height: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. INTERFACE
# ==============================================================================
st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.write("###")

col_so1, col_so2 = st.columns(2)
with col_so1: st.button("ANDROID", use_container_width=True)
with col_so2: st.button("iOS", use_container_width=True)

modelo = st.text_input("MODELO DO CELULAR", placeholder="Ex: Redmi Note 11")

col_h1, col_h2 = st.columns(2)
with col_h1: ram = st.selectbox("MEMÓRIA RAM", ["4 GB", "6 GB", "8 GB", "12 GB"])
with col_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

st.write("###")
st.markdown("#### ⚡ OTIMIZAÇÃO")
st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("MIRA NÃO PASSAR")

st.write("---")

# ==============================================================================
# 4. BOTÃO GERAR E RESULTADO
# ==============================================================================
st.markdown('<div class="btn-final">', unsafe_allow_html=True)
if st.button("GERAR CONFIGURAÇÃO"):
    if modelo:
        with st.spinner("Injetando..."):
            time.sleep(1.5)
        
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        st.markdown(f'<div class="status-banner"><span style="color:white; font-weight:bold;">{modelo.upper()}</span><span class="status-badge">ATIVADO</span></div>', unsafe_allow_html=True)
        
        opcoes = ["GERAL", "PONTO VERMELHO", "MIRA 2X", "MIRA 4X"]
        for op in opcoes:
            val = random.randint(150, 198)
            perc = (val/200)*100
            st.markdown(f'<div style="display:flex; justify-content:space-between; color:white; font-size:14px; margin-bottom:5px;"><span>{op}</span><span>{val}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bar-bg"><div class="bar-fill" style="width:{perc}%;"></div></div><br>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Digite o modelo!")
st.markdown('</div>', unsafe_allow_html=True)
