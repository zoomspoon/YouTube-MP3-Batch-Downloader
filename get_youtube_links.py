import yt_dlp

def get_youtube_links_from_file(input_filename="lista_canciones.txt", output_filename="enlaces_youtube.txt"):
    """
    Lee un archivo de texto con canciones, busca sus enlaces en YouTube y los guarda en un archivo.
    Cada línea del archivo de entrada debe tener el formato "artista - cancion".
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            songs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{input_filename}' no fue encontrado. Asegúrate de que existe en la misma carpeta.")
        return

    failed_searches = []
    
    # Opciones de yt-dlp para una búsqueda simple
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    print(f"Buscando enlaces para {len(songs)} canciones...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for song in songs:
                try:
                    # Realizar una búsqueda con 'ytsearch1' para obtener el primer resultado
                    info = ydl.extract_info(f"ytsearch1:{song}", download=False)
                    
                    # Extraer la URL del resultado
                    if info and info['entries']:
                        video_url = info['entries'][0]['url']
                        line_to_write = f'{song}: {video_url}\n'
                        output_file.write(line_to_write)
                        print(f'Encontrado para "{song}"')
                    else:
                        failed_searches.append(song)
                except yt_dlp.utils.DownloadError:
                    failed_searches.append(song)
                except Exception as e:
                    print(f"Ocurrió un error al procesar la canción '{song}': {e}")
                    failed_searches.append(song)

    print(f"\nProceso completado. Los enlaces se han guardado en '{output_filename}'.")
    if failed_searches:
        print("\nNo se encontraron enlaces para las siguientes canciones:")
        for song in failed_searches:
            print(f"- {song}")

if __name__ == "__main__":
    get_youtube_links_from_file()
