import tkinter as tk
from pytube import Playlist

# Variable para almacenar el tiempo total de la playlist
tiempo_total = 0

def obtener_tiempo_total_playlist(url):
    try:
        playlist = Playlist(url)

        # Calcular el tiempo total de la playlist si no se ha calculado previamente
        global tiempo_total
        if tiempo_total == 0:
            tiempo_total = sum(int(video.length) for video in playlist.videos)

        tiempo_total_h = tiempo_total // 3600
        tiempo_total_m = (tiempo_total % 3600) // 60
        tiempo_total_s = tiempo_total % 60

        return tiempo_total_h, tiempo_total_m, tiempo_total_s

    except Exception as e:
        return None

def procesar_lista_reproduccion():
    divisor = int(divisor_spinbox.get())
    result = obtener_tiempo_total_playlist(url_entry.get())

    if result is not None:
        horas, minutos, segundos = result
        resultado_label.config(text=f"Tiempo total: {horas:02d}:{minutos:02d}:{segundos:02d}")

        horas_divididas = horas // divisor
        minutos_divididos = (minutos + horas % divisor * 60) // divisor

        resultado_dias_label.config(text=f"Duración en días: {horas_divididas} días, {minutos_divididos} minutos")

# Crear ventana
window = tk.Tk()
window.title("Calculadora de Tiempo de YouTube Playlist")

# Interfaz
url_label = tk.Label(window, text="Ingresa el enlace de la lista de reproducción:")
url_label.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

divisor_label = tk.Label(window, text="Divisor de jornadas:")
divisor_label.pack()

divisor_spinbox = tk.Spinbox(window, from_=1, to=100)
divisor_spinbox.pack()

procesar_button = tk.Button(window, text="Procesar Playlist", command=procesar_lista_reproduccion)
procesar_button.pack()

mensaje_label = tk.Label(window, text="")
mensaje_label.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

resultado_dias_label = tk.Label(window, text="")
resultado_dias_label.pack()

# Inicio
window.mainloop()
