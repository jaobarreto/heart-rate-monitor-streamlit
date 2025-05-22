import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("📈 Monitor de Frequência Cardíaca (Simulado)")

min_bpm = st.sidebar.slider("BPM mínimo saudável", 30, 100, 50)
max_bpm = st.sidebar.slider("BPM máximo saudável", 100, 180, 120)

placeholder = st.empty()
bpm_data = []

for i in range(200):
    bpm = np.random.normal(75, 10) + np.random.randint(-5, 5)
    bpm = max(30, min(180, bpm))
    bpm_data.append(bpm)

    df = pd.DataFrame(bpm_data, columns=["BPM"])
    with placeholder.container():
        st.line_chart(df)

        if bpm < min_bpm or bpm > max_bpm:
            st.error(f"🚨 Alerta: BPM fora do limite! ({bpm:.1f})")
        else:
            st.success(f"✅ BPM estável: {bpm:.1f}")

    time.sleep(0.1)
