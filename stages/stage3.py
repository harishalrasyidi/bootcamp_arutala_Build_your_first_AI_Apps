import streamlit as st
import os
from dotenv import load_dotenv

def check_environment():
    """
    Fungsi untuk mengecek dan setup environment variables
    """
    # Load environment variables
    load_dotenv()
    
    # Check Google API Key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("⚠️ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
        st.info("💡 Buat file .env dan tambahkan: GOOGLE_API_KEY=your_api_key_here")
        return False
    else:
        st.success("✅ Google API Key berhasil dimuat!")
        return True

def generate_simple_content(topic):
    """
    Fungsi sederhana untuk generate konten tanpa AI
    (simulasi sebelum integrasi AI sesungguhnya)
    """
    return f"""
    **Judul:** {topic}
    
    **Pendahuluan:**
    {topic} adalah topik yang menarik untuk dibahas. Mari kita eksplorasi lebih dalam.
    
    **Poin Utama:**
    1. Pentingnya memahami {topic}
    2. Manfaat dari {topic} dalam kehidupan sehari-hari
    3. Tips praktis terkait {topic}
    
    **Kesimpulan:**
    {topic} memiliki dampak positif yang signifikan jika diterapkan dengan baik.
    
    **Call to Action:**
    Mulai terapkan pengetahuan tentang {topic} dalam aktivitas Anda!
    """

def run():
    """
    Stage 3: Add Environment Setup
    Menambahkan konfigurasi environment dan setup API key
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="AI Content Generator",
        page_icon="🚀"
    )
    
    # Judul aplikasi
    st.title("AI Content Generator 🚀")
    
    # Teks pembuka
    st.write("Selamat datang di aplikasi AI Content Generator!")
    st.write("Aplikasi ini menggunakan Google Gemini AI untuk membuat konten berkualitas.")
    
    # Check environment setup
    env_ready = check_environment()
    
    st.divider()
    
    # Input teks dari user
    user_topic = st.text_input(
        "Masukkan topik konten:",
        placeholder="Contoh: Tips Belajar Python, Manfaat AI dalam Bisnis, dll."
    )
    
    # Tampilkan topik yang dimasukkan user
    if user_topic:
        st.write(f"**Topik yang Anda masukkan:** {user_topic}")
    
    # Tombol untuk generate konten
    if st.button("Generate Konten"):
        if not env_ready:
            st.error("❌ Environment belum siap! Pastikan API key sudah dikonfigurasi.")
        elif not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            # Generate konten sederhana (belum menggunakan AI)
            with st.spinner("🤖 Sedang memproses..."):
                hasil_konten = generate_simple_content(user_topic)
            
            st.success("✅ Konten berhasil dibuat!")
            st.subheader("Hasil Konten:")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()
