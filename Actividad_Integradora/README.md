# Analizador de frecuencia de palabras

`analizador.py` lee el archivo `texto_integradora.txt`, cuenta cuántas veces aparece cada palabra con un diccionario y muestra las 10 más frecuentes. También, genera y guarda un gráfico de barras con ese top 10 en `grafico_frecuencias.png`.

Si el archivo de texto no existe, el script muestra un mensaje de error en lugar de fallar.

**Bibliotecas necesarias:** `matplotlib` (para el gráfico) y `pytest` (para las pruebas). Instalación: `pip install -r requirements.txt`

**Ejecución:** `python analizador.py`

**Pruebas:** `pytest -v test_analizador.py`
