#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Grafica import Grafica
import random

class BarabasiAlbert(Grafica):
	"""Gráficas de redes de mundo pequeño. Modelo Barabási-Albert."""

	#Cantidad inicial de vértices
	__m0 = 5
		
	def __init__(self, n, m, m0 = BarabasiAlbert.__m0):
		"""Construye una gráfica de n vértices, con m0 vértices iniciales (n > m0) y m aristas por cada vértice nuevo agregado."""
		super(BarabasiAlbert, self).__init__(m0)
		self.__aristasAleatorias(m0)
		j = m0
		while j < n
			et = self.agregaVertice()
			i = 0
			while i < m:
				nodo = self.getVertice(random.randrange(j))
				r = random.ramdom()
				p = self.__probabilidad(nodo)
				if r < p:
					self.conecta(et, nodo.etiqueta)
					i += 1
			j += 1
				
	def __probabilidad(self,vertice):
		#Da la probabilidad de que un nodo se conecte con el nodo vertice.
		suma = 0.0
		for v in self.__vertices:
			suma += v.grado
		return vertice.grado / suma
		
	def __aristasAleatorias(self,m0):
		#Agrega aristas aleatorias entre los m0 vértices
		for i in range()

# Fin BarabasiAlbert.py
