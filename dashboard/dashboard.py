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
weather_options = df['weathersit'].unique()
selected_weather = st.selectbox('Pilih Kondisi Cuaca:', weather_options)
filtered_df = df[df['weathersit'] == selected_weather]
st.markdown("Dashboard ini menyajikan analisis peminjaman sepeda berdasarkan faktor cuaca dan lainnya.")

# Menampilkan Ringkasan Data
st.subheader("📌 Ringkasan Data")
st.write(df.describe())

# Visualisasi Tren Peminjaman Sepeda Harian
st.subheader("📅 Tren Peminjaman Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['dteday'], df['cnt'], marker='o', linestyle='-', alpha=0.3, label='Keseluruhan Data')
ax.plot(filtered_df['dteday'], filtered_df['cnt'], marker='o', linestyle='-', color='red', label='Filtered Data')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Peminjaman Sepeda dari Waktu ke Waktu")
ax.legend()
st.pyplot(fig)

# Visualisasi Jumlah Peminjaman Sepeda Berdasarkan Cuaca
st.subheader("🌦️ Peminjaman Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots()
df.groupby('weathersit')['cnt'].mean().plot(kind='bar', alpha=0.3, label='Keseluruhan Data', ax=ax)
filtered_df.groupby('weathersit')['cnt'].mean().plot(kind='bar', color='red', label='Filtered Data', ax=ax)
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_xlabel("Cuaca")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
ax.legend()
st.pyplot(fig)

# Visualisasi Faktor yang Mempengaruhi Peminjaman Sepeda
st.subheader("📉 Faktor yang Mempengaruhi Peminjaman Sepeda")
correlation = df.corr()[['cnt']].sort_values(by='cnt', ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Korelasi Faktor dengan Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Visualisasi Peminjaman Berdasarkan Musim
st.subheader("🌱 Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
df.groupby('season')['cnt'].mean().plot(kind='bar', alpha=0.3, label='Keseluruhan Data', ax=ax)
filtered_df.groupby('season')['cnt'].mean().plot(kind='bar', color='red', label='Filtered Data', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda per Musim")
ax.legend()
st.pyplot(fig)

# Visualisasi Peminjaman Berdasarkan Hari Kerja
st.subheader("🏢 Peminjaman Sepeda Berdasarkan Hari Kerja")
fig, ax = plt.subplots()
df.groupby('workingday')['cnt'].mean().plot(kind='bar', alpha=0.3, label='Keseluruhan Data', ax=ax)
filtered_df.groupby('workingday')['cnt'].mean().plot(kind='bar', color='red', label='Filtered Data', ax=ax)
ax.set_xlabel("Hari Kerja (0 = Libur, 1 = Kerja)")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda pada Hari Kerja vs Libur")
ax.legend()
st.pyplot(fig)

# Visualisasi Peminjaman Berdasarkan Bulan
st.subheader("📆 Peminjaman Sepeda Berdasarkan Bulan")
fig, ax = plt.subplots()
df.groupby('mnth')['cnt'].mean().plot(kind='bar', alpha=0.3, label='Keseluruhan Data', ax=ax)
filtered_df.groupby('mnth')['cnt'].mean().plot(kind='bar', color='red', label='Filtered Data', ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda per Bulan")
ax.legend()
st.pyplot(fig)

# Kesimpulan
st.subheader("🔍 Kesimpulan")
st.markdown("- **Cuaca cerah** memiliki jumlah peminjaman sepeda tertinggi.")
st.markdown("- **Suhu memiliki dampak terbesar** terhadap peminjaman sepeda.")
st.markdown("- **Kelembaban tinggi dan angin kencang** menurunkan jumlah peminjaman sepeda.")
