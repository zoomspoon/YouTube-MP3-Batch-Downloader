# YouTube MP3 Batch Downloader 🎵

Este conjunto de scripts permite automatizar la búsqueda y descarga de canciones desde YouTube en formato MP3 (192kbps).

## 🚀 Instalación

1. Clona este repositorio o descarga los archivos.
2. Crea un entorno virtual y activa:
[Bash]
   python3 -m venv venv
   source venv/bin/activate  
   # En Windows: venv\Scripts\activate
3. Instala las dependencias:
[Bash]
pip install -r requirements.txt
Nota: Se requiere tener FFmpeg instalado en el sistema para la conversión a MP3.

## 🛠️ Cómo usar

• Opción A: No tengo los enlaces (Solo nombres)
Escribe los nombres de las canciones o artistas en lista_canciones.txt.

Obtén los enlaces automáticamente:

[Bash]
python get_youtube_links.py
Descarga la música:

[Bash]
python bajar_mp3_final.py


• Opción B: Ya tengo las URLs
Pega tus enlaces de YouTube en enlaces_youtube.txt (uno por línea).

Ejecuta el script de descarga:

[Bash]
python bajar_mp3_final_1.py

Nota: Se requiere tener FFmpeg instalado en el sistema para la conversión a MP3.

##📝 Scripts incluidos

• get_youtube_links.py: Busca en YouTube y genera un archivo de texto con URLs.

• script_bajar_mp3_final_solo_urls.py: Descarga masiva. Incluye historial (descargas_completadas.txt) para no bajar dos veces lo mismo si reinicias el proceso.

• bajar_mp3_final.py: Versión simple de descarga masiva sin historial.

## ⚖️ Aviso Legal / Disclaimer

Este proyecto ha sido creado exclusivamente con fines educativos y para uso personal. El desarrollador no se hace responsable del uso que los usuarios den a esta herramienta. Por favor, asegúrate de cumplir con los Términos de Servicio de YouTube y de respetar los derechos de autor de los contenidos que descargues.
