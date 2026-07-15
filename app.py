import streamlit as st
import cloudinary
import cloudinary.utils

# Configuração do Cloudinary
cloudinary.config(
    cloud_name="v4s0xg7h",
    api_key="242294331659617",
    api_secret="Agv8UnhNhV3IMt7sZfkJXcYZcg8"
)

# Estilo para o site
st.markdown("""
    <style>
    .stApp { background-color: #fdf0f5; }
    h1 { color: #d63384; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💅 JS Ju Soldan")

# Coloque aqui o nome da foto que você subiu no Cloudinary
# Exemplo: Se sua foto se chama 'unha1', troque 'sample' por 'unha1'
foto_id = "Unha_01" 

try:
    foto_url = cloudinary.utils.cloudinary_url(foto_id, fetch_format="auto", quality="auto")[0]
    st.image(foto_url, caption="Design em destaque", use_container_width=True)
except:
    st.warning("Suba uma foto no Cloudinary e atualize o nome no código!")

st.link_button("📅 Agendar horário pelo WhatsApp", "https://wa.me/5544998428856")
