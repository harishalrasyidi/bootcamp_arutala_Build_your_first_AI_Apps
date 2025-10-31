import streamlit as st

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
    Stage 2: Add Button and Basic Interaction
    Menambahkan tombol dan interaksi dasar dengan konten yang di-generate sederhana
    """
    
    # Judul aplikasi
    st.title("AI Content Generator 🚀")
    
    # Teks pembuka
    st.write("Selamat datang di aplikasi AI Content Generator!")
    st.write("Masukkan topik yang ingin Anda buatkan kontennya.")
    
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
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            # Generate konten sederhana (belum menggunakan AI)
            hasil_konten = generate_simple_content(user_topic)
            
            st.success("✅ Konten berhasil dibuat!")
            st.subheader("Hasil Konten:")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()
