#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import polib
import mtranslate
import re

class PoTraductor:
	"""Clase para traducir archivos PO utilizando la biblioteca 'polib' y 'mtranslate'"""

	def __init__(self, archivo_origen, archivo_destino, mostrar_porcentaje=True, idioma_origen="es", idioma_destino="en"):
		"""
		Constructor de la clase PoTraductor.
		
		:param archivo_origen: El nombre del archivo de origen que se va a traducir.
		:param archivo_destino: El nombre del archivo de destino donde se guardará la traducción.
		:param mostrar_porcentaje: Indicador booleano que determina si se debe mostrar el progreso de la traducción en porcentaje (por defecto, True).
		:param idioma_origen: El idioma de origen del archivo PO (por defecto, "es" para español).
		:param idioma_destino: El idioma al que se va a traducir el archivo PO (por defecto, "en" para inglés).
		"""
		self.archivo_origen = archivo_origen
		self.archivo_destino = archivo_destino
		self.mostrar_porcentaje = mostrar_porcentaje
		self.idioma_origen = idioma_origen
		self.idioma_destino = idioma_destino

	def traducir_y_preservar_saltos_de_linea(self, texto, idioma_destino, idioma_origen):
		"""
		Traduce una cadena de texto a un idioma destino y preserva los saltos de línea y variables.
		
		:param texto: La cadena de texto que se va a traducir.
		:param idioma_destino: El idioma al que se va a traducir la cadena de texto.
		:param idioma_origen: El idioma de origen de la cadena de texto.
		:return: La cadena de texto traducida con los saltos de línea y variables preservados.
		"""
		lineas = texto.split('\n')
		lineas_traducidas = [mtranslate.translate(linea, idioma_destino, idioma_origen) for linea in lineas]
		return '\n'.join(lineas_traducidas)

	def traducir(self):
		"""
		Traduce el archivo PO de idioma origen a idioma destino y lo guarda en un archivo PO de destino.
		"""
		# Carga el archivo PO
		archivo_po = polib.pofile(self.archivo_origen)

		# Inicializa el recuento de traducciones
		entradas_totales = len(archivo_po)
		entradas_traducidas = 0

		# Calcula el número de cadenas ya traducidas
		entradas_previamente_traducidas = 0
		for entrada in archivo_po:
			if entrada.translated():
				entradas_previamente_traducidas += 1

		# Expresión regular para buscar y mantener variables en las cadenas de texto
		patron = re.compile(r'{[^}]*}')

		# Calcula el número total de entradas no traducidas
		entradas_no_traducidas_totales = entradas_totales - entradas_previamente_traducidas

		# Itera sobre las entradas y traduce las cadenas no traducidas
		for entrada in archivo_po:
			if not entrada.translated():
				# Traduce la cadena utilizando Google Translate y preservando saltos de línea
				traduccion = self.traducir_y_preservar_saltos_de_linea(entrada.msgid, self.idioma_destino, self.idioma_origen)
				# Reemplaza las variables en la cadena traducida con las mismas variables que la original
				traduccion_formateada = patron.sub(lambda coincidencia: coincidencia.group(), traduccion)
				# Asigna la cadena traducida a la entrada
				entrada.msgstr = traduccion_formateada

				# Incrementa el recuento de traducciones
				entradas_traducidas += 1

				if self.mostrar_porcentaje:
					# Calcula y muestra el porcentaje de traducción completado
					porcentaje_completado = (entradas_traducidas / entradas_no_traducidas_totales) * 100
					print(f'Progreso de traducción: {porcentaje_completado:.2f}%', end='\r', flush=True)

		# Guarda el archivo PO actualizado
		archivo_po.save(self.archivo_destino)

		if self.mostrar_porcentaje:
			# Imprime un mensaje de finalización y pasa a la siguiente línea
			print(f'\nTraducción completada. {entradas_traducidas} entradas traducidas.')
