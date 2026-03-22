import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE (Design e Layout Clean)
# ==============================================================================
st.set_page_config(
    page_title="PAINEL SENSI PRO: PURPLE EDITION",
    page_icon="⚡",
    layout="centered", # Centralizado igual app de celular
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CSS AVANÇADO - CLONANDO O VISUAL DO PRINT COM PEGADA ROXA
# ==============================================================================
st.markdown("""
    <style>
    /* Fundo Escuro Profundo do App */
    .main { 
        background-color: #0b0d13; 
        color: #e1e3e8 !important; /* Texto claro padrão, corrigido */
        font-family: 'Segoe UI', system-ui, sans-serif; 
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Título (Discreto, igual print) */
    .app-title { color: #888; text-align: center; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-top: -50px; margin-bottom: 30px;}

    /* Contêineres de Entrada (Bater, Armazenamento) e Texto DENTRO delas */
    .stTextInput>div, .stNumberInput>div, .stSelectbox>div[data-baseweb="select"] {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
        color: white !important; # Corrigido para texto branco dentro
    }
    .stTextInput input, .stNumberInput input { color: white !important; font-size: 16px;}
    label { color: #888 !important; font-size: 12px !important; text-transform: uppercase; font-weight: bold;}

    /* --- SLIDER CUSTOMIZADO (DPI) ROXO --- */
    .stSlider > div > div > div > div { background: #7f00ff; } /* Cor da barra preenchida - ROXO */
    .stSlider > div > div > div > div[data-testid="stSliderThumb"] { background-color: #7f00ff; border: 2px solid white;} /* A bolinha - ROXO */
    
    /* Display da DPI (O numerozinho no canto) - ROXO */
    .dpi-display {
        background-color: #1a1e29;
        color: #7f00ff; /* Texto ROXO */
        border: 1px solid #7f00ff; /* Borda ROXA */
        padding: 5px 10px;
        border-radius: 8px;
        font-weight: bold;
        float: right;
        margin-top: -35px;
    }

    /* --- BOTOÕES DE SELEÇÃO DE S.O. (ANDROID/iOS) COM LÓGICA DE CLIQUE ROXA --- */
    div.stButton > button { # Estilo básico inativo (Igual print 1)
        background-color: #1a1e29;
        color: #555;
        border-radius: 12px;
        border: 1px solid #2a2f3f;
        width: 100%;
        padding: 15px;
        font-weight: bold;
        transition: 0.3s; # Animação suave
    }
    
    /* Hover (Quando passa o mouse/dedo): Fica roxo suave */
    div.stButton > button:hover {
        background-color: #7f00ff50;
        color: white;
        border-color: #7f00ff;
    }

    /* Classes para o estado ATIVO (Serão aplicadas pela lógica Python) */
    .android-active { background-color: #7f00ff !important; color: white !important; border: none !important; }
    .ios-active { background-color: #7f00ff !important; color: white !important; border: none !important; }

    /* --- CHECKBOXES DE OTIMIZAÇÃO E TEXTO LEGÍVEL (Sem o vermelho feio) --- */
    .stCheckbox label span { color: #888 !important; font-size: 14px;}
    .stCheckbox div[data-testid="stMarkdownContainer"] p { color: #888; }
    
    /* A caixinha do Checkbox quando marcada: Fica ROXA */
    .stCheckbox input[type="checkbox"]:checked + div { background-color: #7f00ff !important; border-color: #7f00ff !important;}

    /* Botão Principal Final ROXO */
    .main-btn>div>button {
        width: 100%;
        background-color: #7f00ff; /* ROXO */
        color: white;
        border: none;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 4px 15px rgba(127, 0, 255, 0.3);
    }
    .main-btn>div>button:hover { background-color: #7200e6; }

    /* Cards de Sensi ROXOS */
    .sensi-card {
        background-color: #11141d;
        border: 1px solid #1e2230;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
    }
    .sensi-card p { margin: 0; padding: 0; }
    
    /* Texto dos inputs legível */
    .stTextInput>div>div>input::placeholder { color: #555; }
    .stSelectbox>div[data-baseweb="select"] div[data-testid="stMarkdownContainer"] p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. LAYOUT E CONTEÚDO DO APP
# ==============================================================================

# Título discreto
st.markdown('<div class="app-title">PAINEL SENSI PRO</div>', unsafe_allow_html=True)

# Centralizar os controles
with st.container():
    st.markdown('<div class="xit-title-glow">🛡️ PAINEL SENSI PRO</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>V6.1.1 // PURPLE GENERATIVE ENGINE // BY 3W MIGUEL</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    # --- SISTEMA DE SELEÇÃO (ANDROID/iOS) COM LÓGICA ROXA ---
    if 'sistema_operacional' not in st.session_state:
        st.session_state.sistema_operacional = 'ANDROID' # Inicia com Android ativo

    col_so1, col_so2 = st.columns(2)
    
    with col_so1:
        # Lógica para aplicar a classe 'android-active' se for Android
        cls_android = "android-active" if st.session_state.sistema_operacional == 'ANDROID' else ""
        btn_android = st.button("ANDROID", key="btn_android", type="primary" if st.session_state.sistema_operacional == 'ANDROID' else "secondary")
        if btn_android:
            st.session_state.sistema_operacional = 'ANDROID'
            st.rerun() # Atualiza a tela para mudar a cor

    with col_so2:
        # Lógica para aplicar a classe 'ios-active' se for iOS
        cls_ios = "ios-active" if st.session_state.sistema_operacional == 'iOS' else ""
        btn_ios = st.button("iOS", key="btn_ios", type="primary" if st.session_state.sistema_operacional == 'iOS' else "secondary")
        if btn_ios:
            st.session_state.sistema_operacional = 'iOS'
            st.rerun() # Atualiza a tela para mudar a cor

    # --- MODELO DO CELULAR ---
    st.write("###")
    p_holder = "Ex: Redmi note 11" if st.session_state.sistema_operacional == 'ANDROID' else "Ex: iPhone 15 Pro Max"
    modelo = st.text_input("MODELO DO TE...", placeholder=p_holder)

    # --- BATER (OPÇÃO) & ARMAZENAMENTO (ESCREVER) ---
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        # Bater (RAM) como OPÇÃO (Selectbox)
        ram = st.selectbox("BATER (RAM)", ["Selecione...", "2 GB", "4 GB", "6 GB", "8 GB", "12 GB"], index=4) # Inicia em 8GB
    with col_in2:
        # Armazenamento como campo de ESCREVER (Text Input, igual print)
        storage = st.text_input("ARMAZENAMENTO", placeholder="Ex: 256 GB")

    # --- DPI PERSONALIZADA (Com display roxo) ---
    st.write("###")
    st.write("⚡ DPI PERSONALIZADA")
    # Lógica para mostrar o número dinâmico no estilo do print, mas ROXO
    dpi_val = st.slider("", 100, 1000, 821, label_visibility="collapsed")
    st.markdown(f'<div class="dpi-display">{dpi_val}</div>', unsafe_allow_html=True)
    st.write("<div style='display:flex; justify-content:space-between; color:#555; font-size:10px;'><span>MIN</span><span>MÁXIMO</span></div>", unsafe_allow_html=True)

    # --- FUNÇÕES E OTIMIZAÇÃO (Clean, sem o vermelho feio) ---
    st.write("###")
    st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
    check_fps = st.checkbox("FPS A MILHÃO (120+ FPS)", value=True)
    check_ensino = st.checkbox("MÉTODO ENSINO MÉDIO COMPLETO")
    check_mira = st.checkbox("MIRA NÃO PASSAR")

# ==============================================================================
# 4. BOTÃO PRINCIPAL E LÓGICA DE SENSI (Resultados ROXOS)
# ==============================================================================
st.write("---")
# Usamos uma chave CSS personalizada para o botão final
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
run_btn = st.button("GERAR SENSI DE ELITE V6")
st.markdown('</div>', unsafe_allow_html=True)

if run_btn:
    if modelo == "" or ram == "Selecione..." or storage == "":
        st.error("⚠️ Preencha todos os campos do Hardware!")
    else:
        # Barra de progresso Clean
        with st.spinner("Calibrando IA Generativa para seu hardware..."):
            time.sleep(2)
        
        st.balloons()
        st.success(f"SENSI {st.session_state.sistema_operacional} GERADA PARA: {modelo.upper()} ({ram})")
        
        # Resultados estilo Card Clean, com números ROXOS
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f'<div class="sensi-card"><p style="color:#888;">GERAL</p><p style="color:#7f00ff; font-size:30px; font-weight:bold;">{random.randint(95,100)}</p></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="sensi-card"><p style="color:#888;">RED DOT</p><p style="color:#7f00ff; font-size:30px; font-weight:bold;">{random.randint(94,99)}</p></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="sensi-card"><p style="color:#888;">MIRA 2X</p><p style="color:#7f00ff; font-size:30px; font-weight:bold;">{random.randint(92,98)}</p></div>', unsafe_allow_html=True)
        with c4: st.markdown(f'<div class="sensi-card"><p style="color:#888;">MIRA 4X</p><p style="color:#7f00ff; font-size:30px; font-weight:bold;">{random.randint(90,96)}</p></div>', unsafe_allow_html=True)

        st.divider()
        st.link_button("📱 SEGUE NO TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:10px;'>Powered by 3W Miguel Purple Pro Engine</p>", unsafe_allow_html=True)
