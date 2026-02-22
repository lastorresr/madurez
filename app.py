import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Diagnóstico de Madurez Organizacional", layout="wide")

st.title("Diagnóstico de Madurez Organizacional")

st.markdown("""
Instrumento basado en el Modelo de 5 Fases de Madurez Organizacional.

Indique en qué medida cada afirmación describe su organización actualmente:

1 = No describe mi organización  
2 = Describe parcialmente  
3 = Describe claramente mi organización  
""")

st.divider()

# ---------------------------------------------------------
# MODELO ORGANIZADO POR DIMENSIONES
# ---------------------------------------------------------

modelo = {

    "Alineación Estratégica": {
        1: "La organización está estructurada principalmente alrededor de áreas funcionales y líneas de producto.",
        2: "Se reconoce la importancia de los procesos dentro de la estrategia organizacional.",
        3: "Los procesos están vinculados explícitamente con los objetivos estratégicos.",
        4: "La optimización de procesos es utilizada como fuente de ventaja competitiva.",
        5: "Existe integración estratégica entre procesos propios, de clientes y proveedores dentro de una red de valor."
    },

    "Cultura y Liderazgo": {
        1: "La cultura organizacional está orientada principalmente a jerarquías funcionales.",
        2: "Los líderes impulsan iniciativas de reingeniería y mejora de procesos.",
        3: "Los líderes de proceso promueven el mejoramiento continuo y la agregación de valor.",
        4: "La cultura fomenta colaboración, transparencia y consenso.",
        5: "Las decisiones estratégicas se apoyan en análisis avanzado de información y simulación de escenarios."
    },

    "Personas": {
        1: "Los empleados se enfocan en cumplir expectativas de su jefe inmediato más que en el proceso completo.",
        2: "Algunos empleados han sido entrenados en modelación y mejora de procesos.",
        3: "Las personas trabajan colaborativamente en oportunidades de mejora de procesos.",
        4: "Los empleados anticipan impactos de cambios más allá de su área funcional.",
        5: "Las personas analizan información y relacionan metas organizacionales con procesos para generar innovación."
    },

    "Gobernabilidad": {
        1: "La estructura organizacional está centrada en departamentos funcionales con competencia interna.",
        2: "Existen intentos de integración entre áreas, pero las decisiones siguen siendo funcionales.",
        3: "Existen indicadores de gestión de procesos que soportan el mejoramiento continuo.",
        4: "Se utilizan cuadros de mando e incentivos vinculados al desempeño de procesos.",
        5: "La estructura organizacional permite adaptación ágil ante cambios constantes."
    },

    "Procesos": {
        1: "Los procesos son estáticos y la comunicación entre áreas es principalmente informal.",
        2: "Se han definido algunos procesos interfuncionales con mejoras limitadas.",
        3: "Los procesos son la base de la gestión organizacional.",
        4: "Se aplican métodos estructurados de control y mejora continua.",
        5: "Existe integración y optimización de procesos inter-compañía e innovación constante."
    },

    "Tecnología Informática": {
        1: "Los sistemas informáticos están orientados a necesidades funcionales y no están integrados.",
        2: "Se han implementado sistemas integrados como ERP.",
        3: "La tecnología apoya la automatización y control de procesos.",
        4: "Se utilizan plataformas BPM y centros de competencia para soportar procesos.",
        5: "La infraestructura tecnológica soporta múltiples escenarios de negocio y análisis avanzado."
    }
}

opciones = [
    "1 - No describe mi organización",
    "2 - Describe parcialmente",
    "3 - Describe claramente mi organización"
]

respuestas_dimensiones = {}

# ---------------------------------------------------------
# CAPTURA DE RESPUESTAS
# ---------------------------------------------------------

for dimension in modelo:
    st.subheader(dimension)
    respuestas_dimensiones[dimension] = {}

    for fase in modelo[dimension]:
        respuesta = st.radio(
            modelo[dimension][fase],
            opciones,
            key=f"{dimension}_{fase}"
        )

        valor = int(respuesta[0])
        respuestas_dimensiones[dimension][fase] = valor

    st.divider()

# ---------------------------------------------------------
# CÁLCULO
# ---------------------------------------------------------

if st.button("Generar Diagnóstico"):

    resultados_dim = {}

    for dimension in respuestas_dimensiones:

        fases = respuestas_dimensiones[dimension]
        fase_predominante = max(fases, key=fases.get)
        resultados_dim[dimension] = fase_predominante

    # Nivel global = promedio de fases por dimensión
    nivel_global = round(np.mean(list(resultados_dim.values())), 2)

    # Redondeo al entero más cercano
    nivel_final = round(nivel_global)

    fases_nombre = {
        1: "Fase 1 - Silos Funcionales",
        2: "Fase 2 - Integración Funcional",
        3: "Fase 3 - Enfoque por Procesos",
        4: "Fase 4 - Empresa Optimizada",
        5: "Fase 5 - Empresa Inteligente"
    }

    st.success(f"Nivel Global de Madurez: {fases_nombre[nivel_final]}")

    st.write(f"Promedio global: {nivel_global}")

    st.divider()

    # ---------------------------------------------------------
    # GRÁFICO POR DIMENSIÓN
    # ---------------------------------------------------------

    dimensiones = list(resultados_dim.keys())
    valores = list(resultados_dim.values())

    fig, ax = plt.subplots()
    ax.bar(dimensiones, valores)
    ax.set_ylim(1,5)
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_title("Nivel de Madurez por Dimensión")
    plt.xticks(rotation=45)

    st.pyplot(fig)
