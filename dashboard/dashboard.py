import streamlit as st
import pandas as pd
import requests
import os

############################################################################################

dataset_dict = {}
dataset_folder = './data'
numerical_col = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
for idx, csv_file in enumerate(os.listdir(dataset_folder)):
    dataset_dict[idx] = pd.read_csv(os.path.join(dataset_folder, csv_file))

station_dict = {
    dataset_dict[0]['station'][0]: 0,
    dataset_dict[1]['station'][0]: 1,
    dataset_dict[2]['station'][0]: 2,
    dataset_dict[3]['station'][0]: 3,
    dataset_dict[4]['station'][0]: 4,
    dataset_dict[5]['station'][0]: 5,
    dataset_dict[6]['station'][0]: 6,
    dataset_dict[7]['station'][0]: 7,
    dataset_dict[8]['station'][0]: 8,
    dataset_dict[9]['station'][0]: 9,
    dataset_dict[10]['station'][0]: 10,
    dataset_dict[11]['station'][0]: 11,
}

###############################################################################################

# Title for the dashboard
st.title("Analisis Data Kualitas Udara di Stasiun Cina (2013-2017)")
st.subheader("Kevin Putra Santoso, 2024")

# Introduction to the dashboard
st.markdown("""
Dasbor ini menyajikan analisis gas beracun seperti CO (Karbon Monoksida), SO2 (Sulfur Dioksida), NO2 (Nitrogen Dioksida), dan lain-lain di 12 stasiun di Cina. 
""")

with st.expander("Daftar Stasiun (Klik untuk lihat)"):
    st.markdown("""
1. [Aotizhongxin](https://en.wikipedia.org/wiki/Aotizhongxin_station)
2. [Changping](https://en.wikipedia.org/wiki/Changping_railway_station_(Beijing))
3. Dingling
4. [Dongsi](https://en.wikipedia.org/wiki/Dongsi_station)
5. [Guanyuan](https://en.wikipedia.org/wiki/Guangyuan_railway_station)
6. [Gucheng](https://en.wikipedia.org/wiki/Gucheng_station)
7. [Huairou](https://en.wikipedia.org/wiki/Huairou_South_railway_station)
8. Nongzhanguan
9. [Shunyi](https://en.wikipedia.org/wiki/Shunyi_station)
10. [Tiantan](https://en.wikipedia.org/wiki/Temple_of_Heaven_East_Gate_station)
11. [Wanliu](https://www.travelchinaguide.com/cityguides/beijing/transportation/subway-line10.htm)
12. Wanshouxigong
""")
    
st.markdown("""
Konsentrasi gas-gas ini menunjukkan pola yang berfluktuasi, dengan beberapa tren dan korelasi yang patut diperhatikan.
Selain itu, analisis curah hujan juga disajikan untuk menunjukkan tren bulanan dan tahunan. Analisis multivariat dan korelasi juga dilakukan untuk menunjukkan hubungan antara konsentrasi gas dan variabel lainnya.
""")

st.header("Data Overview")

ds = st.radio(
    label="Silakan pilih stasiun",
    options=(station_dict.keys()),
    horizontal=True
)

st.dataframe(
    data=dataset_dict[station_dict[ds]].head()
)
st.caption(f"Sampel Data dari Stasiun {ds}")

st.markdown("""
Dataset ini adalah dataset yang bertipe time series, yang mana karakteristik dari fitur akan bergantung terhadap waktu. Adapun informasi yang dimuat dalam dataset ini adalah
kandungan polutan dalam udara serta beberapa variabel lain seperti curah hujan dan kecepatan angin ditinjau mulai dari tahun 2013 hingga 2017. Dataset ini memiliki 13 total fitur dimana 9 diantaranya adalah fitur numerik dan 4 fitur lainnya adalah fitur kategorikal.
Ditinjau dari impact yang mungkin diberikan, informasi dalam dataset ini berpotensi memberikan insight yang dapat membantu dalam pengambilan keputusan terkait dengan kualitas udara dan lingkungan hidup di Cina.
Beberapa pertanyaan riset diusulkan dalam proses analisis dataset ini, diantaranya adalah:
1. Bagaimana perubahan kandungan senyawa kimia berbahaya di udara dari waktu ke waktu untuk setiap stasiun?
2. Bagaimana variabel-variabel seperti waktu, PM2.5, PM10, ..., O3 berpengaruh satu sama lain?
3. Bagaimana karakteristik persebaran senyawa kimia seperti SO2, NO2, dan CO jika dibandingkan antar stasiun?

Untuk menjawab pertanyaan ini, terdapat beberapa pendekatan yang mungkin dilakukan, antara lain:
- Analisis tren kandungan senyawa kimia dari waktu ke waktu
- Analisis curah hujan serta trennya
- Persebaran data angka senyawa tertinggi pada selang waktu tertentu
- Analisis Multivariat Korelasi

Dalam proses eksplorasi data, ditemukan beberapa kolom yang memiliki missing value. Nilai missing value diisi menggunakan teknik interpolasi lagrange yang didefinisikan sebagai berikut.
""")

# Lagrange Interpolation Formula
st.latex(r'''
L(x) = \sum_{i=0}^{n} y_i \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}
''')

st.markdown("""
Interpolasi Lagrange adalah metode yang baik untuk mengisi missing values dalam data time series karena metode ini 
mempertimbangkan hubungan antara titik data yang ada sebelum dan setelah missing values. Dalam data time series, titik data 
yang berdekatan cenderung memiliki hubungan yang erat dan pola yang serupa. Dengan menggunakan interpolasi Lagrange, kita dapat 
memperkirakan nilai yang hilang berdasarkan pola dan tren dari titik data sekitarnya. Ini memungkinkan kita untuk 
mengisi missing values dengan perkiraan yang lebih akurat daripada metode pengisian sederhana seperti mean atau median.
""")

st.header("Statistik Deskriptif")
st.markdown("""
Proses ini dilakukan untuk mengekstrak informasi dasar (statistik deskriptif) dari dataset. 
Informasi ini dapat memberikan gambaran umum tentang karakteristik data, seperti rata-rata, standar deviasi, nilai minimum, nilai maksimum, dan lain-lain.
Untuk fitur numerik, statistik deskriptif yang dihasilkan adalah sebagai berikut.
""")
st.write(
    dataset_dict[0][numerical_col].describe()
)

with st.expander("Klik untuk lihat penjelasan!"):
    st.markdown("""
    - **PM2.5**: Partikel dengan ukuran 2.5 mikrometer atau lebih kecil. Rata-rata konsentrasi partikel ini adalah 82.7736 μg/m³, dengan standar deviasi 82.1357, menunjukkan variasi yang cukup besar dalam ukuran sampel.
    - **PM10**: Partikel dengan ukuran 10 mikrometer atau lebih kecil. Rata-rata konsentrasi partikel ini adalah 110.0604 μg/m³.
    - **SO2**: Sulfur Dioksida, gas yang umumnya dihasilkan dari proses pembakaran fosil. Rata-rata konsentrasi adalah 17.3759 μg/m³.
    - **NO2**: Nitrogen Dioksida, gas yang sering dihasilkan dari emisi kendaraan dan pembangkit listrik. Rata-rata konsentrasi adalah 59.3058 μg/m³.
    - **CO**: Karbonmonoksida, gas yang tidak berwarna dan berbau yang berbahaya dalam konsentrasi tinggi. Rata-rata konsentrasi sangat tinggi yaitu 1,262.9451 μg/m³.
    - **O3**: Ozon, gas yang di lapisan atmosfer membantu melindungi makhluk hidup dari sinar UV namun di permukaan bumi merupakan polutan. Rata-rata konsentrasi adalah 56.3534 μg/m³.
    - **TEMP**: Suhu udara rata-rata tercatat 13.5846°C.
    - **PRES**: Tekanan atmosfer rata-rata tercatat 1,011.8469 hPa.
    - **DEWP**: Titik embun, rata-rata tercatat 3.1231°C. Ini mengindikasikan suhu di mana uap air mulai mengembun menjadi air.
    - **RAIN**: Curah hujan, rata-rata tercatat sangat rendah pada 0.0674 mm.
    
    Nilai maksimum untuk CO sangat tinggi dibandingkan dengan rata-ratanya, yang bisa mengindikasikan adanya outlier atau kejadian ekstrem tertentu yang meningkatkan rata-rata.
    """)
st.subheader("Summary Report")
st.markdown("""
    Bagian ini menjelaskan ringkasan analisis keseluruhan untuk dataset yang dipilih. Suit yourself!
""")
url = f'https://raw.githubusercontent.com/echelon2718/Air-Quality-Analysis-Properties/main/properties/{ds}.html'
response = requests.get(url)
if response.status_code == 200:
    html_data = response.text
    # with open(f"https://github.com/echelon2718/Air-Quality-Analysis-Properties/tree/792dba8f768dd89c62739bec8a413a028e3d30ba/properties/{ds}.html", 'r') as f:
    #     html_data = f.read()
    st.components.v1.html(html_data, height=500, scrolling=True)    

else:
    st.write("ERROR: Failed to load the summary report")

st.header("Analisis Tren Stasiun Aotingzhongxin VS Dingling")
st.markdown("""
    Semenjak dataset ini merupakan dataset time series, kita bisa melakukan analisis tren terhadap bagaimana karakteristik data antar stasiun terhadap waktu. 
    Data ini meliputi kandungan gas polutan di udara, curah hujan, kecepatan angin, dan suhu udara. Sebagai contoh, kita akan menganalisis tren kandungan gas CO (karbonmonoksida) dan NO2 (nitrogen dioksida) di stasiun Aotizhongxin dan Dingling.
""")

st.subheader(f"Tren Intensitas Gas Karbonmonoksida (CO)")
col1, col2 = st.columns(2)
with col1:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20Karbonmonoksida%20Per%20Bulan.png?raw=true", caption="Analisis Tren Gas CO Per Bulan")
with col2:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20Karbonmonoksida%20Per%20Tahun.png?raw=true", caption="Analisis Tren Gas CO Per Tahun")

st.subheader("Tren Intensitas Gas Nitrogen Dioksida (NO2)")
col1, col2 = st.columns(2)
with col1:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20NO2%20Per%20Bulan.png?raw=true", caption="Analisis Tren Gas NO2 Per Bulan")
with col2:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20NO2%20Per%20Tahun.png?raw=true", caption="Analisis Tren Gas NO2 Per Tahun")

st.header("Tren Curah Hujan")
col1, col2 = st.columns(2)
with col1:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20Curah%20Hujan%20Per%20Bulan.png?raw=true", caption="Analisis Tren Curah Hujan Per Bulan")
with col2:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Tren%20Curah%20Hujan%20Per%20Tahun.png?raw=true", caption="Analisis Tren Curah Hujan Per Tahun")


with st.expander("Klik untuk lihat penjelasan!"):
    st.markdown("""
    Analisis terhadap kandungan gas beracun seperti CO (karbonmonoksida), SO2 (sulfur dioksida), dan NO2 (nitrogen dioksida) di beberapa stasiun pengamatan di Cina mengungkapkan pola fluktuatif dalam konsentrasi CO sepanjang bulan. Penelitian ini menunjukkan penurunan konsentrasi CO selama periode Mei hingga November 2014, Mei hingga September 2015, dan Mei hingga September 2016 di setiap stasiun. Menariknya, terdapat peningkatan drastis pada konsentrasi CO di awal tahun yang kemungkinan dipicu oleh perayaan tahun baru dan peningkatan lalu lintas kendaraan kembali ke kota. Secara khusus, stasiun Aotizhongxin mencatat konsentrasi polutan tertinggi, sedangkan stasiun Dingling memiliki konsentrasi terendah.         
    Di sisi lain, kita juga dapat melihat bahwa tren curah hujan menunjukkan kenaikan dari waktu ke waktu.
    """)

# Display images for multivariate analysis and correlation
st.header("Analisis Multivariat dan Korelasi")
col1, col2 = st.columns(2)
with col1:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Analisis%20Multivariat%20Gas%20SO2%20dan%20CO%20Stasiun%20Aotizhongxin.png?raw=true", caption="Analisis Multivariat Distributif Gas SO2 dan CO di Stasiun Aotizhongxin")
with col2:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Analisis%20Multivariat%20Gas%20SO2%20dan%20CO%20Stasiun%20Dingling.png?raw=true", caption="Analisis Multivariat Distributif Gas SO2 dan CO di Stasiun Dingling")

col1, col2 = st.columns(2)
with col1: 
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Persebaran%20Konsentrasi%20Gas%20CO%20di%20Stasiun%20Aotizhongxin%205%20tahun.png?raw=true", caption="Distribusi Konsentrasi Gas CO di Stasiun Aotizhongxin dari 2013-2017")
with col2:
    st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Persebaran%20Konsentrasi%20Gas%20CO%20di%20Stasiun%20Dingling%205%20tahun.png?raw=true", caption="Distribusi Konsentrasi Gas CO di Stasiun Dingling dari 2013-2017")

st.image("https://github.com/echelon2718/Air-Quality-Analysis-Properties/blob/main/images/Korelasi%20Rata-rata%20Fitur%20Numerik%20Antar%20Stasiun.png?raw=true")

with st.expander("Klik untuk lihat penjelasan!"):
    st.markdown("""
    Analisis korelasi multivariat mengungkapkan hubungan yang kuat antara variabel konsentrasi gas CO, NO2, SO2, PM10 (partikulat ukuran 10 mikrometer atau lebih kecil), dan PM2.5 (partikulat ukuran 2.5 mikrometer atau lebih kecil). Hubungan ini mencerminkan dampak signifikan dari mobilitas kereta yang meningkat terhadap polusi udara. Ditemukan juga bahwa polutan tersebut secara negatif mempengaruhi ozon (O3) dengan NO2 sebagai kontributor utama dalam merusak lapisan ozon. Selanjutnya, analisis menunjukkan bahwa partikel PM2.5 dan PM10 memiliki korelasi negatif terhadap kecepatan angin (WSPM), menunjukkan bahwa peningkatan kandungan partikulat dalam udara dapat mengurangi kecepatan angin.
    """)

st.markdown("""
## Ringkasan Hasil Analisis
            
- Terdapat pola fluktuasi konsentrasi CO setiap bulan, dengan penurunan yang dicatat dari Mei hingga November pada tahun 2014, 2015, dan 2016 di setiap stasiun.
- Peningkatan signifikan konsentrasi CO diamati di awal tahun, yang kemungkinan disebabkan oleh perayaan Tahun Baru dan peningkatan lalu lintas kendaraan.
- Stasiun Aotizhongxin mencatat konsentrasi polutan tertinggi, sementara stasiun Dingling memiliki konsentrasi terendah.
- Tren curah hujan tahunan menunjukkan peningkatan, dengan puncak tertinggi tercatat pada Agustus 2016.
- Stasiun Aotizhongxin menunjukkan variabilitas yang signifikan dalam standar deviasi intensitas gas CO dan NO2, menandakan tingkat aktivitas yang lebih tinggi di stasiun tersebut.
- Ditemukan korelasi kuat antara konsentrasi CO, NO2, SO2, PM10, dan PM2.5, yang mencerminkan dampak peningkatan mobilitas kereta terhadap polusi udara.
- Polutan memiliki efek negatif terhadap ozon (O3), dengan NO2 sebagai kontributor utama dalam kerusakan lapisan ozon.
- Partikel PM2.5 dan PM10 memiliki korelasi negatif dengan kecepatan angin, menunjukkan bahwa peningkatan kandungan partikulat dapat mengurangi kecepatan angin.
""")

st.caption('Author: Kevin Putra Santoso, 2024')