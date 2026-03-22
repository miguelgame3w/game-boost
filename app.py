import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE (Design e Layout Clean)
# ==============================================================================
st.set_page_config(
    page_title="GAME BOOST PRO",
    page_icon="⚡",
    layout="centered", # Centralizado igual app de celular
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CSS AVANÇADO - CORREÇÃO DE CORES E ANIMAÇÕES
# ==============================================================================
st.markdown("""
    <style>
    /* Fundo Escuro Profundo e Texto Claro (Fica legível) */
    .main { 
        background-color: #0b0d13; 
        color: #e1e3e8 !important; /* Texto claro padrão */
        font-family: 'Segoe UI', system-ui, sans-serif; 
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Título (Discreto, igual print) */
    .app-title { color: #888; text-align: center; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-top: -50px; margin-bottom: 30px;}

    /* Contêineres de Entrada e Texto DENTRO delas */
    .stTextInput>div>div>input {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
        color: white !important; /* TEXTO BRANCO NA CAIXA */
        font-size: 16px;
    }
    label { color: #bbb !important; font-size: 12px !important; text-transform: uppercase; font-weight: bold;}

    /* --- SLIDER CUSTOMIZADO (DPI) --- */
    .stSlider > div > div > div > div { background: #ff4b4b; } /* Cor da barra preenchida */
    .stSlider > div > div > div > div[data-testid="stSliderThumb"] { background-color: #ff4b4b; border: 2px solid white;} /* A bolinha */
    
    /* Display da DPI (O numerozinho vermelho no canto) */
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

    /* --- BOTOÕES DE SELEÇÃO DE S.O. (ANDROID/iOS) COM ANIMAÇÃO ROXA --- */
    div.stButton > button { # Estilo básico
        border-radius: 12px;
        border: 1px solid #2a2f3f;
        width: 100%;
        padding: 15px;
        font-weight: bold;
        transition: all 0.3s ease; # Animação suave
    }
    div.stButton > button:first-child { # Botão Android (Ativo)
        background-color: #ff4b4b;
        color: white;
        border: none;
    }
    div.stButton > button:first-child:hover { # Efeito de passar o dedo (Android)
        background-color: #6a0dad; # ROXO NO HOVER
        box-shadow: 0 0 10px rgba(106, 13, 173, 0.5);
    }
    div.stButton > button:last-child { # Botão iOS (Inativo)
        background-color: #1a1e29;
        color: #ccc !important; /* Texto claro no inativo */
    }
    div.stButton > button:last-child:hover { # Efeito de passar o dedo (iOS)
        background-color: #6a0dad; # ROXO NO HOVER
        color: white !important;
        box-shadow: 0 0 10px rgba(106, 13, 173, 0.5);
    }

    /* --- CHECKBOXES DE OTIMIZAÇÃO E TEXTO LEGÍVEL --- */
    .stCheckbox label div { color: #eee !important; font-size: 14px; font-weight: 500;} /* TEXTO LEGÍVEL */
    .stCheckbox div[data-testid="stMarkdownContainer"] p { color: #eee; }
    
    /* A caixinha do Checkbox quando marcada */
    .stCheckbox input[type="checkbox"]:checked + div { background-color: #ff4b4b !important; border-color: #ff4b4b !important;}

    /* Botão Principal Final COM ANIMAÇÃO ROXA */
    .main-btn>div>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        transition: all 0.4s ease; # Animação suave
    }
    .main-btn>div>button:hover { 
        background-color: #6a0dad; # ROXO NO HOVER
        box-shadow: 0 6px 20px rgba(106, 13, 173, 0.6);
        transform: scale(1.02); # Dá um 'charm' pulando um pouquinho
    }

    /* Cards de Sensi */
    .sensi-card {
        background-color: #11141d;
        border: 1px solid #1e2230;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
    }
    .sensi-card p { margin: 0; padding: 0; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LAYOUT E CONTEÚDO DO APP
# ==============================================================================

# Título discreto
st.markdown('<div class="app-title">GAME BOOST PRO</div>', unsafe_allow_html=True)

# --- SELEÇÃO DE SISTEMA (Igual print 1) ---
st.write("---")
col_so1, col_so2 = st.columns(2)
with col_so1: st.button("ANDROID", key="btn_android")
with col_so2: st.button("iOS", key="btn_ios")

# --- MODELO DO CELULAR ---
modelo = st.text_input("MODELO DO TE...", placeholder="Ex: Redmi note 11")

# --- BATER & ARMAZENAMENTO ---
col_in1, col_in2 = st.columns(2)
with col_in1: ram = st.text_input("BATER (RAM)", placeholder="8 GB")
with col_in2: storage = st.text_input("ARMAZENAMENTO", placeholder="256 GB")

# --- DPI PERSONALIZADA (Com display vermelho igual print) ---
st.write("###")
st.write("⚡ DPI PERSONALIZADA")
# Lógica para mostrar o número dinâmico no estilo do print
dpi_val = st.slider("", 100, 1000, 1000, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val}</div>', unsafe_allow_html=True)
st.write("<div style='display:flex; justify-content:space-between; color:#555; font-size:10px;'><span>MIN</span><span>MÁXIMO</span></div>", unsafe_allow_html=True)

# --- FUNÇÕES E OTIMIZAÇÃO (Igual print 2) ---
st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
with st.container():
    check_fps = st.checkbox("FPS A MILHÃO (120+ FPS)", value=True)
    check_ensino = st.checkbox("MÉTODO ENSINO MÉDIO COMPLETO")
    check_mira = st.checkbox("MIRA NAO PASSAR")

# ==============================================================================
# 4. BOTÃO PRINCIPAL E LÓGICA DE SENSI
# ==============================================================================
st.write("---")
# Usamos uma chave CSS personalizada para o botão final
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
run_btn = st.button("GERAR SENSI DE ELITE V7")
st.markdown('</div>', unsafe_allow_html=True)

if run_btn:
    if not modelo or not ram:
        st.error("⚠️ Preencha o modelo e a RAM!")
    else:
        # Barra de progresso Clean
        with st.spinner("Calibrando IA para seu hardware..."):
            time.sleep(2)
        
        st.balloons()
        st.success(f"SENSI GERADA PARA: {modelo.upper()}")
        
        # Resultados estilo Card Clean
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f'<div class="sensi-card"><p style="color:#aaa;">GERAL</p><p style="color:#ff4b4b; font-size:30px; font-weight:bold;">{random.randint(95,100)}</p></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="sensi-card"><p style="color:#aaa;">RED DOT</p><p style="color:#ff4b4b; font-size:30px; font-weight:bold;">{random.randint(94,99)}</p></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="sensi-card"><p style="color:#aaa;">MIRA 2X</p><p style="color:#ff4b4b; font-size:30px; font-weight:bold;">{random.randint(92,98)}</p></div>', unsafe_allow_html=True)
        with c4: st.markdown(f'<div class="sensi-card"><p style="color:#aaa;">MIRA 4X</p><p style="color:#ff4b4b; font-size:30px; font-weight:bold;">{random.randint(90,96)}</p></div>', unsafe_allow_html=True)

        st.divider()
        st.link_button("📱 SEGUE NO TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:10px;'>Powered by 3W Miguel Pro Engine</p>", unsafe_allow_html=True)
