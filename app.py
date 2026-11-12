import math

import streamlit as st

BAD_HEART_IMAGE = "https://static.vecteezy.com/system/resources/previews/022/341/537/non_2x/heart-bad-red-plaster-valentine-s-day-icon-vector.jpg"
GOOD_HEART_IMAGE = "https://static.vecteezy.com/system/resources/previews/026/568/169/non_2x/heart-blink-and-say-okay-with-hand-vector.jpg"


def calcular_probabilidad_riesgo(edad: int, colesterol: float) -> float:
    # Regresión logística simple para estimar riesgo cardíaco usando dos variables
    # La fórmula devuelve una probabilidad entre 0 y 1.
    z = -8.0 + (0.08 * edad) + (0.025 * colesterol)
    return 1 / (1 + math.exp(-z))


st.set_page_config(page_title="Predicción riesgo cardíaco", page_icon="❤️", layout="centered")
st.title("Predicción de riesgo cardíaco")
st.write("Introduce la edad y el colesterol para saber si podría sufrir problemas del corazón.")

edad = st.number_input("¿Cuál es tu edad?", min_value=1, max_value=120, value=35, step=1)
colesterol = st.number_input("¿Cuál es tu colesterol?", min_value=50.0, max_value=500.0, value=180.0, step=1.0)

if st.button("Predecir"):
    probabilidad = calcular_probabilidad_riesgo(edad, colesterol)
    riesgo = probabilidad >= 0.5
    porcentaje = probabilidad * 100

    if riesgo:
        st.error(f"Sí va a sufrir del corazón. Riesgo estimado: {porcentaje:.1f}%")
        st.image(BAD_HEART_IMAGE, caption="Riesgo cardíaco identificado", width=300)
    else:
        st.success(f"No va a sufrir del corazón. Riesgo estimado: {porcentaje:.1f}%")
        st.image(GOOD_HEART_IMAGE, caption="Sin indicios de riesgo cardíaco", width=300)

    st.caption("Esta es una predicción simple basada en edad y colesterol para demostración.")