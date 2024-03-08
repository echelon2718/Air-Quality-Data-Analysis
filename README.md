# Analisis Data Kualitas Udara di Stasiun Cina (2013-2017)
### Author: Kevin Putra Santoso, 2024

Proyek ini menyajikan analisis gas beracun seperti CO (Karbon Monoksida), SO2 (Sulfur Dioksida), NO2 (Nitrogen Dioksida), dan lain-lain di 12 stasiun di Cina. Konsentrasi gas-gas ini menunjukkan pola yang berfluktuasi, dengan beberapa tren dan korelasi yang patut diperhatikan. Selain itu, analisis curah hujan juga disajikan untuk menunjukkan tren bulanan dan tahunan. Analisis multivariat dan korelasi juga dilakukan untuk menunjukkan hubungan antara konsentrasi gas dan variabel lainnya.

## Setup Environment:
```
conda create --name proyek_ds python=3.10.2
conda activate proyek_ds
pip install -r requirements.txt
```
## Run streamlit app
```
streamlit run ./dashboard/dashboard.py
```