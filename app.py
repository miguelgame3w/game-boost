import streamlit as st
import time
import random

# Configuração de Layout
st.set_page_config(page_title="GAME BOOST PRO", page_icon="⚡", layout="centered")

# --- CSS COM HOVER ROXO SÓLIDO E CORES DO PRINT ---
st.markdown("""
    <style>
    .main { background-color: #0b0d13; color: #e1e3e8 !important; font-family: 'Segoe UI', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Inputs e Placeholders */
    .stTextInput>div>div>input {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
        color: white !important;
    }
    label { color: #bbb !important; font-size: 12px !important; text-transform: uppercase; font-weight: bold;}

    /* Botões com efeito QUADRADO ROXO */
    div.stButton > button {
        border-radius: 12px;
        width: 100%;
        padding: 15px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    /* Hover Roxo em todos os botões */
    div.stButton > button:hover {
        background-color: #6a0dad !important; 
        color: white !important;
        border: none !important;
    }

    /* Cores Iniciais dos Botões de SO */
    .android-active { background-color: #ff4b4b !important; color: white; border: none; }
    .ios-inactive { background-color: #1a1e29 !important; color: #ccc !important; border: 1px solid #2a2f3f; }

    /* Checkboxes legíveis */
    .stCheckbox label div { color: #eee !important; font-size: 14px; }
    
    /* Slider Vermelho */
    .stSlider > div > div > div > div { background: #ff4b4b; }
    .stSlider > div > div > div > div[data-testid="stSliderThumb"] { background-color: #ff4b4b; border: 2px solid white;}

    /* Display DPI */
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
    
    /* Botão Final */
    .main-btn>div>button {
        background-color: #ff4b4b;
        color: white;
        padding: 20px;
        font-size: 18px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ALTERNÂNCIA DE SISTEMA ---
if 'so' not in st.session_state:
    st.session_state.so = 'ANDROID'

col_so1, col_so2 = st.columns(2)
with col_so1:
    if st.button("ANDROID", key="btn_android"):
        st.session_state.so = 'ANDROID'
with col_so2:
    if st.button("iOS", key="btn_ios"):
        st.session_state.so = 'iOS'

# Define o placeholder dinâmico
placeholder_text = "Ex: REDMI NOTE 5" if st.session_state.so == 'ANDROID' else "Ex: IPHONE 15 PRO MAX"

# --- INPUTS DO APP ---
modelo = st.text_input("MODELO DO TE...", placeholder=placeholder_text)

col_in1, col_in2 = st.columns(2)
with col_in1: ram = st.text_input("BATER (RAM)", placeholder="8 GB")
with col_in2: storage = st.text_input("ARMAZENAMENTO", placeholder="256 GB")

st.write("###")
st.write("⚡ DPI PERSONALIZADA")
dpi_val = st.slider("", 100, 1000, 821, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val}</div>', unsafe_allow_html=True)

st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
st.checkbox("FPS A MILHÃO (120+ FPS)", value=True)
st.checkbox("MÉTODO ENSINO MÉDIO COMPLETO")
st.checkbox("MIRA NAO PASSAR")

st.write("---")
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
if st.button("GERAR SENSI DE ELITE V7"):
    if modelo:
        with st.spinner("Injetando Scripts..."):
            time.sleep(2)
        st.balloons()
        st.success(f"SENSI {st.session_state.so} GERADA!")
        
        # Grid de resultados
        res = [random.randint(180, 200) for _ in range(4)]
        labels = ["GERAL", "RED DOT", "2X", "4X"]
        cols = st.columns(4)
        for idx, c in enumerate(cols):
            c.markdown(f"""<div style="background:#11141d; border:1px solid #1e2230; padding:10px; border-radius:12px; text-align:center;">
                <p style="color:#888; font-size:12px;">{labels[idx]}</p>
                <p style="color:#ff4b4b; font-size:24px; font-weight:bold;">{res[idx]}</p>
            </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
