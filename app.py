import streamlit as st
import cloudinary
import cloudinary.utils

# 1. Configuração do Cloudinary
cloudinary.config(
    cloud_name="v4s0xg7h",
    api_key="242294331659617",
    api_secret="Agv8UnhNhV3IMt7sZfkJXcYZcg8"
)

# 2. Estilo Visual (CSS)
st.markdown("""
    <style>
    /* Fundo preto */
    .stApp { background-color: #000000 !important; }
    
    /* Letras Douradas */
    h1, h2, h3, p, div { 
        color: #FFD700 !important; 
        font-family: 'Georgia', serif !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Conteúdo do Site
st.title("💅 JS Ju Soldan")
st.subheader("Nail Design de Excelência")

# 4. Exibição da Imagem (Configurada para Unha_01)
foto_id = "Unha_01" 

try:
    foto_url = cloudinary.utils.cloudinary_url(foto_id, fetch_format="auto", quality="auto")[0]
    st.image(foto_url, use_container_width=True)
except:
    st.error(f"Erro: A foto '{foto_id}' não foi encontrada no Cloudinary. Verifique o nome na sua biblioteca.")

st.markdown("<br>", unsafe_allow_html=True)
st.link_button("📅 Agendar horário pelo WhatsApp", "https://wa.me/5544998428856")
