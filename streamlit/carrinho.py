import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão (1kg)": 8.50,
    "Carne (1kg)": 60.0,
    "Batata (1kg)": 6.99,
    "Leite (1l)": 7.99
}

def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total

itens_selecionados = st.multiselect(
   label =  "Selecione os itens do supermercado:",
    options=list(precos_itens.keys())
)

if itens_selecionados:
    st.subheader("Itens Selecionados:")
    for item in itens_selecionados:
        st.write(f"- {item}: R$ {precos_itens[item]:.2f}")
    total_compra = calcular_preco_total(itens_selecionados)
    st.divider()
    st.metric(label="Total da Compra", value=f"R$ {total_compra:.2f}")

    pagamento = st.number_input("Informe a quantidade do pagamento")
    troco = pagamento - total_compra
    st.write(f"O troco é : R${troco:.2f}")
else:
    st.info("Nenhum item selecionado. Marque os produtos acima para ver o valor total.")