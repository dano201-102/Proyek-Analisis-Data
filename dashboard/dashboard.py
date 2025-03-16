import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/day.csv")

# Konversi kolom tanggal
df['dteday'] = pd.to_datetime(df['dteday'])

# Mapping label musim
df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

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
ax.plot(filtered_df['dteday'], filtered_df['cnt'], marker='o', linestyle='-', color='red', label=f'Filtered Data ({selected_weather})')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.legend()
st.pyplot(fig)

# Visualisasi Faktor yang Mempengaruhi Sedikitnya Peminjaman
st.subheader("🔍 Faktor yang Mempengaruhi Peminjaman Rendah")
low_demand = df[df['cnt'] < df['cnt'].quantile(0.25)]
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=low_demand['season_label'], y=low_demand['cnt'], ax=ax)
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
season_options = ['All Seasons'] + list(df['season_label'].unique())
selected_season = st.selectbox('Pilih Musim:', season_options)

if selected_season != 'All Seasons':
    season_df = df[df['season_label'] == selected_season]
else:
    season_df = df

st.write("Menampilkan data untuk musim:", selected_season)

# Visualisasi dampak musim terhadap peminjaman sepeda
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_df['season_label'], y=season_df['cnt'], ci=None, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
st.pyplot(fig)

# 🔹 Tambahan: Korelasi Faktor dengan Peminjaman Sepeda
st.subheader("📊 Korelasi Faktor dengan Peminjaman Sepeda")
correlation_matrix = df[["cnt", "temp", "hum", "windspeed"]].corr()
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Correlation of Factors with Bike Rentals")
st.pyplot(fig)

# 🔹 Tambahan: Scatter Plot Faktor vs Peminjaman Sepeda
st.subheader("🔍 Analisis Faktor yang Mempengaruhi Peminjaman")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.scatterplot(x=df["temp"], y=df["cnt"], ax=axes[0])
axes[0].set_title("Temperature vs Bike Rentals")

sns.scatterplot(x=df["hum"], y=df["cnt"], ax=axes[1])
axes[1].set_title("Humidity vs Bike Rentals")

sns.scatterplot(x=df["windspeed"], y=df["cnt"], ax=axes[2])
axes[2].set_title("Windspeed vs Bike Rentals")

plt.tight_layout()
st.pyplot(fig)
