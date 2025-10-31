import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Demo Streamlit Widgets", page_icon="🚀")

# 1. st.title() - Judul aplikasi
st.title("Aplikasi AI Pertamaku 🚀")

st.markdown("**Demo 4 Widget Dasar Streamlit**")
st.divider()

# 2. st.text_input() - Input topik dari user
user_topic = st.text_input("Masukkan topik konten:")

# Tampilkan apa yang diketik user
if user_topic:
    st.write(f"Anda mengetik: **{user_topic}**")

# 3. st.button() - Tombol untuk generate
if st.button("Generate Konten"):
    # Validasi input
    if not user_topic.strip():
        st.warning("Mohon masukkan topik terlebih dahulu!")
    else:
        # Simulasi hasil AI (untuk demo)
        hasil_dari_ai = f"""
        # {user_topic}
        
        ## Pendahuluan
        Topik "{user_topic}" adalah salah satu hal yang menarik untuk dibahas.
        
        ## Poin Utama
        1. **Aspek pertama** - Penjelasan singkat tentang aspek pertama
        2. **Aspek kedua** - Detail tentang hal penting kedua  
        3. **Aspek ketiga** - Informasi tambahan yang berguna
        
        ## Kesimpulan
        Demikian pembahasan singkat tentang {user_topic}. Semoga bermanfaat!
        
        ---
        *Konten ini dibuat dengan AI Content Generator*
        """
        
        # 4. st.info() - Tampilkan hasil
        st.success("✅ Konten berhasil dibuat!")
        st.info(hasil_dari_ai)

# Demo widget tambahan
st.divider()
st.markdown("**Widget Tambahan:**")

# Contoh widget lain yang sering dipakai
col1, col2 = st.columns(2)

with col1:
    st.selectbox("Pilih kategori:", ["Teknologi", "Bisnis", "Lifestyle", "Pendidikan"])
    
with col2:
    st.slider("Panjang konten (kata):", 100, 500, 250)

# Footer
st.markdown("""
---
💡 **Konsep Inti Streamlit**: Setiap interaksi widget → skrip dijalankan ulang dari atas ke bawah!
""")