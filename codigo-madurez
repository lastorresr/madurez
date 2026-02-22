# -----------------------------

dimensiones = {
    "Alineación Estratégica": 5,
    "Cultura y Liderazgo": 5,
    "Personas": 5,
    "Gobernabilidad": 5,
    "Procesos y TI": 5
}

preguntas = []
for dim in dimensiones:
    for i in range(dimensiones[dim]):
        preguntas.append(f"{dim} - Ítem {i+1}")

escala = ["1", "2", "3", "4", "5"]

# -----------------------------
# FUNCIÓN DE CÁLCULO
# -----------------------------

def calcular():
    try:
        valores = [int(combo.get()) for combo in combos]

        # Calcular promedio por dimensión
        promedios = []
        index = 0
        for dim in dimensiones:
            suma = sum(valores[index:index+5])
            promedios.append(suma / 5)
            index += 5

        igm = sum(promedios) / len(promedios)

        # Determinar fase
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

        resultado_label.config(
            text=f"Índice Global de Madurez (IGM): {igm:.2f}\nNivel: {fase}"
        )

        # -----------------------------
        # GRÁFICO RADAR
        # -----------------------------
        etiquetas = list(dimensiones.keys())
        valores_radar = promedios + [promedios[0]]

        angulos = np.linspace(0, 2 * np.pi, len(etiquetas), endpoint=False).tolist()
        angulos += angulos[:1]

        plt.figure()
        ax = plt.subplot(111, polar=True)
        ax.plot(angulos, valores_radar)
        ax.fill(angulos, valores_radar, alpha=0.25)

        ax.set_xticks(angulos[:-1])
        ax.set_xticklabels(etiquetas)
        ax.set_ylim(0, 5)

        plt.title("Resumen de Madurez por Dimensión")
        plt.show()

    except:
        messagebox.showwarning("Error", "Debe responder todas las preguntas.")

# -----------------------------
# INTERFAZ
# -----------------------------

root = tk.Tk()
root.title("Evaluador de Madurez Organizacional")
root.geometry("900x750")

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = ttk.Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

titulo = ttk.Label(frame, text="Modelo de Evaluación de Madurez Organizacional",
                   font=("Arial", 16, "bold"))
titulo.pack(pady=15)

combos = []

for pregunta in preguntas:
    fila = ttk.Frame(frame)
    fila.pack(fill="x", padx=20, pady=5)

    label = ttk.Label(fila, text=pregunta)
    label.pack(side="left")

    combo = ttk.Combobox(fila, values=escala, width=5)
    combo.pack(side="right")
    combos.append(combo)

boton = ttk.Button(frame, text="Calcular Nivel de Madurez", command=calcular)
boton.pack(pady=20)

resultado_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=20)

root.mainloop()

# ============================================================
# FIN
# ============================================================
