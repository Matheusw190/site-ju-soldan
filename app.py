import streamlit as st
import cloudinary
import cloudinary.uploader

# 1. Configuração do Cloudinary
cloudinary.config(
    cloud_name="v4s0xg7h",
    api_key="242294331659617",
    api_secret="Agv8UnhNhV3IMt7sZfkJXcYZcg8"
)

st.set_page_config(page_title="Ju Soldan - Nail Design", page_icon="💅")

# CSS para o seu "Fundo e Arte"
st.markdown("""
    <style>
    .stApp {
        background-color: #fdf0f5; /* Cor de fundo suave */
    }
    h1 {
        color: #d63384;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💅 Ju Soldan - Nail Design")

# 2. Exibindo uma foto do Cloudinary
# DICA: Para mudar a foto, basta trocar o 'public_id' abaixo 
# pelo nome da foto que você subir no seu Cloudinary
try:
    foto_url = cloudinary.utils.cloudinary_url("sample", fetch_format="auto", quality="auto")[0]
    st.image(foto_url, caption="Design em destaque", use_container_width=True)
except Exception as e:
    st.error("Erro ao carregar imagem. Verifique o nome no Cloudinary.")

# 3. Seção de Agendamento
st.subheader("Gostou do estilo?")
st.link_button("📅 Agendar horário pelo WhatsApp", "https://wa.me/5544998428856")
