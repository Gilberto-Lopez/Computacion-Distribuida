#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Grafica import Grafica
import random

class ErdosRenyi(Grafica):
	"""Gráficas aleatorias. Modelo Erdős-Rényi."""
	
	def __init__(self, n, p):
		super(ErdosRenyi, self).__init__(n)
		#Agrega aristas aleatorias entre los n vértices
		for vi in self.vertices:
			for vj in self.vertices:
				if vi == vj or vi in vj.vecinos:
					continue
				r = random.random()
				if r < p:
					self.conecta(vi, vj)

# Fin ErdosRenyi.py
