import streamlit as st
import time
import random

# ==============================================================================
# CONFIGURAÇÃO DE ELITE
# ==============================================================================
st.set_page_config(
    page_title="🛡️ SENSI XIT PRO",
    page_icon="⚡",
    layout="centered"
)

# ==============================================================================
# CSS AVANÇADO - TÍTULO NEON E LAYOUT DE BARRAS
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO MALVADO NEON VERMELHO */
    .xit-title-glow {
        color: #ff0000;
        text-align: center;
        font-weight: 800;
        font-size: 45px;
        text-transform: uppercase;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
    }

    /* BARRA DE SENSI (LAYOUT ATUALIZADO) */
    .sensi-container {
        background-color: #161a25;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #1e2230;
    }
    
    /* BANNER DE STATUS QUE PREENCHE O VAZIO */
    .status-banner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .status-badge {
        background-color: rgba(0, 255, 0, 0.1);
        color: #00ff00;
        padding: 5px 15px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 12px;
        border: 1px solid #00ff00;
    }

    .sensi-row { margin-bottom: 15px; }
    .sensi-label-group {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 14px;
        color: #e1e3e8;
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
    }
    
    .stButton > button {
        background-color: #7f00ff;
        color: white;
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Interface de Entrada
st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
modelo = st.text_input("MODELO DO CELULAR", placeholder="Ex: Redmi Note 11")
st.write("---")

if st.button("GERAR SENSI DE ELITE V7"):
    with st.spinner("Calibrando..."):
        time.sleep(1.5)
    
    # DADOS DA SENSI
    sensis = {
        "GERAL": random.randint(170, 195),
        "PONTO VERMELHO": random.randint(160, 185),
        "MIRA 2X": random.randint(140, 160),
        "MIRA 4X": random.randint(120, 145),
        "AWM": random.randint(110, 130),
        "OLHADINHA": random.randint(110, 130)
    }

    # CONTAINER DE RESULTADO (Preenchendo o vazio)
    st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
    
    # Este bloco abaixo é o que preenche o espaço que estava vazio
    st.markdown(f"""
        <div class="status-banner">
            <span style="font-size: 20px; font-weight: bold; color: white;">{modelo.upper()}</span>
            <span class="status-badge">ATIVADO</span>
        </div>
    """, unsafe_allow_html=True)

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
