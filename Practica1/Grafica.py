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
			
		def agregaVecino(self, vecino):
			#Agrega un vecinos
			self.__vecinos.append(vecino)
			
		def eliminaVecino(self, vecino):
			#Elimina un vecinos
			self.__vecinos.remove(vecino)
	
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
		"""Agrega un nuevo vértice a la gráfica. Regresa la etiqueta del nuevo vértice."""
		self.__vertices.append(self.__Nodo(self.__sig))
		self.__sig += 1
		return self.__sig - 1
		
	def conecta(self, n, m):
		"""Agrega una arista del vértice n al m. Los vértices deben existir en la gráfica y no estar conectados."""
		vn = self.getVertice(n)
		vm = self.getVertice(m)
		if vn in vm.vecinos:
			raise Exception("Los nodos ya están conectados.")
		vn.agregaVecino(vm)
		vm.agregaVecino(vn)
	
	def desconecta(self, n, m):
		"""Desconecta los vértice n y m. Los vértices deben existir en la gráfica y estar conectados."""
		vn = self.getVertice(n)
		vm = self.getVertice(m)
		if not vn in vm.vecinos:
			raise Exception("Los vértices no están conectados.")
		vn.eliminaVecino(vm)
		vm.eliminaVecino(vn)
	
	def eliminaVertice(self,n):
		"""Elimina el vértice con etiqueta n de la gráfica. El vértice debe existir en la gráfica."""
		vn = self.getVertice(n)
		for vecino in vn.vecinos:
			vecino.eliminaVecino(vn)
		self.__vertices.remove(vn)
	
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
		
#Fin Grafica.py
