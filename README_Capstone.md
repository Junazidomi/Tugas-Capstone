# Proyek Capstone: ECOVISION Gerakan Pilah Sampah Cerdas Di Mulai Disini

## Cara Menjalankan Streamlit Secara Lokal
Untuk menjalankan aplikasi Streamlit secara lokal di komputer Anda, ikuti langkah-langkah berikut:

### Langkah 1: Instalasi Python
Pastikan Python sudah terpasang di komputer Anda. Anda bisa mengunduhnya dari : 
[Python](https://www.python.org/)

### Langkah 2: Instalasi Streamlit

Buka terminal atau command prompt, lalu jalankan perintah berikut untuk menginstal Streamlit:

```
    bash

    pip install streamlit
```

### Langkah 3: Menjalankan Aplikasi Streamlit

Setelah instalasi selesai, arahkan terminal ke folder tempat file aplikasi Streamlit Anda berada, lalu jalankan perintah:

```
    bash

    streamlit run nama_file.py

```

## Cara Membuat Conda dan Menjalankannya

Conda adalah manajer lingkungan yang memudahkan pengelolaan paket dan environment Python.

### Langkah 1: Instalasi Anaconda

Unduh dan instal Anaconda atau Miniconda dari situs resmi: 

[Anaconda](https://www.anaconda.com/download)

### Langkah 2: Membuat Environment Conda Baru

Buka terminal atau Anaconda Prompt, lalu buat environment baru dengan nama misalnya env_sampah:

```
    bash
    
    conda create -n env_sampah python=3.8

```

### Langkah 3: Mengaktifkan Environment

Aktifkan environment yang sudah dibuat dengan perintah:

```
    bash
    
    conda create -n conda activate env_sampah

```

### Langkah 4: Instalasi Dependensi

Setelah environment aktif, instal paket yang dibutuhkan, misalnya Streamlit dan library lain:

```
    bash

    pip install streamlit
    pip install numpy pandas scikit-learn

```

### Langkah 5: Menjalankan Aplikasi di Environment Conda

Pastikan environment aktif, lalu jalankan aplikasi Streamlit seperti biasa:

```
    bash

    streamlit run nama_file.py

```

## Tampilan Web App

Aplikasi web klasifikasi sampah ini memiliki antarmuka yang sederhana dan user-friendly dengan komponen utama sebagai berikut:

1. Tampilan Awal

   ![Tampilan Awal](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Tampilan%20Awal.png)

2. Memuat Gambar

   ![Memuat Gambar](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Memuat%20Gambar.png)

3. Penjelasan

   ![Penjelasan](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Penjelasan.png)
   
## Jenis Sampah yang Diklasifikasi

Web ini mengklasifikasikan sampah ke dalam 4 kategori utama berikut:

### Organik
- Sampah yang berasal dari bahan-bahan alami dan dapat terurai secara hayati, seperti sisa makanan, daun, dan ranting.

### Plastik
- Sampah berbahan plastik seperti botol, kantong plastik, dan kemasan makanan.

### Logam
- Sampah berbahan logam seperti kaleng minuman, tutup botol, dan potongan logam lainnya.

### Karton/Kardus
- Sampah berbahan kertas tebal seperti kotak kemasan, kardus, dan karton.

Setiap kategori memiliki karakteristik khusus yang membantu model dalam mengenali dan mengklasifikasikan sampah dengan akurat.