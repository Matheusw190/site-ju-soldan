import streamlit as st
import cloudinary
import cloudinary.utils

# Configuração simples
cloudinary.config(
    cloud_name="v4s0xg7h",
    api_key="242294331659617",
    api_secret="Agv8UnhNhV3IMt7sZfkJXcYZcg8"
)

st.title("Teste de Conexão")

st.write("Se você está vendo este texto, o código está funcionando!")

# Tentar exibir a imagem de teste
try:
    foto_url = cloudinary.utils.cloudinary_url("sample", fetch_format="auto", quality="auto")[0]
    st.image(foto_url, caption="Foto de teste")
    st.write(f"URL da imagem: {foto_url}")
except Exception as e:
    st.error(f"Erro ao carregar a foto: {e}")
