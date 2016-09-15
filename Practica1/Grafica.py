# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Grafica(object):
	"""Clase Grafica para modelar Gráficas no dirigidas."""
	
	class __Nodo(object):
		#Clase interna Nodo.
		
		def __init__(self, n):
			#Constructor. El nodo se etiqueta con n.
			self.__etiqueta = n
			self.__vecinos = []
		
		def __repr__(self):
			#Representación en cadena de un Nodo.
			return str(self.etiqueta)
		
		@property #Solo lectura
		def etiqueta(self):
			#Devuelve la etieuta del nodo.
			return self.__etiqueta
		
		@property
		def vecinos(self):
			#Devuelve la lista de vecinos
			return self.__vecinos
			
		@property
		def grado(self):
			#Devuelve el grado del nodo
			return len(self.__vecinos)

		def agregaVecino(self, vecino):
			#Agrega un vecino
			self.__vecinos.append(vecino)
			
		def eliminaVecino(self, vecino):
			#Elimina un vecino
			self.__vecinos.remove(vecino)

		@property
		def coeficienteAoplamiento(self):
			#Regresa el coeficiente de acoplamiento local de un vertice
			k = len(self.vecinos)*(len(self.vecinos) - 1)
			li = 0.0
			for vecino in self.vecinos:
				for vecino2 in self.vecinos:
					if vecino2 in vecino.vecinos:
						li += 1.0
			return li / k
	
	def __init__(self, n):
		"""Constructor, recibe un entero n y añade n vertices a la gráfica, etiquetados de 0 a n-1."""
		self.__sig = n
		self.__vertices = []
		for i in range(n):
			self.__vertices.append(self.__Nodo(i))
	
	@property
	def vertices(self):
		"""Regresa la lista de vértices (etiquetas) de la gráfica."""
		return self.__vertices
			
	def agregaVertice(self):
		"""Agrega un nuevo vértice a la gráfica. Regresa el nuevo vértice."""
		nuevo = self.__Nodo(self.__sig)
		self.__vertices.append(nuevo)
		self.__sig += 1
		return nuevo
		
	def conecta(self, n, m):
		"""Agrega una arista del vértice n al m. Los vértices deben existir en la gráfica y no estar conectados."""
		if n in m.vecinos:
			raise Exception("Los nodos ya están conectados.")
		n.agregaVecino(m)
		m.agregaVecino(n)
	
	def desconecta(self, n, m):
		"""Desconecta los vértice n y m. Los vértices deben existir en la gráfica y estar conectados."""
		if not n in m.vecinos:
			raise Exception("Los vértices no están conectados.")
		n.eliminaVecino(m)
		m.eliminaVecino(n)
	
	def eliminaVertice(self,n):
		"""Elimina el vértice con etiqueta n de la gráfica. El vértice debe existir en la gráfica."""
		for vecino in n.vecinos:
			vecino.eliminaVecino(n)
		self.__vertices.remove(n)
	
	def getVertice(self,n):
		"""Regresa el vertice con la etiqueta n. Si el vértice no existe se lanza una excepción."""
		vn = None
		for vertice in self.__vertices:
			if vertice.etiqueta == n:
				vn = vertice
				break
		if vn == None:
			raise Exception("El vértice no existe.")
		return vn
	
	def distribucionGrados(self):
		"""Regresa un diccionario con la distribución de grados de la gráfica."""
		dist = dict.fromkeys(range(len(self.__vertices) - 1),0)
		g = 1.0 / len(self.__vertices)
		for vertice in self.__vertices:
			dist[vertice.grado] += g
		return dist
		
	def listaAdyacencias(self):
		"""Regresa la lista de adyacencias de la gráfica. Una lista de tuplas (i,j) donde i y j están conectados"""
		l = []
		for vertice in self.__vertices:
			for vecino in vertice.vecinos:
				l.append((vertice.etiqueta,vecino.etiqueta))
		return l
		
	def coeficienteAcoplamiento(self):
		"""Regresa el coeficiente de acoplamiento promedio de la red."""
		suma = 0.0
		for vertice in self.__vertices:
			suma = suma + vertice.coeficienteAcoplamiento
		return suma / len(self.__vertices)

#Fin Grafica.py
