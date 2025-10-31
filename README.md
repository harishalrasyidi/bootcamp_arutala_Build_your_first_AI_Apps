# AI Content Generator dengan Streamlit 🚀

Aplikasi web sederhana untuk membuat konten menggunakan AI, dibangun dengan Streamlit dan Google Gemini AI.

## 📋 Konsep Inti Streamlit

**Konsep Magic**: Setiap skrip dieksekusi dari atas ke bawah. Setiap kali pengguna berinteraksi dengan widget (misalnya menekan tombol), seluruh skrip akan dijalankan ulang dari awal hingga akhir.

## 🧩 4 Widget Inti yang Digunakan

### 1. `st.title()` - Judul
```python
st.title("Aplikasi AI Pertamaku 🚀")
```
Menampilkan teks besar sebagai judul aplikasi.

### 2. `st.text_input()` - Kotak Input Teks
```python
user_topic = st.text_input("Masukkan topik konten:")
```
- Menampilkan kotak input untuk user mengetik
- **Return value**: String yang diketik user (tersimpan di variabel `user_topic`)

### 3. `st.button()` - Tombol
```python
if st.button("Generate Konten"):
    # Kode di sini hanya berjalan JIKA tombol diklik
    pass
```
- **Return value**: `True` jika tombol baru saja diklik, `False` di skenario lain
- Perfect untuk memicu aksi tertentu

### 4. `st.info()` - Penampil Output  
```python
hasil_dari_ai = "Ini adalah konten yang dihasilkan..."
st.info(hasil_dari_ai)
```
- Cara serbaguna untuk menampilkan output
- `st.info()` memberikan kotak biru yang bagus untuk hasil

## 🚀 Setup dan Menjalankan Aplikasi

### 1. Aktivasi Virtual Environment
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Atau jika menggunakan Command Prompt
venv\Scripts\activate.bat
```

### 2. Install Dependencies
```bash
pip install -r requirement.txt
```

### 3. Setup Environment Variables
Edit file `.env` dan tambahkan API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

**Cara mendapatkan Google AI API Key:**
1. Kunjungi: https://makersuite.google.com/app/apikey
2. Login dengan Google account
3. Buat API key baru
4. Copy dan paste ke file `.env`

### 4. Menjalankan Aplikasi

**Demo Sederhana (tanpa AI):**
```bash
streamlit run demo.py
```

**Aplikasi Lengkap (dengan AI):**
```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📁 Struktur File

```
testdrive_sourcecode/
├── app.py              # Aplikasi utama dengan AI integration
├── demo.py             # Demo sederhana konsep Streamlit
├── requirement.txt     # Dependencies
├── .env               # Environment variables (API keys)
├── venv/              # Virtual environment
└── README.md          # Dokumentasi ini
```

## 🔧 Teknologi yang Digunakan

- **Streamlit**: Framework UI untuk Python
- **Google Gemini AI**: Model AI untuk generate konten  
- **LangChain**: Framework untuk integrasi AI
- **Python-dotenv**: Manajemen environment variables

## 💡 Tips Penggunaan

1. **Semakin spesifik topik**, semakin baik hasil kontennya
2. **Contoh topik yang baik**:
   - "Tips Belajar Python untuk Pemula"
   - "Manfaat AI dalam Bisnis E-commerce"  
   - "Resep Masakan Sehat untuk Diet"

3. **Widget Interaction Flow**:
   ```
   User input → Widget interaction → Script re-runs → Output updates
   ```

## 🎯 Contoh Penggunaan

1. Buka aplikasi di browser
2. Masukkan topik di kotak input: "Tips Produktivitas"  
3. Klik tombol "Generate Konten"
4. AI akan memproses dan menampilkan hasil
5. Download konten jika diperlukan

## 🛠️ Troubleshooting

**Error: API Key tidak ditemukan**
- Pastikan file `.env` ada dan berisi `GOOGLE_API_KEY`
- Restart aplikasi setelah menambah API key

**Error: Module not found** 
- Pastikan virtual environment aktif
- Install ulang dependencies: `pip install -r requirement.txt`

**Port sudah digunakan**
- Gunakan port lain: `streamlit run app.py --server.port 8502`

## 📚 Next Steps

Setelah memahami konsep dasar, Anda bisa:

1. **Explore widget lain**: `st.selectbox()`, `st.slider()`, `st.file_uploader()`
2. **Tambah fitur**: Upload file, multiple output format
3. **Styling**: Custom CSS, themes, layouts
4. **State Management**: `st.session_state` untuk data persistence
5. **Deploy**: Streamlit Community Cloud, Heroku, atau platform lain

---

**Happy Coding! 🚀**

*Aplikasi ini dibuat untuk pembelajaran konsep Streamlit dan AI integration.*