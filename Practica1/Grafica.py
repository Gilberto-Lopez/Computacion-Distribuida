#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Grafica(object):
	"""Clase Grafica para modelar Gráficas."""
	
	class __Nodo(object):
		"""Clase interna Nodo."""
	
		def __init__(self, n):
			"""Constructor. El nodo se etiqueta con n."""
			self.__etiqueta = n
			
		@property #Solo lectura
		def etiqueta(self):
			"""Devuelve la etieuta del nodo."""
			return self.__etiqueta
	
	def __init__(self, n):
		"""Constructor, recibe un entero n y añade n vertices a la gráfica, etiquetados de 0 a n-1."""
		self.__sig = n
		self.__vertices = []
		for i in range(n):
			self.__vertices.append(self.__Nodo(i))
		self.__aristas = []
	
	@property
	def vertices(self):
		"""Regresa la lista de vértices (etiquetas) de la gráfica."""
		vert = []
		for nodo in self.__vertices:
			vert.append(nodo.etiqueta)
		return vert
	
	@property
	def aristas(self):
		"""Regresa la lista de aristas de la gráfica."""
		return self.__aristas
		
	def agregaVertice():
		"""Agrega un nuevo vértice a la gráfica. Regresa la etiqueta del nuevo vértice."""
		self.vertices.append(self.__Nodo(self.__sig))
		self.__sig += 1
		return self.__sig - 1
		
	def conecta(n,m):
		pass

#Fin Grafica.py
