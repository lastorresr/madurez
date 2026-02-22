import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Diagnóstico de Madurez Organizacional", layout="wide")

st.title("Diagnóstico de Madurez Organizacional")
st.markdown("""
Instrumento basado en el Modelo de 5 Fases de Madurez Organizacional.

**Indique en qué medida cada afirmación describe su organización actualmente:**

1 = No describe mi organización  
2 = Describe parcialmente  
3 = Describe claramente mi organización  
""")

st.divider()

# -------------------------------------------------
# PREGUNTAS ORGANIZADAS POR FASE (NO SE MODIFICAN)
# -------------------------------------------------

modelo = {

    "Fase 1 - Silos Funcionales": [
        "La organización está estructurada principalmente alrededor de áreas funcionales y líneas de producto.",
        "La cultura organizacional está orientada principalmente a jerarquías funcionales.",
        "Los empleados se enfocan en cumplir expectativas de su jefe inmediato más que en el proceso completo.",
        "La estructura organizacional está centrada en departamentos funcionales con competencia interna.",
        "Los procesos son estáticos y la comunicación entre áreas es principalmente informal.",
        "Los sistemas informáticos están orientados a necesidades funcionales y no están integrados."
    ],

    "Fase 2 - Integración Funcional": [
        "Se reconoce la importancia de los procesos dentro de la estrategia organizacional.",
        "Los líderes impulsan iniciativas de reingeniería y mejora de procesos.",
        "Algunos empleados han sido entrenados en modelación y mejora de procesos.",
        "Existen intentos de integración entre áreas, pero las decisiones siguen siendo funcionales.",
        "Se han definido algunos procesos interfuncionales con mejoras limitadas.",
        "Se han implementado sistemas integrados como ERP."
    ],

    "Fase 3 - Enfoque por Procesos": [
        "Los procesos están vinculados explícitamente con los objetivos estratégicos.",
        "Los líderes de proceso promueven el mejoramiento continuo y la agregación de valor.",
        "Las personas trabajan colaborativamente en oportunidades de mejora de procesos.",
        "Existen indicadores de gestión de procesos que soportan el mejoramiento continuo.",
        "Los procesos son la base de la gestión organizacional.",
        "La tecnología apoya la automatización y control de procesos."
    ],

    "Fase 4 - Empresa Optimizada": [
        "La optimización de procesos es utilizada como fuente de ventaja competitiva.",
        "La cultura fomenta colaboración, transparencia y consenso.",
        "Los empleados anticipan impactos de cambios más allá de su área funcional.",
        "Se utilizan cuadros de mando e incentivos vinculados al desempeño de procesos.",
        "Se aplican métodos estructurados de control y mejora continua.",
        "Se utilizan plataformas BPM y centros de competencia para soportar procesos."
    ],

    "Fase 5 - Empresa Inteligente": [
        "Existe integración estratégica entre procesos propios, de clientes y proveedores dentro de una red de valor.",
        "Las decisiones estratégicas se apoyan en análisis avanzado de información y simulación de escenarios.",
        "Las personas analizan información y relacionan metas organizacionales con procesos para generar innovación.",
        "La estructura organizacional permite adaptación ágil ante cambios constantes.",
        "Existe integración y optimización de procesos inter-compañía e innovación constante.",
        "La infraestructura tecnológica soporta múltiples escenarios de negocio y análisis avanzado."
    ]
}

# -------------------------------------------------
# ESCALA
# -------------------------------------------------

opciones = [
    "1 - No describe mi organización",
    "2 - Describe parcialmente",
    "3 - Describe claramente mi organización"
]

respuestas = {}

# -------------------------------------------------
# CAPTURA DE RESPUESTAS
# -------------------------------------------------

for fase in modelo:
    st.subheader(fase)
    respuestas[fase] = []

    for pregunta in modelo[fase]:
        respuesta = st.radio(
            pregunta,
            opciones,
            key=f"{fase}_{pregunta}"
        )
        valor = int(respuesta[0])
        respuestas[fase].append(valor)

    st.divider()

# -------------------------------------------------
# CÁLCULO DE RESULTADOS
# -------------------------------------------------

if st.button("Generar Diagnóstico"):

    promedios = {}

    for fase in respuestas:
        promedios[fase] = np.mean(respuestas[fase])

    # Ordenar fases por nivel
    fases_ordenadas = sorted(promedios.items(), key=lambda x: x[1], reverse=True)

    fase_predominante = fases_ordenadas[0]
    segunda_fase = fases_ordenadas[1]

    st.success(f"Fase Predominante: {fase_predominante[0]}")
    st.write(f"Puntaje promedio: {round(fase_predominante[1],2)}")

    st.info(f"Fase Emergente: {segunda_fase[0]}")
    st.write(f"Puntaje promedio: {round(segunda_fase[1],2)}")

    st.divider()

    # -------------------------------------------------
    # GRÁFICO COMPARATIVO
    # -------------------------------------------------

    nombres = list(promedios.keys())
    valores = list(promedios.values())

    fig, ax = plt.subplots()
    ax.bar(nombres, valores)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Nivel de presencia (1-3)")
    ax.set_title("Comparativo de Madurez por Fase")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.divider()

    # -------------------------------------------------
    # INTERPRETACIÓN AUTOMÁTICA
    # -------------------------------------------------

    st.subheader("Interpretación General")

    if fase_predominante[1] >= 2.5:
        st.write("La organización muestra características claramente definidas de esta fase.")
    elif fase_predominante[1] >= 1.8:
        st.write("La organización se encuentra en transición hacia esta fase.")
    else:
        st.write("La organización presenta rasgos iniciales de esta fase, pero aún no consolidados.")
