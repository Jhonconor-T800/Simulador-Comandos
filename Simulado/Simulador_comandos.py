import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Diccionarios de ayuda
# -----------------------------

# Diccionario de efectos con emojis y descripciones
EfectosInfo = {
    "speed": ("💨", "Aumenta la velocidad del jugador."),
    "slowness": ("🐢", "Reduce la velocidad del jugador."),
    "haste": ("⛏️", "Aumenta la velocidad de minado."),
    "mining_fatigue": ("😩", "Disminuye la velocidad de minado."),
    "strength": ("💪", "Incrementa el daño de ataque."),
    "instant_health": ("❤️", "Restaura vida instantáneamente."),
    "instant_damage": ("💥", "Hace daño instantáneo."),
    "jump_boost": ("🦘", "Permite saltar más alto."),
    "nausea": ("🤢", "Deforma la pantalla causando mareo."),
    "regeneration": ("♻️", "Recupera vida progresivamente."),
    "resistance": ("🛡️", "Reduce el daño recibido."),
    "fire_resistance": ("🔥", "Inmunidad al fuego y lava."),
    "water_breathing": ("🐠", "Permite respirar bajo el agua."),
    "invisibility": ("👻", "Vuelve invisible al jugador."),
    "blindness": ("🙈", "Reduce la visión del jugador."),
    "night_vision": ("🌙", "Mejora la visión en la oscuridad."),
    "hunger": ("🍖", "Aumenta el hambre del jugador."),
    "weakness": ("🥀", "Reduce el daño de ataque."),
    "poison": ("☠️", "Daña poco a poco hasta medio corazón."),
    "wither": ("💀", "Daña progresivamente hasta la muerte."),
    "health_boost": ("💖", "Aumenta la vida máxima."),
    "absorption": ("🫀", "Añade corazones adicionales."),
    "saturation": ("🍎", "Rellena la barra de hambre."),
    "glowing": ("✨", "Hace que el jugador brille."),
    "levitation": ("🎈", "Hace flotar al jugador hacia arriba."),
    "luck": ("🍀", "Aumenta la suerte en botín."),
    "unluck": ("😵", "Reduce la probabilidad de buen botín."),
    "slow_falling": ("🪶", "Hace caer lentamente."),
    "conduit_power": ("🌊", "Poder del canal: visión y fuerza bajo agua."),
    "dolphins_grace": ("🐬", "Nadar más rápido con delfines."),
    "bad_omen": ("⚠️", "Provoca incursiones al entrar en aldeas."),
    "hero_of_the_village": ("🏆", "Beneficios en aldeas tras una incursión.")
}

# Diccionario de descripciones para otros comandos
Descripciones = {
    "/gamemode survival": "Cambia el modo de juego a supervivencia.",
    "/gamemode creativo": "Cambia el modo de juego a creativo.",
    "/gamemode espectador": "Cambia el modo de juego a espectador.",
    "/time set afternoon": "Establece el tiempo a la tarde.",
    "/time set night": "Establece el tiempo a la noche.",
    "/time set day": "Establece el tiempo a la mañana.",
    "/particle flame": "Genera partículas de fuego.",
    "/particle heart": "Genera partículas de corazones.",
    "/particle smoke": "Genera partículas de humo."
}

# -----------------------------
# Listas de comandos
# -----------------------------
Comandos1 = list(filter(lambda k: k.startswith("/gamemode"), Descripciones.keys()))
Comandos2 = list(filter(lambda k: k.startswith("/time"), Descripciones.keys()))
Comandos4 = list(filter(lambda k: k.startswith("/particle"), Descripciones.keys()))
EfectosPocion = list(EfectosInfo.keys())
Comandos3 = [f"/effect @p {efecto}" for efecto in EfectosPocion]
Comandos = ["/gamemode", "/effect", "/time", "/particle"]

# -----------------------------
# Función para ejecutar comandos
# -----------------------------
def ejecutar_comando():
    comando = entrada_comando.get().strip()
    salida_texto.config(state="normal")

    if comando in Comandos1 or comando in Comandos2 or comando in Comandos3 or comando in Comandos4:
        if comando.startswith("/effect"):
            efecto = comando.split()[-1]  # último texto es el efecto
            emoji, descripcion = EfectosInfo.get(efecto, ("", "Sin descripción."))
            salida_texto.insert("end", f"Comando establecido: {comando} {emoji}\n")
            salida_texto.insert("end", f"Descripción: {descripcion}\n\n")
        else:
            descripcion = Descripciones.get(comando, "Sin descripción.")
            salida_texto.insert("end", f"Comando establecido: {comando}\n")
            salida_texto.insert("end", f"Descripción: {descripcion}\n\n")

    elif comando.lower() == "/help":
        salida_texto.insert("end", "Ayuda: Escribe un comando válido de la lista.\n\n")
    else:
        messagebox.showerror("Error", "Comando no reconocido.")

    salida_texto.config(state="disabled")

# -----------------------------
# Interfaz gráfica Tkinter
# -----------------------------
ventana = tk.Tk()
ventana.title("Emulador de Bloque de Comandos Minecraft")
ventana.geometry("500x450")
ventana.configure(bg="#696969")

# Cargar icono personalizado
ventana.iconbitmap("command_block")


tk.Label(ventana, text="Emulador de Comandos", font=("Arial", 14), bg="#696969", fg="white").pack(pady=10)
entrada_comando = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_comando.pack(pady=5)

boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_comando, bg="#4CAF50", fg="white")
boton_ejecutar.pack(pady=5)

salida_texto = tk.Text(ventana, height=12, width=55, state="disabled", bg="#333333", fg="white")
salida_texto.pack(pady=10)

sugerencias = tk.Listbox(ventana, height=4, width=40, bg="#333333", fg="white")

def actualizar_sugerencias(event):
    sugerencias.delete(0, tk.END)
    texto = entrada_comando.get().strip().lower()
    for comando in Comandos + Comandos1 + Comandos2 + Comandos3 + Comandos4:
        if texto in comando.lower():
            sugerencias.insert(tk.END, comando)

def autocompletar_sugerencia(event):
    seleccion = sugerencias.get(sugerencias.curselection())
    entrada_comando.delete(0, tk.END)
    entrada_comando.insert(tk.END, seleccion)
    sugerencias.place_forget()

entrada_comando.bind("<KeyRelease>", actualizar_sugerencias)
sugerencias.bind("<<ListboxSelect>>", autocompletar_sugerencia)

def mostrar_sugerencias(event):
    if sugerencias.size() > 0:
        sugerencias.place(x=entrada_comando.winfo_x(), y=entrada_comando.winfo_y() + 25)

entrada_comando.bind("<KeyRelease>", mostrar_sugerencias)

ventana.mainloop()
