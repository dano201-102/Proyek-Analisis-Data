import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/day.csv")

# Konversi kolom tanggal
df['dteday'] = pd.to_datetime(df['dteday'])

# Judul Dashboard
st.title("🚴 Bike Sharing Dashboard")

# Fitur Interaktif: Filter Cuaca
weather_options = ['All Weathers'] + list(df['weathersit'].unique())
selected_weather = st.selectbox('Pilih Kondisi Cuaca:', weather_options)

if selected_weather != 'All Weathers':
    filtered_df = df[df['weathersit'] == selected_weather]
else:
    filtered_df = df

st.markdown("Dashboard ini menyajikan analisis peminjaman sepeda berdasarkan faktor cuaca dan lainnya.")

# Menampilkan Ringkasan Data
st.subheader("📌 Ringkasan Data")
st.write(filtered_df.describe())

# Visualisasi Tren Peminjaman Sepeda Harian
st.subheader("📅 Tren Peminjaman Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['dteday'], df['cnt'], marker='o', linestyle='-', alpha=0.3, label='Keseluruhan Data')
ax.plot(filtered_df['dteday'], filtered_df['cnt'], marker='o', linestyle='-', color='red', label='Filtered Data')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.legend()
st.pyplot(fig)

# Visualisasi Faktor yang Mempengaruhi Sedikitnya Peminjaman
st.subheader("🔍 Faktor yang Mempengaruhi Peminjaman Rendah")
low_demand = df[df['cnt'] < df['cnt'].quantile(0.25)]
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=low_demand['season'], y=low_demand['cnt'], ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Tambahkan visualisasi tambahan untuk faktor lain
st.subheader("📉 Pengaruh Cuaca Terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=df['weathersit'], y=df['cnt'], ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Tambahkan opsi filter tambahan
st.subheader("🎚️ Filter Data Berdasarkan Musim")
season_options = ['All Seasons'] + list(df['season'].unique())
selected_season = st.selectbox('Pilih Musim:', season_options)

if selected_season != 'All Seasons':
    df = df[df['season'] == selected_season]

st.write("Menampilkan data untuk musim:", selected_season)
