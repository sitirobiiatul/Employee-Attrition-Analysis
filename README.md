# Menyelesaikan Permasalahan Human Resources

## Business Understanding

Perusahaan saat ini tengah menghadapi tantangan serius dalam menjaga stabilitas tenaga kerjanya. Tingginya angka karyawan yang mengundurkan diri tidak hanya berdampak pada produktivitas operasional, namun juga berpotensi menghambat pertumbuhan perusahaan secara keseluruhan. Permasalahan ini perlu segera ditangani untuk mencegah dampak negatif yang lebih besar pada produktivitas dan biaya operasional perusahaan. Untuk itu, memahami penyebab utama dari keputusan karyawan untuk meninggalkan perusahaan menjadi langkah strategis dalam menyusun kebijakan retensi yang lebih efektif di masa depan.

### Business Problem

- **Kurangnya Pemahaman atas Faktor Penyebab**
    
    Belum adanya kejelasan tentang variabel atau kondisi kerja seperti lingkungan, kepuasan, hingga beban kerja yang paling berpengaruh terhadap keputusan karyawan untuk keluar.
    
- **Keterbatasan Alat Pemantauan**
    
    Departemen HR belum memiliki media visualisasi yang komprehensif untuk memantau tren attrition secara dinamis, sehingga sulit mengambil keputusan berbasis data secara cepat.
    
- **Minimnya Strategi Pencegahan yang Terukur**
    
    Tidak ada rekomendasi berbasis data yang dapat dijadikan landasan untuk membuat kebijakan retensi yang efektif dan terukur.

### Project Scope

- **Eksplorasi Data Karyawan**

    Melakukan analisis deskriptif terhadap data demografi, jabatan, gaji karyawan dll untuk mengenali pola-pola yang berkaitan dengan keputusan untuk berhenti bekerja.

- **Identifikasi Pola dan Faktor Risiko**
    
    Menganalisis hubungan antar variabel untuk menemukan faktor-faktor kunci yang berkorelasi tinggi dengan keputusan karyawan untuk keluar dari perusahaan.

- **Pembuatan Dashboard Interaktif**
    
    Mendesain dan membangun dashboard bisnis interaktif untuk menyajikan insight terkait faktor-faktor utama penyebab attrition, yang dapat digunakan oleh tim HR dalam pengambilan keputusan.
    
- **Pembuatan Model Prediktif**
    
    Membangun model machine learning sederhana yang dapat memperkirakan kemungkinan seorang karyawan melakukan attrition berdasarkan variabel-variabel yang tersedia.

### Preparation

**Data source:** [Employee data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee 'Dicoding GitHub - Employee data')

**Setup environment:**

1. Clone this Repository
   ```bash
   git clone https://github.com/sitirobiiatul/Employee-Attrition-Analysis.git
   ```

2. Create Python Virtual Environment
   ```bash
   virtualenv venv
   ```

2. Activate the Environment
   ```bash
   venv\Scripts\activate
   ```

4. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

**To run the Streamlit prediction:**
```bash
streamlit run streamlit_app.py
```

**Streamlit Link**

Link cloud streamlit dapat diaksaes melalui: https://employee-attrition-analysis-sitirobiiatul.streamlit.app/
    
