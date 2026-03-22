import streamlit as st
import time
import random

# Configuração de Layout para parecer um App
st.set_page_config(page_title="GAME BOOST PRO", page_icon="⚡", layout="centered")

# --- CSS PREMIUN (BORDA ARREDONDADA E HOVER ROXO SÓLIDO) ---
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Estilizando as Caixas de Seleção (Dropdowns) */
    div[data-baseweb="select"] > div {
        background-color: #11141d !important;
        border: 1px solid #1e2230 !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    /* Input de Texto do Modelo */
    .stTextInput>div>div>input {
        background-color: #11141d !important;
        border: 1px solid #1e2230 !important;
        border-radius: 12px !important;
        color: white !important;
    }

    /* Labels cinzas e pequenas */
    label { color: #888 !important; font-size: 11px !important; text-transform: uppercase; font-weight: bold; margin-bottom: 5px;}

    /* Botão Final com Hover Roxo */
    div.stButton > button {
        border-radius: 12px;
        width: 100%;
        padding: 15px;
        font-weight: bold;
        transition: 0.3s;
        background-color: #1a1e29;
        color: #ccc;
        border: 1px solid #2a2f3f;
    }
    div.stButton > button:hover {
        background-color: #6a0dad !important; 
        color: white !important;
        border: none !important;
    }

    /* Slider Vermelho */
    .stSlider > div > div > div > div { background: #ff4b4b; }
    .stSlider > div > div > div > div[data-testid="stSliderThumb"] { background-color: #ff4b4b; border: 2px solid white;}

    /* Display da DPI */
    .dpi-display {
        background-color: #210a0a;
        color: #ff4b4b;
        border: 1px solid #ff4b4b;
        padding: 5px 10px;
        border-radius: 8px;
        font-weight: bold;
        float: right;
        margin-top: -35px;
    }
    
    /* Botão Gerar Sensi */
    .main-btn>div>button {
        background-color: #ff4b4b !important;
        color: white !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE SISTEMA ---
if 'so' not in st.session_state:
    st.session_state.so = 'ANDROID'

col_so1, col_so2 = st.columns(2)
with col_so1:
    if st.button("ANDROID"): st.session_state.so = 'ANDROID'
with col_so2:
    if st.button("iOS"): st.session_state.so = 'iOS'

# Placeholder dinâmico para o Modelo
p_holder = "Ex: REDMI NOTE 5" if st.session_state.so == 'ANDROID' else "Ex: IPHONE 15 PRO MAX"
modelo = st.text_input("MODELO DO TE...", placeholder=p_holder)

# --- AGORA OS DOIS SÃO CAIXINHAS DE SELEÇÃO (SELECTBOX) ---
col_sel1, col_sel2 = st.columns(2)
with col_sel1:
    ram = st.selectbox("BATER (RAM)", ["2 GB", "3 GB", "4 GB", "6 GB", "8 GB", "12 GB"], index=4)
with col_sel2:
    # Mudança aqui: de text_input para selectbox
    storage = st.selectbox("ARMAZENAMENTO", ["32 GB", "64 GB", "128 GB", "256 GB", "512 GB", "1 TB"], index=3)

# --- DPI ---
st.write("###")
st.write("⚡ DPI PERSONALIZADA")
dpi_val = st.slider("", 100, 1000, 821, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val}</div>', unsafe_allow_html=True)

# --- OTIMIZAÇÃO ---
st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
st.checkbox("FPS A MILHÃO (120+ FPS)", value=True)
st.checkbox("MÉTODO ENSINO MÉDIO COMPLETO")
st.checkbox("MIRA NÃO PASSAR")

# --- BOTÃO FINAL ---
st.write("---")
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
if st.button("GERAR SENSI DE ELITE V7"):
    if modelo:
        with st.spinner("Calibrando para seu Hardware..."):
            time.sleep(2)
        st.balloons()
        st.success(f"SENSI {st.session_state.so} GERADA COM SUCESSO!")
        
        # Grid de Sensi
        res = [random.randint(190, 200) for _ in range(4)]
        labels = ["GERAL", "RED DOT", "2X", "4X"]
        cols = st.columns(4)
        for i, c in enumerate(cols):
            c.markdown(f"""<div style="background:#11141d; border:1px solid #1e2230; padding:10px; border-radius:12px; text-align:center;">
                <p style="color:#888; font-size:11px;">{labels[i]}</p>
                <p style="color:#ff4b4b; font-size:22px; font-weight:bold;">{res[i]}</p>
            </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
