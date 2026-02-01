# script_bajar_mp3_final_solo_urls.py

import yt_dlp
import os

def download_mp3_from_links(input_filename="enlaces_youtube.txt"):
    """
    Lee un archivo donde cada línea es una URL de YouTube y descarga el audio en formato MP3 en lote.
    """
    
    # 1. LECTURA Y VALIDACIÓN DEL ARCHIVO DE ENLACES
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{input_filename}' no fue encontrado. Asegúrate de tenerlo en el mismo directorio.")
        return

    # 2. PROCESAMIENTO DE ENLACES (Simplificado)
    all_urls = []
    
    # Recoge solo las líneas que parecen ser una URL válida
    for line in lines:
        if line.startswith(('http://', 'https://')):
            all_urls.append(line)

    if not all_urls:
        print("🛑 No se encontraron URLs válidas para descargar después de revisar el archivo.")
        print("Asegúrate de que cada línea en 'enlaces_youtube.txt' sea una URL completa que comience con 'http://' o 'https://'.")
        return

    # 3. CONFIGURACIÓN DE YTDLP
    ydl_opts = {
        # Formato de audio recomendado
        'format': 'bestaudio/best',
        
        # Opciones para FFmpeg: extraer y convertir a MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', # 192K es un buen estándar
        }],
        
        # Plantilla de salida: guarda los archivos en el mismo directorio usando el título del video.
        'outtmpl': os.path.join(os.path.dirname(input_filename) or '.', '%(title)s.%(ext)s'),
        
        'verbose': True,         # Muestra la información de debug
        'ignoreerrors': True,    # Importante: Continúa si una URL falla
        'quiet': False,          # Muestra el progreso normal
    }

    # 4. EJECUCIÓN DE LA DESCARGA EN LOTE
    print(f"🎵 Iniciando la descarga en lote de {len(all_urls)} canciones en formato MP3...")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ydl.download() procesa toda la lista de URLs
            result_code = ydl.download(all_urls)
            
            if result_code == 0:
                print("\n✅ ¡Descarga en lote completada exitosamente!")
            else:
                print("\n⚠️ Descarga completada con algunos errores. Revisa la salida anterior para ver qué URLs fallaron.")
                
    except Exception as e:
        print(f"\n❌ Ocurrió un error grave durante la ejecución de yt-dlp: {e}")

    print("\n¡Proceso finalizado!")


if __name__ == "__main__":
    download_mp3_from_links()