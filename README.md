# Chrome Tab Saver

Un script para capturar todas las pestañas abiertas de Google Chrome y guardarlas en un archivo Markdown con títulos, URLs y resúmenes generados llamando a la API de OpenAI.

## Funcionalidades

- Captura sesiones de pestañas en vivo de Chrome (macOS via AppleScript, Linux/Windows via DevTools Protocol).
- Excluye dominios especificados (por ejemplo, Gmail, Google Calendar).
- Genera resúmenes concisos de 2–3 líneas llamando a la API de OpenAI.
- Genera archivos Markdown con timestamp en el nombre.
- Código en Python modular, extensible y testeable.
