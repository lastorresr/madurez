import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------

st.set_page_config(page_title="Modelo de Madurez Organizacional", layout="wide")

st.title("Modelo de Evaluación de Madurez Organizacional")
st.markdown("""
Este instrumento evalúa el nivel de madurez organizacional en cinco dimensiones clave.
  
**Escala de evaluación:**
1 = Inexistente  
2 = Inicial  
3 = Definido  
4 = Gestionado  
5 = Optimizado  
""")

st.divider()

# -------------------------------
# PREGUNTAS DEL MODELO
# -------------------------------

preguntas = {
    "Alineación Estratégica": [
        "La estrategia organizacional está formalmente definida y comunicada.",
        "Los procesos críticos están alineados con los objetivos estratégicos.",
        "Existen indicadores estratégicos vinculados a procesos.",
        "La optimización de procesos se considera fuente de ventaja competitiva.",
        "Existe integración estratégica con clientes y proveedores."
    ],
    "Cultura y Liderazgo": [
        "La alta dirección promueve activamente la gestión por procesos.",
        "Se fomenta la colaboración interfuncional.",
        "Las decisiones se basan en análisis de datos.",
        "Se promueve la mejora continua.",
        "Existe apertura organizacional al cambio."
    ],
    "Personas": [
        "Los empleados comprenden los procesos de principio a fin.",
        "Existe capacitación formal en mejora de procesos.",
        "El personal participa en iniciativas de mejora.",
        "Se trabaja en equipos interfuncionales.",
        "Los colaboradores comprenden cómo su rol impacta la estrategia."
    ],
    "Gobernabilidad": [
        "Existen dueños de proceso formalmente designados.",
        "Se utilizan KPIs para monitorear el desempeño de procesos.",
        "Existen mecanismos sistemáticos de seguimiento.",
        "Hay incentivos ligados al desempeño de procesos.",
        "La estructura organizacional facilita la gestión transversal."
    ],
    "Procesos y Tecnología Informática": [
        "Los procesos están documentados y actualizados.",
        "Existen procesos interfuncionales formalizados.",
        "Se aplican metodologías de mejora continua.",
        "Los sistemas de información están integrados.",
        "La tecnología soporta automatización y analítica de procesos."
    ]
}

# -------------------------------
# CAPTURA DE RESPUESTAS
# -------------------------------

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

# -------------------------------
# BOTÓN DE EVALUACIÓN
# -------------------------------

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

    # -------------------------------
    # DETERMINAR NIVEL
    # -------------------------------

    if promedio_global < 1.5:
        nivel = "Nivel 1 - Inicial"
    elif promedio_global < 2.5:
        nivel = "Nivel 2 - Básico"
    elif promedio_global < 3.5:
        nivel = "Nivel 3 - Definido"
    elif promedio_global < 4.5:
        nivel = "Nivel 4 - Gestionado"
    else:
        nivel = "Nivel 5 - Optimizado"

    st.success(f"Nivel de Madurez Organizacional: {nivel}")
    st.write(f"Promedio Global: {round(promedio_global, 2)}")

    st.divider()

    # -------------------------------
    # GRÁFICO RESUMEN
    # -------------------------------

    dimensiones = list(promedios.keys())
    valores = list(promedios.values())

    fig, ax = plt.subplots()
    ax.bar(dimensiones, valores)
    ax.set_ylim(0, 5)
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_title("Resultados por Dimensión")
    plt.xticks(rotation=45)

    st.pyplot(fig)
