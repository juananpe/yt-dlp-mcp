import yt_dlp

def descargar_video(url):
    # Opciones de descarga: en este caso se descargará la mejor calidad disponible y
    # se guardará con el nombre del título del vídeo.
    opciones = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        # Puedes agregar más opciones si lo deseas, por ejemplo para descargar solo audio:
        # 'format': 'bestaudio/best',
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        # }],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Descarga completada.")
    except Exception as error:
        print(f"Ocurrió un error durante la descarga: {error}")

if __name__ == '__main__':
    video_url = input("Introduce la URL del vídeo de YouTube: ")
    descargar_video(video_url)