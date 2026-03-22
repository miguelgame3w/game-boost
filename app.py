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
# 2. CSS AVANÇADO - DESIGN PREMIUM E ANIMAÇÕES SUAVES
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
        margin-bottom: 5px;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

    /* --- ESTILO DOS BOTÕES (ROXO QUANDO ATIVO) --- */
    div.stButton > button {
        background-color: #1a1e29; color: #888; border-radius: 12px;
        border: 1px solid #2a2f3f; font-weight: bold; transition: all 0.3s ease;
        width: 100%; padding: 12px;
    }
    
    div.stButton > button:hover { border-color: #7f00ff; color: white; transform: translateY(-2px); }
    div.stButton > button:active { transform: scale(0.95); }

    /* Lógica de cor para o botão selecionado (Primary) */
    div.stButton > button[kind="primary"] {
        background-color: #7f00ff !important; color: white !important;
        border: none !important; box-shadow: 0 0 15px rgba(127, 0, 255, 0.4);
    }

    /* CONTAINER DE SENSI E BARRAS */
    .sensi-container {
        background-color: #161a25; border-radius: 15px; padding: 20px;
        border: 1px solid #1e2230; margin-top: 20px;
    }
    .bar-bg { background-color: #2a2f3f; border-radius: 10px; height: 12px; width: 100%; }
    .bar-fill {
        background: linear-gradient(90deg, #7f00ff, #ff0000);
        height: 100%; border-radius: 10px; box-shadow: 0 0 10px rgba(127, 0, 255, 0.5);
    }
    .status-badge {
        color: #00ff00; padding: 5px 12px; border-radius: 8px;
        border: 1px solid #00ff00; font-size: 12px; font-weight: bold;
        background: rgba(0, 255, 0, 0.05);
    }
    
    /* Checkbox Roxo */
    .stCheckbox input[type="checkbox"]:checked + div {
        background-color: #7f00ff !important; border-color: #7f00ff !important;
    }
    
    /* Texto dos inputs sempre branco */
    .stTextInput input { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LÓGICA DE MEMÓRIA (SISTEMA E DICAS)
# ==============================================================================
if 'plataforma' not in st.session_state:
    st.session_state.plataforma = "ANDROID"

st.markdown('<div class="xit-title-glow">🛡️ SENSI XIT PRO</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; margin-top:-10px;'>V8.2 // PURPLE ENGINE // BY 3W MIGUEL</p>", unsafe_allow_html=True)

# --- SELEÇÃO DE SISTEMA ---
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

# Dica dinâmica baseada na escolha
dica = "Ex: Redmi Note 11" if st.session_state.plataforma == "ANDROID" else "Ex: iPhone 13"

# --- INPUTS ---
st.write("###")
modelo = st.text_input("MODELO DO DISPOSITIVO", placeholder=dica)

c_h1, c_h2 = st.columns(2)
with c_h1: ram = st.selectbox("MEMÓRIA RAM", ["4 GB", "6 GB", "8 GB", "12 GB", "16 GB"])
with c_h2: storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 128 GB")

st.write("###")
st.markdown("#### ⚡ OTIMIZAÇÃO")
st.checkbox("FPS UNLOCK (120+ FPS)", value=True)
st.checkbox("AIMLOCK (MIRA GRUDANTE)")
st.checkbox("REGEDIT MOBILE V8")

st.write("---")

# ==============================================================================
# 4. GERAÇÃO E RESULTADOS (SEM RAIOS)
# ==============================================================================
if st.button("🚀 GERAR CONFIGURAÇÃO MÍTICA", use_container_width=True, type="primary"):
    if not modelo:
        st.error(f"Digite o modelo do seu {st.session_state.plataforma}!")
    else:
        with st.spinner("Injetando Scripts Pro..."):
            time.sleep(2)
        
        st.markdown('<div class="sensi-container">', unsafe_allow_html=True)
        
        # Banner de Status
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; border-bottom: 1px solid #2a2f3f; padding-bottom: 10px;">
                <span style="color:white; font-size:20px; font-weight:bold;">📱 {modelo.upper()}</span>
                <span class="status-badge">XIT ATIVADO</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Sensis Geradas
        itens = ["GERAL", "PONTO VERMELHO", "MIRA 2X", "MIRA 4X", "AWM"]
        for item in itens:
            val = random.randint(165, 199)
            perc = (val/200)*100
            st.markdown(f'''
                <div style="display:flex; justify-content:space-between; color:white; font-size:14px; margin-bottom:5px; font-weight:bold;">
                    <span>{item}</span><span>{val}</span>
                </div>
                <div class="bar-bg"><div class="bar-fill" style="width:{perc}%;"></div></div><br>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("Sensi Injetada com Sucesso!")
        st.link_button("MEU TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<p style='text-align:center; color:#222; font-size:10px; margin-top:50px;'>3W MIGUEL XIT ENGINE © 2026</p>", unsafe_allow_html=True)
