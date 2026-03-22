import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DE ELITE (Design e Layout Clean)
# ==============================================================================
st.set_page_config(
    page_title="GAME BOOST PRO: XIT EDITION",
    page_icon="😈",
    layout="centered", # Centralizado igual app de celular
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CSS AVANÇADO - FOCO NO EFEITO ROXO SÓLIDO, ANIMAÇÕES E TELA DE INJEÇÃO
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

    /* Título discreto */
    .app-title { color: #888; text-align: center; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-top: -50px; margin-bottom: 30px;}

    /* Contêineres de Entrada */
    .stTextInput>div>div>input {
        background-color: #11141d;
        border: 1px solid #1e2230;
        border-radius: 12px;
        color: white !important;
        font-size: 16px;
    }
    label { color: #bbb !important; font-size: 12px !important; text-transform: uppercase; font-weight: bold;}

    /* --- SLIDER CUSTOMIZADO (DPI) --- */
    .stSlider > div > div > div > div { background: #ff4b4b; }
    .stSlider > div > div > div > div[data-testid="stSliderThumb"] { background-color: #ff4b4b; border: 2px solid white;}
    
    /* Display da DPI vermelho */
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

    /* --- BOTOÕES DE SELEÇÃO (ANDROID/iOS) COM HOVER ROXO SÓLIDO --- */
    div.stButton > button {
        border-radius: 12px;
        width: 100%;
        padding: 15px;
        font-weight: bold;
        transition: all 0.3s ease; # Animação suave e rápida
    }

    /* --- Botão Android (Ativo Padrão) --- */
    div.stButton > button:first-child { 
        background-color: #ff4b4b; 
        color: white;
        border: none;
    }
    /* EFEITO DE PASSAR O DEDO NO ANDROID: O QUADRADO FICA ROXO SÓLIDO */
    div.stButton > button:first-child:hover { 
        background-color: #6a0dad !important; # FUNDO ROXO SÓLIDO
        color: white !important;
        border: none !important;
    }

    /* --- Botão iOS (Inativo Padrão) --- */
    div.stButton > button:last-child { 
        background-color: #1a1e29; 
        color: #ccc !important;
        border: 1px solid #2a2f3f;
    }
    /* EFEITO DE PASSAR O DEDO NO iOS: O QUADRADO FICA ROXO SÓLIDO */
    div.stButton > button:last-child:hover { 
        background-color: #6a0dad !important; # FUNDO ROXO SÓLIDO
        color: white !important;
        border: none !important;
    }

    /* Checkboxes legíveis */
    .stCheckbox label div { color: #eee !important; font-size: 14px; font-weight: 500;}
    .stCheckbox input[type="checkbox"]:checked + div { background-color: #ff4b4b !important; border-color: #ff4b4b !important;}

    /* --- BOTÃO PRINCIPAL FINAL COM HOVER ROXO SÓLIDO --- */
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
        transition: all 0.3s ease;
    }
    /* EFEITO DE PASSAR O DEDO NO BOTÃO FINAL: O QUADRADO FICA ROXO SÓLIDO */
    .main-btn>div>button:hover { 
        background-color: #6a0dad !important; # FUNDO ROXO SÓLIDO
        color: white !important;
        box-shadow: 0 6px 20px rgba(106, 13, 173, 0.6);
        transform: scale(1.02); # Um 'charm' pulando
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

    /* ============================================================================== */
    /* --- TELA DE INJEÇÃO XIT NEON (A MÁGICA DE VOLTA) --- */
    /* ============================================================================== */
    .exit-screen {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-color: #0b0d13;
        z-index: 1000;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        opacity: 0; animation: fadeIn 0.5s forwards;
    }
    
    /* O Símbolo do Capetinha Neon */
    .exit-devil {
        color: #ff4b4b; font-size: 80px; text-shadow: 0 0 10px #ff4b4b, 0 0 20px #ff4b4b;
        margin-bottom: 20px;
    }
    
    /* Texto de Status */
    .exit-status {
        color: #6a0dad; font-size: 14px; text-transform: uppercase; font-weight: bold;
        text-align: center; letter-spacing: 1px;
    }
    
    /* Barra de Progresso Customizada para ser Neon Vermelha */
    .stProgress > div > div > div > div { background-color: #ff0000; box-shadow: 0 0 10px #ff0000; }
    
    /* Logs do Terminal (Simulação de Xit) */
    .term { color: #5f5; font-family: monospace; font-size: 12px; line-height: 1; text-align: left; width: 80%; }
    
    /* Estilo do Rodapé minimalista */
    .footer-text { color: #333; text-align: center; font-size: 12px; margin-top: 50px; }

    /* Estilos das Notificações (Alertas) */
    .stAlert { background-color: #161b22; border: 1px solid #ff0000; color: #ff4b4b; border-radius: 10px; }
    
    /* Estilos dos Checkboxes Neon */
    .stCheckbox label div { color: #aaa !important; font-weight: bold; }
    .stCheckbox input[type="checkbox"]:checked + div { background-color: #ff0000 !important; border-color: #ff0000 !important; box-shadow: 0 0 10px #ff0000;}

    /* Estilos da Sensibilidade Xit Mítica */
    .xit-sensi-box {
        background-color: #000;
        border: 2px solid #ff0000;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4);
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .xit-sensi-label { color: #888; font-size: 14px; text-transform: uppercase; font-weight: bold; }
    .xit-sensi-value { color: #ff0000; font-size: 55px; font-weight: 800; text-shadow: 0 0 10px #ff0000; }

    /* Título com Brilho Neon Vermelho Pulsante */
    .xit-title-glow {
        color: #ff0000;
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 55px;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000;
        margin-bottom: 5px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.8; } 100% { opacity: 1; } }

    /* Campo de Entrada de Texto com Estilo Xit */
    .xit-input>div>div>input {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        color: white !important;
        font-size: 16px;
    }
    label { color: #aaa !important; font-weight: bold; }

    /* Botão Principal com Efeito de Pulso Neon */
    .xit-btn>div>button {
        width: 100%;
        background: linear-gradient(135deg, #800000 0%, #ff0000 100%);
        color: white;
        border: none;
        padding: 18px;
        font-size: 22px;
        font-weight: 800;
        border-radius: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0px 5px 20px rgba(255, 0, 0, 0.5);
        transition: all 0.3s ease;
    }
    .xit-btn>div>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 30px rgba(255, 0, 0, 0.8);
        background: linear-gradient(135deg, #ff0000 0%, #800000 100%);
    }

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. CONTEÚDO PRINCIPAL DO PAINEL
# ==============================================================================

# Título discreto
st.markdown('<div class="app-title">GAME BOOST PRO: XIT EDITION</div>', unsafe_allow_html=True)

# --- SELEÇÃO DE SISTEMA (Os botões que vão ficar roxos) ---
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

# --- DPI PERSONALIZADA ---
st.write("###")
st.write("⚡ DPI PERSONALIZADA")
dpi_val = st.slider("", 100, 1000, 1000, label_visibility="collapsed")
st.markdown(f'<div class="dpi-display">{dpi_val}</div>', unsafe_allow_html=True)
st.write("<div style='display:flex; justify-content:space-between; color:#555; font-size:10px;'><span>MIN</span><span>MÁXIMO</span></div>", unsafe_allow_html=True)

# --- FUNÇÕES E OTIMIZAÇÃO ---
st.write("###")
st.markdown("#### FUNÇÕES E OTIMIZAÇÃO")
with st.container():
    cb1, cb2, cb3, cb4 = st.columns(4)
    with cb1: fps = st.checkbox("🔥 FPS UNLOCK (120 FPS)", value=True)
    with cb2: sensi = st.checkbox("🎯 SENSI 2.0 (TOUCH)")
    with cb3: net = st.checkbox("🌐 PING ZERO (ROUTE)")
    with cb4: anticheat = st.checkbox("🛡️ ANTI-BAN (BYPASS)")

# ==============================================================================
# 4. BOTÃO PRINCIPAL (O outro que vai ficar roxo)
# ==============================================================================
st.write("---")
# Chave CSS personalizada
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
run_btn = st.button("INICIAR SENSI XIT (GOD MODE)")
st.markdown('</div>', unsafe_allow_html=True)

if run_btn:
    if not modelo or not ram:
        st.error("⚠️ Preencha o modelo e a RAM!")
    else:
        # --- A MÁGICA DA TELA DE INJEÇÃO XIT (Estilo Hacker Matrix) ---
        status_text = st.empty()
        prog_bar = st.progress(0)
        
        # Textos de Log para dar Hype (Baseado no V3 anterior)
        logs = [
            f"🔍 ANALISANDO HARDWARE DO {modelo.upper()}...",
            "📁 ACESSANDO REGISTROS DO SISTEMA... [OK]",
            "🛡️ PROTOCÓLO ANTI-BAN BYPASS: ATIVADO... [OK]",
            "🎯 CALIBRANDO TOUCH SCREEN DE ALTA PRECISÃO...",
            "🔥 DESBLOQUEANDO LIMITE DE 120 FPS...",
            "🌐 OTIMIZANDO ROTA DE CONEXÃO (PING ZERO)...",
            "🎯 CALCULANDO SENSIBILIDADE XIT MÍTICA...",
            "✅ SINCRONIZANDO SCRIPTS COM O FREE FIRE... [SUCESSO]"
        ]

        # Início da Injeção (Hype Máximo)
        for i in range(101):
            # Atualizar texto de log aleatoriamente (Efeito Matrix)
            if i % 12 == 0:
                # Agora o texto tem aquela cor verde hacker estilo o terminal V7
                status_text.markdown(f'<p style="color:#5f5; font-family:monospace; text-align:center;">{random.choice(logs)}</p>', unsafe_allow_html=True)
            
            # Barra de progresso Neon Vermelha (Via Streamlit com CSS customizado no V5)
            prog_bar.progress(i)
            time.sleep(0.04) # Velocidade da animação

        # TELA FINAL COM SÍMBOLO DO CAPETINHA NEON (Estilo V3, mas Clean)
        status_text.empty()
        prog_bar.empty()
        
        st.balloons()
        
        # O Símbolo do Capetinha Neon Vermelho (God Mode)
        st.markdown('<div class="exit-devil">😈</div>', unsafe_allow_html=True)
        # Texto de Status (God Mode)
        st.markdown('<div class="exit-status">SENSI XIT MÍTICA APLICADA!<br>SEUS TIROS AGORA SÃO AUTOMÁTICOS</div>', unsafe_allow_html=True)
        
        time.sleep(2) # Segurar a tela final por 2 segundos antes de mostrar os resultados
        
        # Mostrar os Resultados Míticos Estilo V3 Neon
        st.divider()
        st.markdown(f'### ✅ OTIMIZAÇÃO CONCLUÍDA NO {modelo.upper()}!')
        
        s_col1, s_col2, s_col3, s_col4 = st.columns(4)
        
        # Lógica de Sensi "Mítica" (Sempre Alta - Xit)
        g, r, m2, m4 = "190", "195", "185", "180"

        # Cartões Neon Vermelhos Pulsantes (Xit Edition)
        with s_col1:
            st.markdown(f'<div class="xit-sensi-box"><div class="xit-sensi-label">GERAL</div><div class="xit-sensi-value">{g}</div></div>', unsafe_allow_html=True)
        with s_col2:
            st.markdown(f'<div class="xit-sensi-box"><div class="xit-sensi-label">RED DOT</div><div class="xit-sensi-value">{r}</div></div>', unsafe_allow_html=True)
        with s_col3:
            st.markdown(f'<div class="sensi-card"><div class="sensi-label">MIRA 2X</div><div class="sensi-value">{m2}</div></div>', unsafe_allow_html=True)
        with s_col4:
            st.markdown(f'<div class="sensi-card"><div class="sensi-label">MIRA 4X</div><div class="sensi-value">{m4}</div></div>', unsafe_allow_html=True)

        st.divider()
        st.link_button("📱 SEGUE NO TIKTOK (@3wmiguel)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:10px;'>Powered by 3W Miguel Pro Engine Xit Edition</p>", unsafe_allow_html=True)
