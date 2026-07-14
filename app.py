import streamlit as st

# Título e Nome do Salão
st.title("💅 Ju Soldan - Nail Design")
st.subheader("Beleza • Cuidado • Confiança")

# Tabela de Preços
st.markdown("### 📋 Tabela de Preços")

# Criando a estrutura de serviços
servicos = {
    "Manicure": "R$ 25,00",
    "Pedicure": "R$ 35,00",
    "Alongamento": "R$ 100,00",
    "Esmalt. em gel": "R$ 50,00",
    "Blindagem": "R$ 65,00"
}

# Exibindo os serviços principais
for item, preco in servicos.items():
    st.text(f"{item.ljust(20)} {preco}")

# Seção de Manutenção
st.markdown("---")
st.markdown("### 🔄 Manutenção")
st.text(f"{'Unha de Gel'.ljust(20)} R$ 80,00")

# Botão de Agendamento com seu número
link_whatsapp = "https://wa.me/5544998428856" 
st.markdown("---")
st.link_button("📅 Agendar horário pelo WhatsApp", link_whatsapp)
