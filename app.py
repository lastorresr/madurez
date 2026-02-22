import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Evaluador de Madurez", layout="wide")

st.title("Modelo de Evaluación de Madurez Organizacional")

dimensiones = {
    "Alineación Estratégica": 5,
    "Cultura y Liderazgo": 5,
    "Personas": 5,
    "Gobernabilidad": 5,
    "Procesos y TI": 5
}

respuestas = {}

for dim in dimensiones:
    st.subheader(dim)
    respuestas[dim] = []
    for i in range(dimensiones[dim]):
        valor = st.slider(
            f"{dim} - Ítem {i+1}",
            min_value=1,
            max_value=5,
            value=3
        )
        respuestas[dim].append(valor)

if st.button("Calcular Nivel de Madurez"):

    promedios = []
    for dim in respuestas:
        promedio = np.mean(respuestas[dim])
        promedios.append(promedio)

    igm = np.mean(promedios)

    if igm < 2:
        fase = "Fase 1 – Silos funcionales"
    elif igm < 3:
        fase = "Fase 2 – Integración funcional"
    elif igm < 4:
        fase = "Fase 3 – Enfoque por procesos"
    elif igm < 4.5:
        fase = "Fase 4 – Empresa optimizada"
    else:
        fase = "Fase 5 – Empresa inteligente"

    st.success(f"Índice Global de Madurez (IGM): {igm:.2f}")
    st.info(f"Nivel: {fase}")

    # -------- GRÁFICO RADAR --------
    etiquetas = list(dimensiones.keys())
    valores = promedios + [promedios[0]]

    angulos = np.linspace(0, 2 * np.pi, len(etiquetas), endpoint=False).tolist()
    angulos += angulos[:1]

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angulos, valores)
    ax.fill(angulos, valores, alpha=0.25)

    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(etiquetas)
    ax.set_ylim(0, 5)

    st.pyplot(fig)
