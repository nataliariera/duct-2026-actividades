# analizador.py
import string

import matplotlib.pyplot as plt


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def main():
    try:
        with open("texto_integradora.txt", "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print("Error: el archivo texto_integradora.txt no existe.")
        return

    frecuencias = contar_frecuencias(texto)
    print(f"Cantidad de palabras totales: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")

    print("\nLas 10 palabras mas frecuentes:")
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")

    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title("Top 10 palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
