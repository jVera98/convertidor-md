# Script para convertir PDF del aula virtual a md.
Este es un script desarrollado con la única intención de ser educativo para mí y poder darle un uso mínimo.

## Comandos iniciales
El script corre en uv por lo tanto será importante tenerlo descargado e instalado. Por suerte al clonar el repo
podrás obtener el pyproject.toml con las depedencias necesarias para correrlo.

Para ello debes clonar el repo directamente en tu ordenador.

> [!IMPORTANT]
Si no tienes uv instalado en tu ordenador, ejecuta primero:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Comprueba versión con:
```bash
uv --version
```

```bash
git clone https://github.com/jVera98/convertidor-md
cd vuestra_carpeta
uv sync
```


Como el PDF son imágenes, hay que pasarlo por OCR. Para ello, instala en tu WSL: 

````bash
sudo apt install ocrmypdf tesseract-ocr-spa
````


## Flujo de trabajo
Lo primero de todo que debes de hacer es asegurarte de tener el pdf guardado en la ruta del proyecto.

> [!IMPORTANT]
Aseguraos de tener creada en la carpeta del proyecto una carpeta para guardar los temas.
```bash
mkdir -p temas
```
Os dejo un ejemplo de como pasar archivos de vuestro sistema windows a vuestro wsl.

```bash
cp /mnt/c/Users/TuUsuario/Downloads/temaX-Y.pdf ~/convertidor-md/temas/
```


Una vez copiado el procedimiento es sencillo, se pasa el PDF de imágenes por OCR para obtener un PDF con texto,

Para eso ejecutáis:
```bash
ocrmypdf -l spa temas/tema1-psp.pdf temas/tema1-psp-ocr.pdf
```

En mi flujo actual lo que hago es lo siguiente:

1º: Elimino el archivo pdf original.

```bash
rm temas/tema1-psp.pdf
```

2º Modifico el nombre del archivo ocr to pdf.

```bash
mv temas/tema1-psp-ocr.pdf temas/tema1-psp.pdf
```

Tras esto ya solo queda ejecutar nuestro script.

```bash
uv run script.py
```
Nos pedira introducir dos numeros, 0 cierra el programa, 1 para indicar la ruta, en este caso estamos en el mismo
directorio de trabajo asi que debe ser temas/archivo.pdf

