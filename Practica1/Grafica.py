#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Grafica(object):
	"""Clase Grafica para modelar Gráficas."""
	
	class __Nodo(object):
		#Clase interna Nodo.
		
		def __init__(self, n):
			#Constructor. El nodo se etiqueta con n.
			self.__etiqueta = n
		
		def __repr__(self):
			#Representación en cadena de un Nodo.
			return str(self.etiqueta)
		
		@property #Solo lectura
		def etiqueta(self):
			#Devuelve la etieuta del nodo.
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
		return self.__vertices
	
	@property
	def aristas(self):
		"""Regresa la lista de aristas de la gráfica."""
		return self.__aristas
		
	def agregaVertice(self):
		"""Agrega un nuevo vértice a la gráfica. Regresa la etiqueta del nuevo vértice."""
		self.__vertices.append(self.__Nodo(self.__sig))
		self.__sig += 1
		return self.__sig - 1
		
	def conecta(self, n, m):
		"""Agrega una arista del vértice n al m. Los vértices deben existir en la gráfica y no estar conectados"""
		if not str(n) in self.vertices or not str(m) in self.vertices:
			raise Exception("Exception.")
		if (n,m) in self.__aristas:
			raise Exception("Exception.")
		self.__aristas.append((n,m))
	
	def desconecta(self, n, m):
		"""Desconecta dos vértices en la gráfica. Los vértices deben existir en la gráfica y estar conectados"""
		if not str(n) in self.vertices or not str(m) in self.vertices:
			raise Exception("Exception.")
		if not (n,m) in self.__aristas:
			raise Exception("Exception.")
		self.__aristas.remove((n,m))

	def eliminar(self,n):
		"""Elimina el vértice con etiqueta n de la gráfica. El vértice debe existir en la gráfica."""
		if not str(n) in self.vertices:
			raise Exception("Exception.")
		for arista in self.__aristas:
			if arista[0] == n or arista[1] == n:
				self.__aristas.remove(arista)
		for vert in self.__vertices:
			if vert.etiqueta == n:
				self.__vertices.remove(vert)
	
#Fin Grafica.py
