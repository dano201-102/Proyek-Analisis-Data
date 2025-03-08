import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/day.csv")

# Judul Dashboard
st.title("🚴 Bike Sharing Dashboard")
st.markdown("Dashboard ini menyajikan analisis peminjaman sepeda berdasarkan faktor cuaca dan lainnya.")

# Menampilkan Ringkasan Data
st.subheader("📌 Ringkasan Data")
st.write(df.describe())

# Visualisasi Jumlah Peminjaman Sepeda Berdasarkan Cuaca
st.subheader("🌦️ Peminjaman Sepeda Berdasarkan Cuaca")
weather_counts = df.groupby("weathersit")["cnt"].sum()
weather_labels = {1: "Cerah", 2: "Berawan", 3: "Hujan", 4: "Salju"}
weather_counts = weather_counts.rename(index=weather_labels)

fig, ax = plt.subplots()
weather_counts.plot(kind="bar", color=["#2ECC71", "#F1C40F", "#E74C3C", "#3498DB"], ax=ax)
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_xlabel("Cuaca")
ax.set_title("Total Peminjaman Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Analisis Faktor yang Mempengaruhi Peminjaman Sepeda
st.subheader("📉 Faktor yang Mempengaruhi Peminjaman Sepeda")
correlation = df.corr()[["cnt"]].sort_values(by="cnt", ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Korelasi Faktor dengan Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Kesimpulan
st.subheader("🔍 Kesimpulan")
st.markdown("- **Cuaca cerah** memiliki jumlah peminjaman sepeda tertinggi.")
st.markdown("- **Suhu memiliki dampak terbesar** terhadap peminjaman sepeda.")
st.markdown("- **Kelembaban tinggi dan angin kencang** menurunkan jumlah peminjaman sepeda.")
