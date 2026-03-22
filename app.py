import streamlit as st
import time
import random

# Configuração de Layout
st.set_page_config(page_title="GAME BOOST IA: GOD MODE", page_icon="⚡", layout="wide")

# CSS PREMIER - O MAIS BONITO QUE JÁ FIZEMOS
st.markdown("""
    <style>
    .main {
        background-color: #050505;
        background-image: radial-gradient(#220000 0.5px, transparent 0.5px);
        background-size: 20px 20px;
        color: white;
        font-family: 'Consolas', monospace;
    }
    #MainMenu, footer, header {visibility: hidden;}
    
    .glow-title {
        color: #ff0000;
        text-align: center;
        font-weight: 900;
        font-size: 60px;
        text-transform: uppercase;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 40px #ff0000;
        margin-top: -40px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .stTextInput>div>div>input {
        background-color: #000;
        color: #00ff00; /* Texto verde estilo Hacker */
        border: 2px solid #ff0000;
        border-radius: 5px;
        padding: 15px;
        font-size: 20px;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
    }

    .stButton>button {
        width: 100%;
        background: #000;
        color: #ff0000;
        border: 2px solid #ff0000;
        padding: 20px;
        font-size: 24px;
        font-weight: 900;
        text-transform: uppercase;
        box-shadow: 0 0 15px #ff0000;
        transition: 0.4s;
    }
    .stButton>button:hover { background: #ff0000; color: #000; box-shadow: 0 0 50px #ff0000; }

    .sensi-card {
        background-color: #000;
        border: 1px solid #ff0000;
        padding: 20px;
        border-radius: 0px; /* Estilo quadrado mais agressivo */
        text-align: center;
        box-shadow: inset 0 0 10px #ff0000;
    }
    .sensi-value { color: #ff0000; font-size: 70px; font-weight: 900; text-shadow: 0 0 10px #ff0000; }
    
    .terminal-text { color: #00ff00; font-size: 12px; line-height: 1; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="glow-title">GAME BOOST IA</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>V7.4.0 // GENERATIVE ENGINE // BY 3W MIGUEL</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("### [!] IDENTIFICAÇÃO DE HARDWARE")
    user_input = st.text_input("ENTER DEVICE SPECS:", placeholder="EX: IPHONE 16 PRO MAX / REDMI NOTE 15")

    st.write("###")
    col1, col2, col3 = st.columns(3)
    with col1: fps = st.toggle("FORCE 120 FPS", value=True)
    with col2: bypass = st.toggle("BYPASS ANTICHEAT", value=True)
    with col3: regedit = st.toggle("INJECT REGEDIT", value=True)

    if st.button("RUN EXECUTABLE"):
        if not user_input:
            st.error("ACCESS DENIED: DEVICE NAME REQUIRED")
        else:
            # TERMINAL HACKER EM TEMPO REAL
            terminal = st.empty()
            log_lines = []
            
            for _ in range(15):
                new_log = f">> {random.choice(['SEARCHING', 'INJECTING', 'DECRYPTING', 'BYPASSING'])}: {random.randint(1000,9999)}... OK"
                log_lines.append(new_log)
                if len(log_lines) > 5: log_lines.pop(0)
                terminal.markdown(f'<div class="terminal-text">{"<br>".join(log_lines)}</div>', unsafe_allow_html=True)
                time.sleep(0.2)

            st.balloons()
            terminal.empty()

            # LÓGICA DE SENSI 200 PRO
            input_lower = user_input.lower()
            base = 150 if "iphone" in input_lower else 185
            g = random.randint(base, 200)
            r = random.randint(base, 200)
            m2 = random.randint(base-10, 200)
            m4 = random.randint(base-15, 200)

            st.markdown(f"## >> RESULTADO PARA: {user_input.upper()}")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.markdown(f'<div class="sensi-card"><p>GERAL</p><p class="sensi-value">{g}</p></div>', unsafe_allow_html=True)
            with c2: st.markdown(f'<div class="sensi-card"><p>RED DOT</p><p class="sensi-value">{r}</p></div>', unsafe_allow_html=True)
            with c3: st.markdown(f'<div class="sensi-card"><p>2X</p><p class="sensi-value">{m2}</p></div>', unsafe_allow_html=True)
            with s4: st.markdown(f'<div class="sensi-card"><p>4X</p><p class="sensi-value">{m4}</p></div>', unsafe_allow_html=True)

            st.write("###")
            st.success(f"DPI: {random.choice([600, 720, 800])} // BOTÃO: {random.choice([52, 55])}%")
            
            st.divider()
            st.link_button("📱 TIKTOK @3WMIGUEL", "https://www.tiktok.com/@3wmiguel", use_container_width=True)

st.markdown("<p style='text-align:center; color:#222;'>INTERNAL SYSTEM v7 // NO ERRORS FOUND</p>", unsafe_allow_html=True)
