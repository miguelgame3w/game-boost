import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE & SEO (PARA APARECER NO GOOGLE)
# ==============================================================================
st.set_page_config(
    page_title="GameBoost IA - Sensi Xit Pro 2026",
    page_icon="😈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Meta tags ocultas para ajudar na busca "GameBoost IA"
st.markdown('<meta name="description" content="GameBoost IA - O melhor gerador de sensibilidade e DPI para Android e iOS.">', unsafe_allow_html=True)
st.markdown('<meta name="keywords" content="gameboost ia, sensi xit, ff sensi, dpi mobile, 3w miguel">', unsafe_allow_html=True)

# ==============================================================================
# 2. CSS PERSONALIZADO - DESIGN "VILÃO" E BARRAS VERMELHAS
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO NEON GAMEBOOST IA */
    .xit-title-glow {
        color: #ff0000; text-align: center; font-weight: 800; font-size: 40px;
        text-transform: uppercase; text-shadow: 0 0 15px #ff0000;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

    /* BOTÕES DE SISTEMA */
    div.stButton > button {
        background-color: #1a1e29; color: #888; border-radius: 10px;
        border: 1px solid #2a2f3f; font-weight: bold; width: 100%; transition: 0.3s;
    }
    
    /* BOTÃO SELECIONADO (ROXO FIXO) */
    div.stButton > button[kind="primary"] {
        background-color: #7f00ff !important; color: white !important;
        border: none !important; box-shadow: 0 0 15px rgba(127, 0, 255, 0.4);
    }

    /* SLIDER E DISPLAY DPI */
    .stSlider > div > div > div > div { background: #7f00ff; }
    .dpi-display {
        background-color: #210a0a; color: #ff4b4b; border: 1px solid #ff4b4b;
        padding: 5px 12px; border-radius: 8px; font-weight: bold;
        float: right; margin-top: -45px;
    }

    /* CARD DE RESULTADO (ESTILO IGUAL AO PRINT) */
    .sensi-container {
        background-color: #10121a; border-radius: 15px; padding: 25px;
        border: 1px solid #1e2230; margin-top: 20px;
    }
    .bar-bg { background-color: #1e2230; border-radius: 10px; height: 10px; width: 100%; }
    .bar-fill {
        background: #ff0000; /* Vermelho do print */
        height: 100%; border-radius: 10px; box-shadow: 0 0 8px rgba(255, 0, 0, 0.4);
    }
    
    .status-badge {
        color: #00ff00; padding: 4px 10px; border-radius: 5px;
        border: 1px solid #00ff00; font-size: 11px; font-weight: bold;
        background: rgba(0, 255, 0, 0.1);
    }

    .stCheckbox input[type="checkbox"]:checked + div {
        background-color: #7f00ff !important; border-color: #7f00ff !important;
    }
    .stTextInput input { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LÓGICA DE MEMÓRIA (BOTÕES ROXOS)
# ==============================================================================
if 'plataforma' not in st.session_state:
    st.session_state.plataforma = "ANDROID"

st.markdown('<div class="xit-title-glow">🛡️ GAMEBOOST IA</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; margin-top:-10px;'>V8.5 // POWERED BY 3W MIGUEL</p>", unsafe_allow_html=True)

# Seleção de Sistema
st.write("###")
col_so1, col_so2 = st.columns(2)
with col_so1:
    if st.button("ANDROID", type="primary" if st.session_state.plataforma == "ANDROID" else "secondary"):
        st.session_state.plataforma = "ANDROID"
        st.rerun()
with col_so2:
    if st.button("iOS", type="primary" if st.session_state.plataforma == "iOS" else "secondary"):
        st.session_state.plataforma = "iOS"
        st.rerun()

# Dica dinâmica (Redmi ou iPhone)
dica = "Ex: Redmi Note 11" if st.session_state.plataforma == "ANDROID" else "Ex: iPhone 13"

# Inputs de Dados
st.write("###")
modelo = st.text_input("MODELO DO DISPOSITIVO", placeholder=dica)

c_h1, c_h2 = st.columns(2)
with c_h1: ram = st.selectbox("MEMÓRIA RAM", ["2 GB", "4 GB", "6 GB", "8 GB", "12 GB", "16 GB"], index=2)
with c_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

# Slider DPI
st.write("###")
st.write("⚡ AJUSTE DE DPI")
dpi_val = st.slider("", 100, 1000, 814, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val} DPI</div>', unsafe_allow_html=True)

st.write("###")
st.markdown("#### FUNÇÕES DE OTIMIZAÇÃO")
st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("AIMLOCK (MIRA GRUDANTE)")
st.checkbox("REGEDIT BY 3W MIGUEL")

st.write("---")

# ==============================================================================
# 4. GERAÇÃO DE RESULTADOS (OCUPANDO O ESPAÇO VAZIO)
# ==============================================================================
if st.button("🚀 INICIAR GAMEBOOST (SENSI XIT)", use_container_width=True, type="primary"):
    if not modelo:
        st.error("Digite o modelo do aparelho primeiro!")
    else:
        with st.spinner("Calibrando GameBoost IA..."):
            time.sleep(2)
        
        # CONTAINER DE RESULTADO
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        
        # Cabeçalho com o Modelo e Status (Preenche o vazio)
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <span style="color:white; font-size:22px; font-weight:bold;">📱 {modelo.upper()}</span>
                <span class="status-badge">ATIVADO</span>
            </div>
            <div style="margin-bottom: 25px; font-size: 13px; color: #888; border-bottom: 1px solid #1e2230; padding-bottom: 10px;">
                <span>🎯 {dpi_val} DPI</span> &nbsp;&nbsp; <span>💾 {ram} RAM</span> &nbsp;&nbsp; <span>🔥 {st.session_state.plataforma}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Gerador de números de sensibilidade
        sensis = {
            "GERAL": random.randint(175, 198),
            "PONTO VERMELHO": random.randint(165, 188),
            "MIRA 2X": random.randint(145, 170),
            "MIRA 4X": random.randint(130, 155),
            "AWM": random.randint(110, 135),
            "OLHADINHA": random.randint(100, 125)
        }
        
        for item, val in sensis.items():
            perc = (val/200)*100
            st.markdown(f'''
                <div style="display:flex; justify-content:space-between; color:white; font-size:14px; margin-bottom:5px;">
                    <span style="color:#aaa; font-weight:600;">{item}</span><span style="font-weight:bold; color:white;">{val}</span>
                </div>
                <div class="bar-bg"><div class="bar-fill" style="width:{perc}%;"></div></div><br>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botões de Rodapé
        st.write("###")
        col_end1, col_end2 = st.columns(2)
        with col_end1: st.button("🔄 Redefinir", use_container_width=True)
        with col_end2: st.button("📄 Copiar Sensi", use_container_width=True, type="primary")

st.markdown("<p style='text-align:center; color:#222; font-size:10px; margin-top:50px;'>GAMEBOOST IA © 2026 - BY 3W MIGUEL</p>", unsafe_allow_html=True)
