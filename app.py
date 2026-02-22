import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Diagnóstico de Madurez Organizacional", layout="wide")

st.title("Diagnóstico de Madurez Organizacional")

st.markdown("""
Seleccione la descripción que mejor representa la situación actual de su organización en cada dimensión.
""")

st.divider()

modelo = {

    "Alineación Estratégica": [
        "Fase 1: La organización está centrada en áreas funcionales y líneas de producto.",
        "Fase 2: Se reconoce la importancia de los procesos dentro de la estrategia organizacional.",
        "Fase 3: Los procesos están vinculados explícitamente con los objetivos estratégicos.",
        "Fase 4: La optimización de procesos es utilizada como fuente de ventaja competitiva.",
        "Fase 5: Existe integración estratégica entre procesos propios, clientes y proveedores dentro de una red de valor."
    ],

    "Cultura y Liderazgo": [
        "Fase 1: Cultura orientada a jerarquías funcionales.",
        "Fase 2: Líderes impulsan reingeniería y mejora de procesos.",
        "Fase 3: Cultura basada en líderes de proceso y mejoramiento continuo.",
        "Fase 4: Cultura basada en colaboración, transparencia y consenso.",
        "Fase 5: Liderazgo apoyado en análisis avanzado y simulación de escenarios."
    ],

    "Personas": [
        "Fase 1: Enfoque en cumplir expectativas del jefe inmediato.",
        "Fase 2: Algunas personas entrenadas en modelación de procesos.",
        "Fase 3: Trabajo colaborativo en mejora de procesos.",
        "Fase 4: Empleados anticipan impactos más allá de su función.",
        "Fase 5: Personas relacionan metas con procesos y generan innovación."
    ],

    "Gobernabilidad": [
        "Fase 1: Estructura centrada en departamentos funcionales.",
        "Fase 2: Integración limitada, decisiones funcionales.",
        "Fase 3: Indicadores de gestión de procesos definidos.",
        "Fase 4: Cuadros de mando e incentivos vinculados a procesos.",
        "Fase 5: Estructura ágil que permite adaptación rápida."
    ],

    "Procesos": [
        "Fase 1: Procesos estáticos y comunicación informal.",
        "Fase 2: Procesos interfuncionales definidos parcialmente.",
        "Fase 3: Procesos como base de la gestión.",
        "Fase 4: Métodos estructurados de control y mejora continua.",
        "Fase 5: Integración y optimización inter-compañía e innovación constante."
    ],

    "Tecnología Informática": [
        "Fase 1: Sistemas funcionales no integrados.",
        "Fase 2: Implementación de ERP.",
        "Fase 3: Tecnología orientada a automatización de procesos.",
        "Fase 4: Uso de BPM y centros de competencia.",
        "Fase 5: Infraestructura que soporta múltiples escenarios de negocio."
    ]
}

respuestas = {}

for dimension in modelo:
    st.subheader(dimension)

    opcion = st.radio(
        "Seleccione una opción:",
        modelo[dimension],
        key=dimension
    )

    # Extraer número de fase
    fase = int(opcion.split(":")[0].replace("Fase","").strip())
    respuestas[dimension] = fase

    st.divider()

if st.button("Generar Diagnóstico"):

    valores = list(respuestas.values())
    promedio = round(np.mean(valores),2)
    nivel_global = round(promedio)

    nombres_fase = {
        1: "Fase 1 - Silos Funcionales",
        2: "Fase 2 - Integración Funcional",
        3: "Fase 3 - Enfoque por Procesos",
        4: "Fase 4 - Empresa Optimizada",
        5: "Fase 5 - Empresa Inteligente"
    }

    st.success(f"Nivel Global de Madurez: {nombres_fase[nivel_global]}")
    st.write(f"Promedio global: {promedio}")

    st.divider()

    fig, ax = plt.subplots()
    ax.bar(respuestas.keys(), respuestas.values())
    ax.set_ylim(1,5)
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_title("Madurez por Dimensión")
    plt.xticks(rotation=45)

    st.pyplot(fig)
