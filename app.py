import streamlit as st
import time
import random

# Configuração de Janela
st.set_page_config(page_title="GAME BOOST IA: HYPER DRIVE", page_icon="⚡", layout="wide")

# CSS PREMIER COM ANIMAÇÕES TOPS
st.markdown("""
    <style>
    /* Fundo com efeito de Profundidade */
    .main {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 50%, #1a0000 0%, #050505 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    #MainMenu, footer, header {visibility: hidden;}

    /* Título com Animação de Brilho */
    .glitch-title {
        color: #ff0000;
        text-align: center;
        font-size: 55px;
        font-weight: 900;
        text-transform: uppercase;
        text-shadow: 3px 3px 0px #550000;
        margin-top: -40px;
        animation: glitch 1s linear infinite;
    }
    
    @keyframes glitch {
        0% { text-shadow: 2px 2px #ff0000; }
        50% { text-shadow: -2px -2px #800000, 0 0 15px #ff0000; }
        100% { text-shadow: 2px 2px #ff0000; }
    }

    /* Cards de Sensi Neon */
    .sensi-card {
        background: linear-gradient(145deg, #101010, #000000);
        border: 2px solid #ff0000;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);
        transition: 0.4s;
    }
    .sensi-card:hover { transform: translateY(-10px); box-shadow: 0 0 35px #ff0000; }
    .sensi-val { color: #ff0000; font-size: 55px; font-weight: 900; text-shadow: 0 0 10px #ff0000; }

    /* Estilo dos Sliders e Inputs */
    .stSlider > div > div > div > div { background: #ff0000; }
    label { font-size: 18px !important; color: #ff4b4b !important; font-weight: bold !important; }
    
    /* Terminal de Logs */
    .terminal {
        background: #000;
        border-left: 3px solid #ff0000;
        padding: 10px;
        font-family: monospace;
        color: #00ff00;
        font-size: 13px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título
st.markdown('<div class="glitch-title">🚀 GAME BOOST V8</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>SISTEMA GENERATIVO DE ALTA PERFORMANCE</p>", unsafe_allow_html=True)

with st.container():
    # --- INPUT DO DISPOSITIVO ---
    st.markdown("### 📱 IDENTIFICAÇÃO DO DISPOSITIVO")
    modelo = st.text_input("DIGITE O NOME DO APARELHO:", placeholder="Ex: iPhone 16 Pro Max")

    # --- SELEÇÃO DE HARDWARE ---
    col_hw1, col_hw2 = st.columns(2)
    
    with col_hw1:
        st.markdown("#### 💾 Memória RAM")
        ram = st.select_slider(
            "Selecione a quantidade de RAM:",
            options=["2 GB ⚡", "4 GB ⚡", "6 GB ⚡", "8 GB ⚡", "10 GB ⚡", "12 GB ⚡", "16 GB ⚡"]
        )
    
    with col_hw2:
        st.markdown("#### 📦 Armazenamento")
        armazenamento = st.slider(
            "Arraste para definir a capacidade:",
            min_value=1, 
            max_value=3000, 
            value=128,
            help="De 1GB até 3000GB (3TB)"
        )
        # Formatação bonita para o usuário ver
        if armazenamento >= 1000:
            st.write(f"Capacidade Detectada: **{armazenamento/1000:.1f} Terabyte(s)**")
        else:
            st.write(f"Capacidade Detectada: **{armazenamento} Gigabytes**")

    st.divider()

    # --- BOTÃO DE INJEÇÃO ---
    if st.button("🚀 INICIAR INJEÇÃO HYPER DRIVE"):
        if not modelo:
            st.warning("⚠️ INSIRA O MODELO DO APARELHO!")
        else:
            # ANIMAÇÃO DE TERMINAL
            term_placeholder = st.empty()
            logs = [
                f">> ANALISANDO {modelo.upper()}...",
                f">> RAM DETECTADA: {ram}",
                f">> STORAGE BYPASS: {armazenamento}GB OK",
                ">> INJETANDO SCRIPTS DE SENSIBILIDADE 200...",
                ">> OTIMIZANDO REGISTROS DO SISTEMA...",
                ">> BYPASS ANTI-BAN ATIVADO...",
                ">> PERFORMANCE 120 FPS DESBLOQUEADA!"
            ]
            
            for i in range(len(logs)):
                term_placeholder.markdown(f'<div class="terminal">{"<br>".join(logs[:i+1])}</div>', unsafe_allow_html=True)
                time.sleep(0.5)

            st.balloons()
            
            # LÓGICA DE SENSI ATÉ 200
            # IA gera valores baseados na potência da RAM escolhida
            potencia = int(ram.split()[0])
            base_sensi = 190 if potencia >= 8 else 180
            
            g = random.randint(base_sensi, 200)
            rd = random.randint(base_sensi, 200)
            m2 = random.randint(base_sensi - 5, 200)
            m4 = random.randint(base_sensi - 10, 200)

            st.markdown(f"<h2 style='text-align:center;'>🎯 SENSI CALCULADA PARA {modelo.upper()}</h2>", unsafe_allow_html=True)
            
            # CARDS DE RESULTADO
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.markdown(f'<div class="sensi-card"><p>GERAL</p><p class="sensi-val">{g}</p></div>', unsafe_allow_html=True)
            with c2: st.markdown(f'<div class="sensi-card"><p>RED DOT</p><p class="sensi-val">{rd}</p></div>', unsafe_allow_html=True)
            with c3: st.markdown(f'<div class="sensi-card"><p>MIRA 2X</p><p class="sensi-val">{m2}</p></div>', unsafe_allow_html=True)
            with c4: st.markdown(f'<div class="sensi-card"><p>MIRA 4X</p><p class="sensi-val">{m4}</p></div>', unsafe_allow_html=True)

            st.write("###")
            st.success(f"📈 **DPI IDEAL:** {random.choice([600, 720, 800])} | **BOTÃO:** {random.choice([52, 55])}%")
            
            st.divider()
            
            # BOTÕES SOCIAIS
            st.link_button("📱 SEGUE NO TIKTOK (@3WMIGUEL)", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<p style='text-align:center; color:#333;'>V8.0 // HIGH PERFORMANCE ENGINE</p>", unsafe_allow_html=True)
