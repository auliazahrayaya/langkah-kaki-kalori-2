import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Langkah & Kalori", page_icon="🔥", layout="wide")
st.title("🔥 Dashboard Langkah Kaki & Kalori + Interpolasi")

uploaded_file = st.file_uploader("Upload data CSV (kolom: steps, calories)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Asli")
    st.write(df)

    df_inter = df.copy()
    df_inter['steps'] = df_inter['steps'].interpolate()
    df_inter['calories'] = df_inter['calories'].interpolate()

    st.subheader("Data Setelah Interpolasi")
    st.write(df_inter)

    fig, ax = plt.subplots()
    ax.plot(df_inter['steps'], df_inter['calories'], marker="o")
    ax.set_xlabel("Steps")
    ax.set_ylabel("Calories")
    st.pyplot(fig)

else:
    st.info("Upload file CSV untuk melihat hasil interpolasi.")
