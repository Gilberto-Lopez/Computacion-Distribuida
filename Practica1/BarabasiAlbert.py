#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Grafica import Grafica
import random

class BarabasiAlbert(Grafica):
	"""Gráficas de redes de mundo pequeño. Modelo Barabási-Albert."""

	#Cantidad inicial de vértices
	__m0 = 5
		
	def __init__(self, n, m, m0 = __m0):
		"""Construye una gráfica de n vértices, con m0 vértices iniciales (n > m0) y m aristas por cada vértice nuevo agregado."""
		super(BarabasiAlbert, self).__init__(max(m0, self.__m0))
		self.__aristasAleatorias()
		j = m0
		while j < n:
			et = self.agregaVertice()
			i = 0
			while i < m:
				nodo = self.getVertice(random.randrange(j))
				if nodo in et.vecinos:
					continue
				r = random.random()
				p = self.__probabilidad(nodo)
				if r < p:
					self.conecta(et, nodo)
					i += 1
			j += 1
				
	def __probabilidad(self, vertice):
		#Da la probabilidad de que un nodo se conecte con el nodo vertice.
		suma = 0.0
		for v in self.vertices:
			suma += v.grado
		return vertice.grado / suma
		
	def __aristasAleatorias(self):
		#Agrega aristas aleatorias entre los m0 vértices
		for i in self.vertices:
			for j in self.vertices:
				if i != j:
					if i in j.vecinos:
						continue
					if random.random() > 0.5:
						self.conecta(i, j)

# Fin BarabasiAlbert.py
