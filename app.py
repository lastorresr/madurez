import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------
# CONFIGURACIÓN
# ---------------------------------

st.set_page_config(page_title="Modelo de Madurez Organizacional", layout="wide")

st.title("Evaluación de Madurez Organizacional")
st.markdown("""
Instrumento basado en las 5 Fases de Madurez Organizacional.

**Escala de evaluación:**
1 = Fase 1 - Silos funcionales  
2 = Fase 2 - Integración funcional  
3 = Fase 3 - Enfoque por procesos  
4 = Fase 4 - Empresa optimizada  
5 = Fase 5 - Empresa inteligente  

Seleccione el nivel que mejor describe la realidad actual de la organización.
""")

st.divider()

# ---------------------------------
# PREGUNTAS BASADAS EN EL PDF
# ---------------------------------

preguntas = {

    "Alineación Estratégica": [
        "La organización está estructurada principalmente alrededor de áreas funcionales y líneas de producto.",
        "Se reconoce la importancia de los procesos dentro de la estrategia organizacional.",
        "Los procesos están vinculados explícitamente con los objetivos estratégicos.",
        "La optimización de procesos es utilizada como fuente de ventaja competitiva.",
        "Existe integración estratégica entre procesos propios, de clientes y proveedores dentro de una red de valor."
    ],

    "Cultura y Liderazgo": [
        "La cultura organizacional está orientada principalmente a jerarquías funcionales.",
        "Los líderes impulsan iniciativas de reingeniería y mejora de procesos.",
        "Los líderes de proceso promueven el mejoramiento continuo y la agregación de valor.",
        "La cultura fomenta colaboración, transparencia y consenso.",
        "Las decisiones estratégicas se apoyan en análisis avanzado de información y simulación de escenarios."
    ],

    "Personas": [
        "Los empleados se enfocan en cumplir expectativas de su jefe inmediato más que en el proceso completo.",
        "Algunos empleados han sido entrenados en modelación y mejora de procesos.",
        "Las personas trabajan colaborativamente en oportunidades de mejora de procesos.",
        "Los empleados anticipan impactos de cambios más allá de su área funcional.",
        "Las personas analizan información y relacionan metas organizacionales con procesos para generar innovación."
    ],

    "Gobernabilidad": [
        "La estructura organizacional está centrada en departamentos funcionales con competencia interna.",
        "Existen intentos de integración entre áreas, pero las decisiones siguen siendo funcionales.",
        "Existen indicadores de gestión de procesos que soportan el mejoramiento continuo.",
        "Se utilizan cuadros de mando e incentivos vinculados al desempeño de procesos.",
        "La estructura organizacional permite adaptación ágil ante cambios constantes."
    ],

    "Procesos": [
        "Los procesos son estáticos y la comunicación entre áreas es principalmente informal.",
        "Se han definido algunos procesos interfuncionales con mejoras limitadas.",
        "Los procesos son la base de la gestión organizacional.",
        "Se aplican métodos estructurados de control y mejora continua.",
        "Existe integración y optimización de procesos inter-compañía e innovación constante."
    ],

    "Tecnología Informática": [
        "Los sistemas informáticos están orientados a necesidades funcionales y no están integrados.",
        "Se han implementado sistemas integrados como ERP.",
        "La tecnología apoya la automatización y control de procesos.",
        "Se utilizan plataformas BPM y centros de competencia para soportar procesos.",
        "La infraestructura tecnológica soporta múltiples escenarios de negocio y análisis avanzado."
    ]
}

# ---------------------------------
# CAPTURA DE RESPUESTAS
# ---------------------------------

respuestas = {}

for dimension in preguntas:
    st.subheader(dimension)
    respuestas[dimension] = []

    for pregunta in preguntas[dimension]:
        valor = st.slider(
            pregunta,
            min_value=1,
            max_value=5,
            value=3
        )
        respuestas[dimension].append(valor)

    st.divider()

# ---------------------------------
# EVALUACIÓN
# ---------------------------------

if st.button("Calcular Nivel de Madurez"):

    promedios = {}
    total = 0
    cantidad_total = 0

    for dimension in respuestas:
        promedio_dim = np.mean(respuestas[dimension])
        promedios[dimension] = promedio_dim
        total += sum(respuestas[dimension])
        cantidad_total += len(respuestas[dimension])

    promedio_global = total / cantidad_total

    # Determinación de fase

    if promedio_global < 1.5:
        nivel = "Fase 1 - Silos Funcionales"
    elif promedio_global < 2.5:
        nivel = "Fase 2 - Integración Funcional"
    elif promedio_global < 3.5:
        nivel = "Fase 3 - Enfoque por Procesos"
    elif promedio_global < 4.5:
        nivel = "Fase 4 - Empresa Optimizada"
    else:
        nivel = "Fase 5 - Empresa Inteligente"

    st.success(f"Nivel Global de Madurez: {nivel}")
    st.write(f"Promedio Global: {round(promedio_global, 2)}")

    st.divider()

    # ---------------------------------
    # GRÁFICO RESUMEN
    # ---------------------------------

    dimensiones = list(promedios.keys())
    valores = list(promedios.values())

    fig, ax = plt.subplots()
    ax.bar(dimensiones, valores)
    ax.set_ylim(0, 5)
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_title("Resultado por Dimensión")
    plt.xticks(rotation=45)

    st.pyplot(fig)
