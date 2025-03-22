import streamlit as st
import pandas as pd

# Sayfa ayarları – geniş ekran
st.set_page_config(layout="wide")

# Başlık ve açıklama
st.markdown("## 📄 ARDEK Eylem ve Faaliyet Takip Tablosu")

# Excel dosyasını oku
df = pd.read_excel("Faaliyet_Matrisi.xlsx")  # Dosya aynı klasörde olmalı

# --- Tabloyu Göster ---
st.table(df.reset_index(drop=True))
