# 🎤 SKRIP PRESENTASI - STAGE 0: Basic Streamlit Setup

## 📋 PERSIAPAN SEBELUM MULAI
---

**[Sebelum mulai coding]**

"Selamat datang di sesi live coding hari ini! Kita akan membangun aplikasi AI Content Generator dari nol sampai jadi aplikasi yang kompleks. 

Hari ini kita akan melihat bagaimana membangun aplikasi AI step by step, dari yang paling sederhana sampai yang canggih menggunakan Google Gemini AI.

Mari kita mulai dengan tahap paling dasar - Stage 0!"

---

## 🎬 STAGE 0 - SKRIP LIVE CODING
---

### **1. PEMBUKAAN (30 detik)**

"Baik teman-teman, sekarang kita masuk ke **Stage 0 - Basic Streamlit Setup**. 

Di stage ini, tujuan kita sangat sederhana:
- ✅ Membuat aplikasi Streamlit paling basic
- ✅ Menampilkan judul dan teks sambutan
- ✅ Memastikan environment Streamlit berjalan dengan baik

Ini adalah fondasi dari semua yang akan kita bangun hari ini!"

---

### **2. MULAI CODING (2-3 menit)**

**[Buka editor, buat file stage0.py]**

"Pertama-tama, saya akan membuat file baru bernama `stage0.py`. Kenapa dimulai dari 0? Karena dalam programming, kita selalu mulai dari 0! 😄"

**[Tulis import statement]**
```python
import streamlit as st
```

"Yang pertama kita lakukan adalah import Streamlit. Streamlit ini adalah framework Python yang memungkinkan kita membuat web app hanya dengan beberapa baris kode. Sangat powerful!"

---

**[Tulis fungsi run()]**
```python
def run():
```

"Saya membuat fungsi `run()` - ini adalah pattern yang akan kita gunakan di semua stage. Kenapa? Supaya nanti kita bisa import dan panggil fungsi ini dari file lain dengan mudah."

**[Tambahkan docstring]**
```python
    """
    Stage 0: Basic Streamlit Setup
    Menampilkan halaman Streamlit paling sederhana dengan judul dan teks
    """
```

"Saya selalu menambahkan docstring untuk menjelaskan apa yang dilakukan fungsi ini. Good practice dalam programming!"

---

**[Tambahkan st.title()]**
```python
    # Judul aplikasi
    st.title("AI Content Generator 🚀")
```

"Sekarang magic-nya mulai! Dengan `st.title()`, kita langsung bisa membuat judul besar di web app kita. Lihat betapa mudahnya Streamlit!"

**[Tambahkan st.write()]**
```python
    # Teks pembuka sederhana
    st.write("Selamat datang di aplikasi AI Content Generator!")
    st.write("Aplikasi ini akan membantu Anda membuat konten dengan bantuan AI.")
```

"Dan dengan `st.write()`, kita bisa menampilkan teks apapun. Streamlit akan otomatis format semuanya jadi cantik!"

---

**[Tambahkan if __name__ == "__main__":]**
```python
if __name__ == "__main__":
    run()
```

"Bagian ini memastikan kalau file ini dijalankan langsung, fungsi `run()` akan dipanggil. Tapi kalau di-import dari file lain, tidak akan auto-run."

---

### **3. TESTING & DEMO (1-2 menit)**

**[Save file dan run di terminal]**

"Sekarang mari kita test! Saya akan jalankan:"

```bash
streamlit run stage0.py
```

**[Tunggu app terbuka di browser]**

"Dan voila! Lihat apa yang terjadi! Dalam hitungan detik, kita sudah punya web application yang berjalan di browser! 

Ini yang keren dari Streamlit - dari code Python biasa, langsung jadi web app yang cantik!"

**[Tunjukkan di browser]**

"Perhatikan:
- ✅ Judul sudah muncul dengan ukuran besar
- ✅ Emoji rocket muncul dengan sempurna  
- ✅ Teks sambutan tampil rapi
- ✅ Ada menu sidebar otomatis dari Streamlit
- ✅ Bahkan ada tombol rerun kalau kita ubah code!"

---

### **4. PENUTUPAN STAGE 0 (1 menit)**

"Jadi teman-teman, dengan hanya **10 baris kode**, kita sudah berhasil membuat:
- 🌐 Web application yang berjalan di browser
- 📱 Responsive design otomatis  
- 🎨 UI yang cantik tanpa CSS
- ⚡ Hot reload untuk development

Ini adalah kekuatan Streamlit! Bayangkan kalau kita harus buat ini dengan HTML, CSS, JavaScript - bisa puluhan bahkan ratusan baris!

**Stage 0 selesai!** Sekarang kita punya fondasi yang solid untuk melanjutkan ke Stage 1, dimana kita akan menambahkan interaktivitas dengan input dari user.

Ada pertanyaan tentang Stage 0 sebelum kita lanjut?"

---

## 📝 TIPS PRESENTASI
---

### **Pacing & Timing:**
- **Total waktu Stage 0: 5-7 menit**
- Jangan terburu-buru, biarkan audience melihat setiap langkah
- Pause sejenak setelah setiap konsep penting
- Berikan waktu untuk audience bertanya

### **Engagement Tips:**
- Sering bertanya: "Apakah ini terlihat jelas?"
- Gunakan analogi: "Ini seperti magic, tapi dengan code!"
- Tunjukkan antusiasme: "Lihat betapa mudahnya!"
- Libatkan audience: "Ada yang sudah pernah coba Streamlit?"

### **Technical Tips:**
- Pastikan font di editor cukup besar untuk audience
- Zoom browser saat demo agar semua bisa lihat
- Siapkan backup jika ada masalah koneksi
- Test run sebelum presentasi dimulai

### **Transisi ke Stage 1:**
"Sekarang kita sudah punya halaman basic, tapi masih statis. Di Stage 1, kita akan buat aplikasi kita bisa menerima input dari user. Mari kita lanjut!"

---

## 🎯 KEY TAKEAWAYS UNTUK AUDIENCE
---

1. **Streamlit sangat mudah untuk pemula**
2. **Dari Python script ke web app dalam hitungan menit**  
3. **Pattern `run()` function untuk modular code**
4. **Hot reload membuat development sangat cepat**
5. **UI cantik tanpa perlu tahu HTML/CSS**

---

*💡 Catatan: Sesuaikan kecepatan bicara dengan level audience dan jangan lupa untuk sering-sering check apakah mereka masih mengikuti!*