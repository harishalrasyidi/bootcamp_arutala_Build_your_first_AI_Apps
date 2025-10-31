import streamlit as st

def run():
    """
    Stage 1: Add Text Input
    Menambahkan input teks untuk menerima topik dari user
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

if __name__ == "__main__":
    run()
