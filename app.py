import streamlit as st
import time
import random

# ==============================================================================
# CONFIGURAÇÃO DE ELITE
# ==============================================================================
st.set_page_config(
    page_title="🛡️ PAINEL SENSI PRO",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# CSS AVANÇADO - TÍTULO NEON E LAYOUT DE BARRAS
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO MALVADO NEON VERMELHO */
    .xit-title-glow {
        color: #ff0000;
        text-align: center;
        font-weight: 800;
        font-size: 45px;
        text-transform: uppercase;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
        margin-bottom: 10px;
    }

    /* INPUTS E SELEÇÃO ROXA */
    .stTextInput>div, .stSelectbox>div[data-baseweb="select"] {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
    }
    
    /* BOTÃO ATIVO ROXO (ANDROID/iOS) */
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #7f00ff !important;
        color: white !important;
        border: none !important;
    }

    /* CAIXINHA ROXA QUANDO ATIVADA */
    .stCheckbox input[type="checkbox"]:checked + div {
        background-color: #7f00ff !important;
        border-color: #7f00ff !important;
    }

    /* BARRA DE SENSI (LAYOUT IGUAL AO PRINT) */
    .sensi-container {
        background-color: #161a25;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
    }
    .sensi-row {
        margin-bottom: 15px;
    }
    .sensi-label-group {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 14px;
        color: #888;
    }
    .bar-bg {
        background-color: #2a2f3f;
        border-radius: 10px;
        height: 12px;
        width: 100%;
        overflow: hidden;
    }
    .bar-fill {
        background: linear-gradient(90deg, #7f00ff, #ff0000);
        height: 100%;
        border-radius: 10px;
    }
    
    .btn-final > div > button {
        background-color: #7f00ff;
        color: white;
        width: 100%;
        padding: 15px;
        border-radius: 12px;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# INTERFACE
# ==============================================================================
st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>V7.0 // PURPLE GEN // BY 3W MIGUEL</p>", unsafe_allow_html=True)

# Seleção de Sistema
col_so1, col_so2 = st.columns(2)
with col_so1: st.button("ANDROID", use_container_width=True)
with col_so2: st.button("iOS", use_container_width=True)

modelo = st.text_input("MODELO DO CELULAR", placeholder="Ex: Redmi Note 11")

col_h1, col_h2 = st.columns(2)
with col_h1: ram = st.selectbox("BATER (RAM)", ["4 GB", "6 GB", "8 GB", "12 GB"])
with col_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
st.checkbox("FPS A MILHÃO (120+ FPS)")
st.checkbox("MÉTODO ENSINO MÉDIO COMPLETO")
st.checkbox("MIRA NÃO PASSAR")

st.markdown('<div class="btn-final">', unsafe_allow_html=True)
if st.button("GERAR SENSI DE ELITE V7"):
    with st.spinner("Processando..."):
        time.sleep(2)
    
    st.markdown(f"### 📱 SENSI PARA {modelo.upper()}")
    
    # NOVO LAYOUT DE SENSIBILIDADE EM BARRAS (IGUAL AO SEU PRINT)
    sensis = {
        "GERAL": random.randint(170, 195),
        "PONTO VERMELHO": random.randint(160, 185),
        "MIRA 2X": random.randint(140, 160),
        "MIRA 4X": random.randint(120, 145),
        "AWM": random.randint(110, 130),
        "OLHADINHA": random.randint(110, 130)
    }

    st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
    for nome, valor in sensis.items():
        porcentagem = (valor / 200) * 100 # Cálculo para a barra
        st.markdown(f"""
            <div class="sensi-row">
                <div class="sensi-label-group">
                    <span>{nome}</span>
                    <span>{valor}</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" style="width: {porcentagem}%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
