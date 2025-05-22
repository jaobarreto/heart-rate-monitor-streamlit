import streamlit as st
import pandas as pd
import numpy as np
import time

# Configurações da página
st.set_page_config(page_title="Monitor de BPM", layout="wide")

st.title("📡 Monitor de Frequência Cardíaca (Simulação)")
st.markdown("Este painel simula a leitura de BPM com alertas em tempo real.")

# Sidebar - controles
st.sidebar.header("⚙️ Configurações")
min_bpm = st.sidebar.slider("BPM mínimo saudável", 30, 100, 50)
max_bpm = st.sidebar.slider("BPM máximo saudável", 100, 180, 120)
update_interval = st.sidebar.slider("Intervalo de atualização (segundos)", 0.1, 2.0, 0.5, step=0.1)
max_points = st.sidebar.slider("Nº de pontos no gráfico", 50, 300, 100)

# Dados simulados
bpm_data = []

# Espaços reservados para exibição
chart_placeholder = st.empty()
status_placeholder = st.empty()

# Loop de simulação
for i in range(200):  # Simula 200 leituras
    bpm = np.random.normal(loc=75, scale=8) + np.random.randint(-5, 5)
    bpm = round(np.clip(bpm, 30, 180), 1)  # Limite de valores plausíveis
    bpm_data.append(bpm)

    # Limita histórico para o gráfico
    bpm_data = bpm_data[-max_points:]

    # Atualiza o gráfico
    df = pd.DataFrame(bpm_data, columns=["BPM"])
    chart_placeholder.line_chart(df, use_container_width=True)

    # Exibe status
    with status_placeholder.container():
        if bpm < min_bpm or bpm > max_bpm:
            st.error(f"🚨 Alerta: BPM fora da faixa saudável! ({bpm} BPM)")
        else:
            st.success(f"✅ BPM dentro da faixa saudável: {bpm} BPM")

    time.sleep(update_interval)
