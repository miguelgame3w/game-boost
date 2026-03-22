import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE (Design e Layout Clean)
# ==============================================================================
st.set_page_config(
    page_title="🛡️ SENSI XIT PRO",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CSS AVANÇADO - TÍTULO NEON, ROXO E LAYOUT DE BARRAS
# ==============================================================================
st.markdown("""
    <style>
    /* Fundo Escuro Profundo */
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
        margin-bottom: 5px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.8; }
        100% { opacity: 1; }
    }

    /* INPUTS E SELEÇÃO ROXA */
    .stTextInput>div, .stSelectbox>div[data-baseweb="select"] {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
    }
    
    /* BOTÃO ATIVO ROXO/VERMELHO */
    div.stButton > button {
        background-color: #1a1e29;
        color: #555;
        border-radius: 12px;
        border: 1px solid #2a2f3f;
        font-weight: bold;
    }
    
    /* ESTILO DO CHECKBOX ROXO */
    .stCheckbox input[type="checkbox"]:checked + div {
        background-color: #7f00ff !important;
        border-color: #7f00ff !important;
    }

    /* --- CONTAINER DE SENSI (LAYOUT IGUAL AO PRINT) --- */
    .sensi-container {
        background-color: #161a25;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid #1e2230;
    }
    
    /* BANNER DE STATUS (PREENCHE O VAZIO) */
    .status-banner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        padding-bottom: 10px;
        border-bottom: 1px solid #2a2f3f;
    }
    
    .status-badge {
        background-color: rgba(0, 255, 0, 0.1);
        color: #00ff00;
        padding: 5px 15px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 12px;
        border: 1px solid #00ff00;
        text-transform: uppercase;
    }

    .sensi-row { margin-bottom: 18px; }
    
    .sensi-label-group {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 14px;
        color: #ffffff;
    }
    
    .bar-bg {
        background-color: #2a2f3f;
        border-radius: 10px;
        height: 12px;
        width: 100%;
    }
    
    .bar-fill {
        background: linear-gradient(90deg, #7f00ff, #ff0000);
        height: 100%;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(127, 0, 255, 0.5);
    }
    
    /* BOTÃO GERAR */
    .btn-final > div > button {
        background-color: #7f00ff;
        color: white;
        width: 100%;
        padding: 20px;
        border-radius: 15px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(127, 0, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. INTERFACE PRINCIPAL
# ==============================================================================
st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; margin-bottom:30px;'>V7.0 // PURPLE ENGINE // BY 3W MIGUEL</p>", unsafe_allow_html=True)

# Seleção de Sistema
col_so1, col_so2 = st.columns(2)
with col_so1: st.button("ANDROID", use_container_width=True)
with col_so2: st.button("iOS", use_container_width=True)

st.write("###")
modelo = st.text_input("MODELO DO CELULAR", placeholder="Ex: Redmi Note 11")

col_h1, col_h2 = st.columns(2)
with col_h1: ram = st.selectbox("MEMÓRIA RAM", ["2 GB", "4 GB", "6 GB", "8 GB", "12 GB"], index=2)
with col_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

st.write("###")
st.markdown("#### ⚡ OTIMIZAÇÃO DE ELITE")
st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("MIRA NÃO PASSAR (RECOIL CONTROL)")
st.checkbox("SENSI 2.0 (TOUCH RESPONSE)")

st.write("---")

# ==============================================================================
# 4. LÓGICA DE GERAÇÃO E RESULTADOS
# ==============================================================================
st.markdown('<div class="btn-final">', unsafe_allow_html=True)
if st.button("GERAR CONFIGURAÇÃO MÍTICA"):
    if modelo == "":
        st.error("Digite o modelo do celular para continuar!")
    else:
        with st.spinner("Injetando scripts de sensibilidade..."):
            time.sleep(2)
        
        # DADOS DA SENSI
        sensis = {
            "GERAL": random.randint(175, 198),
            "PONTO VERMELHO": random.randint(165, 190),
            "MIRA 2X": random.randint(150, 175),
            "MIRA 4X": random.randint(130, 160),
            "AWM": random.randint(100, 125),
            "OLHADINHA": random.randint(115, 140)
        }

        # CONTAINER DE RESULTADO (PREENCHENDO O VAZIO)
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        
        # Banner de Status com Modelo e Selo Ativado
        st.markdown(f"""
            <div class="status-banner">
                <span style="font-size: 20px; font-weight: bold; color: white;">📱 {modelo.upper()}</span>
                <span class="status-badge">ATIVADO</span>
            </div>
        """, unsafe_allow_html=True)

        # Barras de Sensibilidade
        for nome, valor in sensis.items():
            porcentagem = (valor / 200) * 100
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
        
        st.success("Configuração aplicada com sucesso!")
        st.link_button("MEU TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><p style='text-align:center; color:#222; font-size:10px;'>3W MIGUEL PRO ENGINE © 2026</p>", unsafe_allow_html=True)
