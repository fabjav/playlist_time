from pytube import Playlist

def obtener_tiempo_total_playlist(url):
    try:
        playlist = Playlist(url)
        tiempo_total = 0

        for video in playlist.videos:
            tiempo = int(video.length)
            tiempo_total += tiempo

        segundos_totales = tiempo_total
        horas, segundos = divmod(segundos_totales, 3600)
        minutos, segundos = divmod(segundos, 60)

        print(f"Tiempo total de la playlist: {horas} horas, {minutos} minutos, {segundos} segundos")

        return tiempo_total
    except Exception as e:
        print(f"Error al obtener la lista de reproducción: {e}")
        return None

if __name__ == "__main__":
    url = input("Ingresa la URL de la lista de reproducción de YouTube: ")
    tiempo_total = obtener_tiempo_total_playlist(url)

    if tiempo_total is not None:
        opcion = input("¿Deseas dividir el tiempo en jornadas? (Sí/No): ")
        if opcion.lower() == 'si':
            horas_por_jornada = int(input("Ingresa la cantidad de horas por jornada: "))
            horas, segundos = divmod(tiempo_total, 3600)
            minutos, segundos = divmod(segundos, 60)
            jornadas = horas // horas_por_jornada
            horas_restantes = horas % horas_por_jornada
            print(f"El tiempo total se divide en {jornadas} jornadas de {horas_por_jornada} horas y {horas_restantes} horas restantes.")
