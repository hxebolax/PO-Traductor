# PoTraductor

PoTraductor es una herramienta de traducción para archivos PO que utiliza la biblioteca polib y mtranslate. Este script traduce automáticamente las entradas de un archivo PO de un idioma origen a un idioma destino, preservando saltos de línea y variables.

Las traducciones se hacen con Google Translate y no es necesario clave API.

Se recomienda una vez generada una traducción el ser revisada ya que hay cosas que no consigue guardar como (&) para teclas modificadoras.

Cualquier contribución para mejorar el resultado de las traducciones y que cada vez sea menos necesario revisarlas se agradecen.

## Instalación

Para instalar las dependencias necesarias, ejecute el siguiente comando:

pip install -r requirements.txt

## Uso

from po_traductor import PoTraductor

\# Crear una instancia de PoTraductor

traductor = PoTraductor("archivo__origen.po", "archivo__destino.po", mostrar_porcentaje=True, idioma_origen="es", idioma_destino="en")

\# Iniciar la traducción

traductor.traducir()

### Parámetros

- archivo__origen: El nombre del archivo de origen que se va a traducir.
- archivo__destino: El nombre del archivo de destino donde se guardará la traducción.
- mostrar_porcentaje: Indicador booleano que determina si se debe mostrar el progreso de la traducción en porcentaje (por defecto, True).
- idioma_origen: El idioma de origen del archivo PO (por defecto, "es" para español), también podemos poner "auto" para que detecte automáticamente el idioma origen.
- idioma_destino: El idioma al que se va a traducir el archivo PO (por defecto, "en" para inglés).

## Información técnica

PoTraductor utiliza la biblioteca polib para leer y escribir archivos PO. La biblioteca mtranslate es utilizada para realizar las traducciones de las cadenas de texto. Además, se utiliza la biblioteca re para buscar y mantener variables en las cadenas de texto.

Probado en Python 3.7 / 3.11.

## Ejemplo

from po_traductor import PoTraductor

\# Crear una instancia de PoTraductor para traducir un archivo PO del español al italiano

traductor = PoTraductor("it_origen.po", "it_destino.po", mostrar_porcentaje=True, idioma_origen="es", idioma_destino="it")

\# Iniciar la traducción

traductor.traducir()

Este ejemplo cargará el archivo es.po en español, lo traducirá al italiano y guardará el resultado en el archivo it.po. Durante el proceso, se mostrará el progreso de la traducción en porcentaje.

## Licencia

Este programa se distribuye bajo la licencia GNU GENERAL PUBLIC LICENSE Version 2.
