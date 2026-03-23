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
# 2. CSS PERSONALIZADO (CORES DO PRINT)
# ==============================================================================
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; }
    #MainMenu, footer, header {visibility: hidden;}

    /* TÍTULO NEON */
    .xit-title-glow {
        color: #ff0000; text-align: center; font-weight: 800; font-size: 40px;
        text-transform: uppercase; text-shadow: 0 0 15px #ff0000;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

    /* BOTÕES DE SISTEMA */
    div.stButton > button {
        background-color: #1a1e29; color: #888; border-radius: 10px;
        border: 1px solid #2a2f3f; font-weight: bold; width: 100%;
    }
    
    /* BOTÃO SELECIONADO (ROXO) */
    div.stButton > button[kind="primary"] {
        background-color: #7f00ff !important; color: white !important;
        border: none !important; box-shadow: 0 0 15px rgba(127, 0, 255, 0.4);
    }

    /* SLIDER E DISPLAY DPI */
    .dpi-display {
        background-color: #210a0a; color: #ff4b4b; border: 1px solid #ff4b4b;
        padding: 5px 12px; border-radius: 8px; font-weight: bold;
        float: right; margin-top: -45px;
    }

    /* CARD DE RESULTADO */
    .sensi-container {
        background-color: #10121a; border-radius: 15px; padding: 25px;
        border: 1px solid #1e2230; margin-top: 20px;
    }
    .bar-bg { background-color: #1e2230; border-radius: 10px; height: 10px; width: 100%; }
    .bar-fill {
        background: #ff0000; /* Vermelho igual ao print */
        height: 100%; border-radius: 10px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
    }
    
    .status-badge {
        color: #00ff00; padding: 4px 10px; border-radius: 5px;
        border: 1px solid #00ff00; font-size: 11px; font-weight: bold;
        background: rgba(0, 255, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LÓGICA DE MEMÓRIA
# ==============================================================================
if 'plataforma' not in st.session_state:
    st.session_state.plataforma = "ANDROID"

st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.write("###")

# Seleção de Sistema
col_so1, col_so2 = st.columns(2)
with col_so1:
    if st.button("ANDROID", type="primary" if st.session_state.plataforma == "ANDROID" else "secondary"):
        st.session_state.plataforma = "ANDROID"
        st.rerun()
with col_so2:
    if st.button("iOS", type="primary" if st.session_state.plataforma == "iOS" else "secondary"):
        st.session_state.plataforma = "iOS"
        st.rerun()

# Dica dinâmica
dica = "Ex: Redmi Note 11" if st.session_state.plataforma == "ANDROID" else "Ex: iPhone 13"

# Inputs
st.write("###")
modelo = st.text_input("MODELO DO DISPOSITIVO", placeholder=dica)

c_h1, c_h2 = st.columns(2)
with c_h1: ram = st.selectbox("BATER (RAM)", ["2 GB", "4 GB", "6 GB", "8 GB", "12 GB", "16 GB"])
with c_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

# DPI
st.write("###")
st.write("⚡ DPI PERSONALIZADA")
dpi_val = st.slider("", 100, 1000, 814, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val} DPI</div>', unsafe_allow_html=True)

st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("SENSI 2.0 (TOUCH)")
st.checkbox("ANTI-BAN (BYPASS)")

st.write("---")

# ==============================================================================
# 4. GERAÇÃO DE RESULTADOS
# ==============================================================================
if st.button("🚀 INICIAR SENSI XIT (GOD MODE)", use_container_width=True, type="primary"):
    if not modelo:
        st.error("Digite o modelo do aparelho!")
    else:
        with st.spinner("Processando..."):
            time.sleep(2)
        
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        
        # Cabeçalho igual ao print
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <span style="color:white; font-size:22px; font-weight:bold;">{modelo.upper()}</span>
                <span class="status-badge">ATIVADO</span>
            </div>
            <div style="margin-bottom: 20px; font-size: 13px; color: #888;">
                <span>📱 {dpi_val} DPI</span> &nbsp;&nbsp; <span>⚙️ {ram}</span> &nbsp;&nbsp; <span>{st.session_state.plataforma}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Itens de Sensibilidade
        sensis = {
            "GERAL": random.randint(170, 195),
            "PONTO VERMELHO": random.randint(160, 185),
            "MIRA 2X": random.randint(140, 160),
            "MIRA 4X": random.randint(120, 140),
            "AWM": random.randint(110, 130),
            "OLHADINHA": random.randint(100, 120)
        }
        
        for item, val in sensis.items():
            perc = (val/200)*100
            st.markdown(f'''
                <div style="display:flex; justify-content:space-between; color:white; font-size:14px; margin-bottom:5px;">
                    <span style="color:#aaa;">{item}</span><span style="font-weight:bold;">{val}</span>
                </div>
                <div class="bar-bg"><div class="bar-fill" style="width:{perc}%;"></div></div><br>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botões de ação final
        st.write("###")
        c_b1, c_b2 = st.columns(2)
        with c_b1: st.button("🔄 Redefinir", use_container_width=True)
        with c_b2: st.button("📄 Copiar", use_container_width=True, type="primary")

st.markdown("<p style='text-align:center; color:#222; font-size:10px; margin-top:50px;'>PAINEL SENSI PRO © 2026</p>", unsafe_allow_html=True)
