import streamlit as st
import numpy as np
import os 
from PIL import Image
import tensorflow as tf

st.markdown("""
    <style>
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        background-color:#CFE3D4;
    }

    .custom-col {
        color: #000000;
        background-image:linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
             url( Gambar/green-technology.png);
        background-size: cover;
        background-position: center;
        padding: 20px;
        color:white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title('Klasifikasi Sampah')
    st.image('Gambar/Logo.png', width=250)
    st.markdown("""
<a href="https://www.kaggle.com/datasets/juanzi/basetrash2" target="_blank" style="color: black; text-decoration: none;">
    Source
</a>
""", unsafe_allow_html=True)

st.markdown('''
    <div class="custom-col" style="display: flex; flex-direction: row; gap: 20px; align-items: center;">
        <div style="flex: 1; text-align: center;">
            <img src="https://raw.githubusercontent.com/Junazidomi/Tugas-Capstone/refs/heads/main/Tugas_Capstone/Gambar/Recycle.png" width="200">
        </div>
        <div style="flex: 2; text-align: left;">
            <p>Web klasifikasi sampah ini dibuat untuk membantu pengguna mengenali dan mengelompokkan 4 jenis sampah.
            Dengan memanfaatkan deep learning CNN dalam pengenalan gambar, diharapkan dapat membantu pengguna dalam mengenali kategori sampah dan cara pengelolaan sampah.</p>
        </div>
    </div>
''', unsafe_allow_html=True)


def load_tflite_model():
    interpreter = tf.lite.Interpreter(model_path="Notebook/model_quant.tflite")
    interpreter.allocate_tensors()
    return interpreter

@st.cache_resource
def load_labels():
    with open("Notebook/label.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

interpreter = load_tflite_model()
class_names = load_labels()


st.markdown("""
    <div style='text-align: center;'>
        <h1>Waste Classification</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown('''
    <div style="
        display: grid; 
        grid-template-columns: repeat(2, 1fr); 
        gap: 30px; 
        justify-items: center; 
        margin-bottom: 30px;
    ">
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/Junazidomi/Tugas-Capstone/refs/heads/main/Tugas_Capstone/Gambar/Botol%20Plastik.png" width="200">
            <p>Botol Plastik</p>
        </div>
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/Junazidomi/Tugas-Capstone/refs/heads/main/Tugas_Capstone/Gambar/Kardus.png" width="200">
            <p>Karton</p>
        </div>
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/Junazidomi/Tugas-Capstone/refs/heads/main/Tugas_Capstone/Gambar/Metal.png" width="200">
            <p>Metal</p>
        </div>
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/Junazidomi/Tugas-Capstone/refs/heads/main/Tugas_/Gambar/Organik.png" width="200">
            <p>Organik</p>
        </div>
    </div>
''', unsafe_allow_html=True)


st.markdown("""
    <div style='text-align: center;'>
        <h1>Deteksi Sekarang</h1>
    </div>
""", unsafe_allow_html=True)
st.write("Unggah gambar untuk diprediksi oleh model CNN.")

uploaded_file = st.file_uploader("Pilih file gambar...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image_resized = image.resize((150, 150))
    img_array = np.array(image_resized, dtype=np.float32) / 255.0
    input_data = np.expand_dims(img_array, axis=0)

    # TFLite prediction
    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']
    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_index)
    predicted_class = np.argmax(prediction)

    label = class_names[predicted_class]
    if class_names[predicted_class]=='Metal':
        Kate='Anorganik'
        st.markdown("<h2 style='text-align: center;'>Sampah Metal</h2>", unsafe_allow_html=True)
        st.write('Sampah Metal adalah sampah yag terbuat dari alumunium besi yang umumnya kaleng minuman.' \
        'Sampah metal tidak dapat terurai sehingga dikategorikan anorganik sehingga butuh proses daur ulang atau mengubah menjadi produk kerajinan' \
        'Berikut adalah tahapan dalam proses pengelolaan sampah metal:')
        st.write('1. Pisahkan dari sampah lainnya')
        st.write('2. Bersihkan sisa makanan/minuman dari kaleng/logam')
        st.write('3. Jangan membakar sampah logam karena berbahaya dan tidak efisien')
        st.write('4. Kumpulkan dan jual ke pengepul atau tempat daur ulang sampah logam')
        st.write('Solusi alternatif: Dapat diubah menjadi kerajinan logam seperti vas bunga, asbak dan lain-lain')
    elif class_names[predicted_class] == 'Karton':
        Kate='Organik'
        st.markdown("<h2 style='text-align: center;'>Sampah Karton atau Kardus </h2>", unsafe_allow_html=True)
        st.write('Sampah karton atau kardus adalah sampah yang terbuat dari kertas, umumnya berbentuk kotak dan sering digunakan untuk membungkus barang-barang atau digunakan pada pengiriman barang atau' \
        'ekspedisi. Sampah ini termasuk kategori organik atau dapat terurai karena kertas terbuat dari kayu. Berikut ini adalah tahapan dalam proses pengelolaan sampah karton/kardus')
        st.write('1. Pisahkan dari sampah basah atau organik.')
        st.write('2. Lipat dan susun rapi agar mudah disimpan dan diangkut.')
        st.write('3. Jangan biarkan terkena air karena akan menurunkan nilai daur ulang.')
        st.write('4. Serahkan ke tempat pengumpulan kertas atau tukang loak.')
        st.write('Solusi alternatif: Sampah karton/kardus dapat diolah menjadi perabotan rumah tangga seperti, tempat tisu, tempat alat tulis dan lain-lain')
    elif class_names[predicted_class] =='Organik':
        Kate='Organik'
        st.markdown("<h2 style='text-align: center;'>Sampah Organik</h2>", unsafe_allow_html=True)
        st.write('Sampah organik adalah sampah yang terbuat dari sisa makanan, sisa dapur dan kebun dan sisa hewan. Sampah ini dapat mencemari lingkungan seperti dapat mencemari udara karena bau busuk dan gas yang dihasilkan,' 
        'dan jika ditempatkan di air seperti sungai maka akan menyebabkan lingkungan air menjadi kotor dan tercemar. Berikut adalah tahapan dalam proses pengelolaan sampah organik:')
        st.write('1. Kumpulkan sisa makanan, sayur, kulit buah, dan dedaunan.')
        st.write('2. Jangan mencampur dengan plastik atau logam.')
        st.write('3. Gunakan sebagai bahan kompos menggunakan metode komposter rumah tangga')
        st.write('4. Bisa juga menggunakan teknik vermikompos (dengan cacing tanah)')
        st.write('Solusi alternatif: Sampah organik dapat dijadikan menjadi pupuk alami bagi tumbuhan supaya dapat bertumbuh cepat  ')
    elif class_names[predicted_class]=='Botol_Plastik':
        Kate='Anorganik'
        st.markdown("<h2 style='text-align: center;'>Sampah Botol Plastik</h2>", unsafe_allow_html=True)
        st.write('Sampah botol plastik adalah sampah yang terbuat dari plastik yang biasaya ditemukan pada kemasan minuman mineral.' 
        'Sampah ini termasuk sampah anorganik atau sampah yang tidak bisa terurai. Sampah ini jika terkena sinar matahari,'
        'maka akan mengeluarkan gas metana yang dapat menyebabkan pemanasan global. Selain itu, sampah botol plastik dapat mencemari lingkungan jika ' \
        'tidak benar dalam pengelolaan sampah.Berikut adalah tahapan dalam proses pengelolaan sampah Botol plastik:' )
        st.write('1. Pisahkan dari jenis sampah lainnya')
        st.write('2. Bersihkan botol dari sisa cairan agar tidak menarik serangga')
        st.write('3. Pipihkan botol agar menghemat ruang saat disimpan atau dibuang')
        st.write('4. Kirim ke tempat daur ulang plastik atau bank sampah terdekat')
        st.write('Solusi alternatif: Sampah botol plastik dapat diubah menjadi kerajinan dan perabot rumah tangga seperti pot anaman, tempat alat tulis dan lain-lain.')
    
    with st.sidebar:
        st.markdown("""
            <div style="
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 15px;
                background-color: #e6ffe6;
                text-align: left;
                margin-top: 20px;
            ">
                <h4>Hasil Prediksi</h4>
                <p><strong>Nama File:</strong><br> {filename}</p>
                <p><strong>Jenis:</strong><br> {jenis}</p>
                 <p><strong>Kategori Sampah:</strong><br> {kategori}</p>
            </div>
        """.format(
            filename=uploaded_file.name,
            kategori=class_names[predicted_class].replace("_", " "),
            jenis=Kate
        ), unsafe_allow_html=True)

