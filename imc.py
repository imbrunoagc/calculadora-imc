import streamlit as st

with st.sidebar: # TEXTO na Barrinha lateral
    st.title("Calculado IMC")
    st.header("IMC: Definição?")
    st.write("Indice de Massa Corporal (IMC)")
    st.write("É um indice que relaciona peso e altura de uma pessoa")
    st.write("É utilizado como uma medida de saúde geral e para determinar se uma pessoa está em um peso")

st.title("Calculadora")

# Variaveis que armazenam valores inputados pelo usuario
peso = st.number_input(label="Digite seu peso em kg", min_value=0.0)
altura = st.number_input(label="Digite sua altura em metros", min_value=0.0)

if st.button("Calcular"): # Se o botão for pressionado vai acontcer o que estiver dentro do IF
    imc = peso / (altura ** 2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal

    if imc < 18.5:
        resultado = {
            "classe": "Abaixo do peso",
            "delta": imc_delta
        }

    elif 18.5 <= imc < 25:
        resultado = {
            "classe": "Peso ideal",
            "delta": imc_delta
        }

    elif 25 <= imc <= 30:
        resultado = {
            "classe": "SobrePeso",
            "delta": imc_delta
        }
    
    elif imc < 40:
        resultado = {
            "classe": "Obesidade",
            "delta": imc_delta
        }
    
    else:
        resultado = {
            "classe": "Obesidade morbida",
            "delta": imc_delta
        }
    
    st.code(f"O resultado é {resultado}") # Exebição de código no streamlit
    
    col1, col2 = st.columns(2)

    col1.metric("IMC Classificado", resultado['classe'], resultado['delta'], delta_color="inverse")
    col2.metric("IMC Calculado", round(imc, 2), resultado['delta'], delta_color="off")
    
    st.divider()
    st.text("Fonte")

    st.image("./regua-imc.png")