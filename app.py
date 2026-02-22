import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Diagnóstico de Madurez Organizacional", layout="wide")

st.title("Diagnóstico de Madurez Organizacional")

st.markdown("""
Seleccione la descripción que mejor representa la situación actual de su organización en cada dimensión.

El modelo contempla cinco niveles evolutivos de madurez organizacional.
""")

st.divider()

modelo = {

    "Alineación Estratégica": [
        "La organización está estructurada principalmente alrededor de áreas funcionales, líneas de producto o unidades independientes. La estrategia se gestiona desde cada área sin una visión integral de procesos.",
        
        "La organización reconoce la importancia de los procesos dentro de la estrategia. Se discute su rol, aunque la estructura funcional sigue predominando.",
        
        "Los procesos están claramente vinculados con los objetivos estratégicos mediante factores críticos de éxito. La gestión estratégica incluye la gestión por procesos.",
        
        "La optimización de procesos es un eje central para lograr ventajas competitivas. La estrategia se ejecuta a través de la mejora sistemática y controlada de procesos.",
        
        "La alineación estratégica integra procesos internos con los de clientes y proveedores dentro de una red de valor, buscando agilidad, competitividad y adaptación continua."
    ],

    "Cultura y Liderazgo": [
        "La cultura organizacional está orientada principalmente a jerarquías funcionales. Los líderes priorizan resultados de su área sobre la visión integral.",
        
        "Los líderes promueven iniciativas de mejora y reingeniería de procesos, aunque la cultura funcional aún es predominante.",
        
        "La cultura gira alrededor de líderes o dueños de proceso que impulsan el mejoramiento continuo y la generación de valor.",
        
        "Predomina una cultura de colaboración, transparencia y consenso. El liderazgo fomenta responsabilidad compartida por los procesos.",
        
        "El liderazgo se apoya en análisis avanzado de información y simulación de escenarios para la toma de decisiones estratégicas y operativas."
    ],

    "Personas": [
        "Los empleados se enfocan principalmente en cumplir con las expectativas de su jefe inmediato, con poco entendimiento de los procesos de principio a fin.",
        
        "Algunos colaboradores han recibido formación en modelación y mejora de procesos y comienzan a comprender su impacto transversal.",
        
        "Las personas trabajan de manera colaborativa en la identificación y mejora de procesos organizacionales.",
        
        "Los empleados anticipan el impacto de los cambios en procesos más allá de su función, colaboran activamente y comparten información.",
        
        "Las personas analizan información estratégica, relacionan metas organizacionales con procesos y generan innovación continua."
    ],

    "Gobernabilidad": [
        "La estructura organizacional está centrada en departamentos funcionales con indicadores individuales y competencia interna.",
        
        "Existen intentos de integración entre áreas, pero las decisiones siguen tomándose principalmente por funciones.",
        
        "Existen indicadores de gestión de procesos que sirven como base para el mejoramiento continuo.",
        
        "Se utilizan cuadros de mando e incentivos alineados al desempeño de procesos y a la mejora continua.",
        
        "La estructura organizacional permite adaptarse ágilmente a cambios constantes y gestionar transformaciones de manera sistemática."
    ],

    "Procesos": [
        "Los procesos son estáticos y la comunicación entre áreas es principalmente informal y no estructurada.",
        
        "Se han definido algunos procesos interfuncionales, aunque el mejoramiento es limitado.",
        
        "Los procesos constituyen la base de la gestión organizacional y se aplica mejoramiento continuo.",
        
        "Se implementan métodos estructurados para el control, medición y optimización sistemática de procesos.",
        
        "Existe integración y optimización de procesos inter-compañía, con innovación constante y entrenamiento continuo."
    ],

    "Tecnología Informática": [
        "Los sistemas informáticos están orientados a necesidades funcionales específicas y no están integrados.",
        
        "Se han implementado sistemas integrados (como ERP) para mejorar la coordinación entre áreas.",
        
        "La tecnología apoya la automatización, monitoreo y control de procesos organizacionales.",
        
        "Se utilizan plataformas BPM y la infraestructura tecnológica responde ágilmente a cambios en procesos.",
        
        "La infraestructura tecnológica soporta múltiples escenarios de negocio, análisis avanzado y adaptación estratégica."
    ]
}

respuestas = {}

for dimension in modelo:
    st.subheader(dimension)

    opcion = st.radio(
        "Seleccione la opción que mejor describe su organización:",
        modelo[dimension],
        key=dimension
    )

    fase = modelo[dimension].index(opcion) + 1
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
    st.write(f"Promedio global obtenido: {promedio}")

    st.divider()

    fig, ax = plt.subplots()
    ax.bar(respuestas.keys(), respuestas.values())
    ax.set_ylim(1,5)
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_title("Madurez Organizacional por Dimensión")
    plt.xticks(rotation=45)

    st.pyplot(fig)
