# Proyek Capstone: ECOVISION Gerakan Pilah Sampah Cerdas Di Mulai Disini

## Latar Belakang Masalah 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sampah di Indonesia masih merupakan masalah lingkungan yang mendesak dan kompleks. Volume sampah yang dihasilkan terus meningkat setiap hari karena populasi yang meningkat dan laju urbanisasi. Sayangnya, pengelolaan sampah masih menggunakan sistem kumpul-angkut-buang tradisional tanpa proses pemilahan yang memadai di tingkat sumber, seperti rumah tangga dan lingkungan sekitar. Hal ini menyebabkan tumpukan sampah bercampur di Tempat Pembuangan Akhir (TPA), yang mempercepat kapasitas TPA, dan menyebabkan pencemaran tanah, air, dan udara serta risiko kesehatan bagi komunitas sekitar.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Namun, pemilahan sampah dari sumbernya sangat penting untuk pengelolaan sampah yang berkelanjutan. Sampah anorganik seperti kaca, plastik, dan logam sangat berharga karena dapat didaur ulang. Sampah organik seperti sisa makanan dan daun kering dapat diolah menjadi kompos atau bahan baku energi. Namun, kesadaran dan pengetahuan masyarakat tentang pemilahan mandiri masih rendah. Selain itu, kendala utama dalam menerapkan pemilahan sampah baik di tingkat individu maupun komunitas adalah keterbatasan waktu dan sumber daya.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ketika teknologi berkembang, khususnya di bidang kecerdasan buatan (AI), ada peluang untuk membuat solusi inovatif yang dapat mengatasi masalah ini. Kami dapat membangun sistem klasifikasi citra yang menggunakan teknologi Convolutional Neural Network (CNN) untuk mengidentifikasi jenis sampah berdasarkan gambar. Diharapkan sistem ini akan membantu masyarakat memilah sampah organik dan anorganik secara praktis, cepat, dan akurat. Sebagai bagian dari upaya untuk mendukung gerakan pilah sampah cerdas dan membangun ekosistem pengelolaan sampah yang lebih ramah lingkungan dan berkelanjutan, proyek ini bertujuan untuk mengembangkan model CNN tersebut.

## Cakupan Proyek

Cakupan proyek yang dilakukan yaitu:
1. Gathering dan Prepocessing Image
   - Melakukan eksplorasi terhadap dataset yang relavan dengan 4 kelas yaitu Metal, Botol Plastik, Karton/kardus dan Organik
   - Mengumpulkan dataset kemudan menyatukannya dalam 1 folder
3. Melakukan training dan modeling:
   - Melakukan training dan hypertune parameter supaya mendapatkan akurasi yang baik
   - Melakukan eksport model sesuai dengan kebutuhan deployment
   
3. Membangun sistem berupa Web App Streamlit
   - Merancang dan mengimplementasikan sistem klasifikasi sampah berbasis Web App menggunakan Streamlit

## Jenis Sampah yang Diklasifikasi

Web ini mengklasifikasikan sampah ke dalam 4 kategori utama berikut:

### Organik
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sampah organik adalah sampah yang berasal dari bahan-bahan alami yang dapat terurai secara alami melalui proses biologi, seperti sisa makanan, daun, dan ranting. Sampah jenis ini dapat diolah menjadi kompos atau pupuk yang bermanfaat untuk tanaman.

### Plastik
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sampah plastik terdiri dari material sintetis yang sulit terurai di alam, seperti botol plastik, kantong plastik, dan kemasan makanan. Jenis sampah ini sebaiknya didaur ulang agar tidak mencemari lingkungan dalam jangka panjang.

### Logam

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sampah logam meliputi bahan-bahan seperti kaleng minuman, tutup botol, dan potongan logam lainnya yang dapat didaur ulang dan memiliki nilai ekonomi. Sampah logam membutuhkan waktu sangat lama untuk terurai jika tidak dikelola dengan baik.

### Karton/Kardus
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sampah logam meliputi bahan-bahan seperti kaleng minuman, tutup botol, dan potongan logam lainnya yang dapat didaur ulang dan memiliki nilai ekonomi. Sampah logam membutuhkan waktu sangat lama untuk terurai jika tidak dikelola dengan baik.

Setiap kategori memiliki karakteristik khusus yang membantu model dalam mengenali dan mengklasifikasikan sampah dengan akurat.
## Persiapan

### Cara Menjalankan Streamlit Secara Lokal
Untuk menjalankan aplikasi Streamlit secara lokal di komputer Anda, ikuti langkah-langkah berikut:

Langkah 1: Instalasi Python
Pastikan Python sudah terpasang di komputer Anda. Anda bisa mengunduhnya dari : 
[Python](https://www.python.org/)

Langkah 2: Instalasi Streamlit

Buka terminal atau command prompt, lalu jalankan perintah berikut untuk menginstal Streamlit:

```
    bash

    pip install streamlit
```

Langkah 3: Menjalankan Aplikasi Streamlit

Setelah instalasi selesai, arahkan terminal ke folder tempat file aplikasi Streamlit Anda berada, lalu jalankan perintah:

```
    bash

    streamlit run nama_file.py

```

## Cara Menjalankan proyek melalui Env

Conda adalah manajer lingkungan yang memudahkan pengelolaan paket dan environment Python.

 Membuat dan Mengaktifkan Virtual Envirotment
   ```bash
      python   -m venv venv
   ```
- Aktifkan Envirotment
  - Windows
    ```bash
    venv\Scripts\activate
    ```
  - MacOS/Linux
    ```bash
    source  venv/bin/activate
    ```
- Install Dependecies
    ```bash
    pip install -r requirements.txt
    ```

## Tampilan Web App

Aplikasi web klasifikasi sampah ini memiliki antarmuka yang sederhana dan user-friendly dengan komponen utama sebagai berikut:

1. Tampilan Awal

   ![Tampilan Awal](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Tampilan%20Awal.png)

2. Memuat Gambar

   ![Memuat Gambar](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Memuat%20Gambar.png)

3. Penjelasan

   ![Penjelasan](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Penjelasan.png)
   

