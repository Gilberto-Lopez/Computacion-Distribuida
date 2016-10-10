#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BarabasiAlbert import BarabasiAlbert
import random

class SIR(BarabasiAlbert):
	"""
	Clase SIR para modelar el modelo epidémico SIR.
	"""
	
	#Tiempo que puede estar un agente en estado recuperado.
	__tiempo_recuperado = 10
	#TIempo que pude estar un agente en estado infeccioso.
	__tiempo_infeccioso = 5
	#Cantidad inicial de agentes infectados.
	__infectados_iniciales = 4
	
	class __Agente(object):
		#Clase interna para modelar los agentes del modelo SIR.
		#Estados:
		#0 - Susceptible.
		#1 - Infeccioso.
		#2 - Recuperado.
		
		def __init__(self, resistencia, interaccion, estado = 0):
			#Constructor:
			#resistencia - La resistencia del agente a la infección. 0 nula, 1 inmune.
			#interaccion - La probabilidad de interaccion del agente con sus vecinos.
			#estado - El estado inicial del agente. El estado por omisión es Susceptible.
			self.theta = resistencia
			self.p = interaccion
			self.e = estado
			self.s = 0 #Siguiente estado.
			self.t = 0 #Tiempo en el estado actual.
			
	def __init__(self,agentes = 100, infectados = __infectados_iniciales):
		"""
		El modelo se inicializa con una cierta cantidad de agentes,
		de los cuales cierta cantidad están infectados.
		"""
		a = max(agentes,100)
		super(SIR, self).__init__(a, a/100)
		self.__infectados = max(infectados, __infectados_iniciales)
		self.__recuperados = 0
		self.__susceptibles = a - self.__infectados
		for v in self.vertices:
			v.setElemento(self.__Agente(random.random(),random.random()))
		#vertices infectados
		i = 0
		while i < self.__infectados:
			r = random.randint(0,self.__infectados - 1)
			nodo = self.getVertice(r)
			if nodo.e == 0:
				nodo.e = 1

	def actualiza(self):
		"""
		Actuliza los estados de los agentes de la red un una unidad de tiempo.
		Regresa una tupla (s,i,r) donde:
		s : El número de agentes susceptibles.
		i : El número de agentes infecciosos.
		r : El número de agentes recuperados.
		"""
		for v in self.vertices:
			#Actulizamos estados.
			v.elemento.e = v.elemento.s
		for v in self.vertices:
			elem = v.elemento
			if elem.e == 1: #Estado infeccioso.
				for vecino in v.vecinos:
					velem = vecino.elemento
					r = random.random()
					if r < elem.p: #Interactúa con el vecino.
						g = random.random()
						if velem.e == 0 and g < velem.theta: #Infecta al vecino.
							velem.s = 1
							velem.t = 0
				elem.t += 1
				if elem.t > __tiempo_infeccioso: #Pasa a recuperado.
					elem.s = 2
			elif elem.e == 2: #Estado recuperado.
				elem.t += 1
				if elem.t > __tiempo_recuperado: #Pasa a ser susceptible.
					elem.s = 0
			else: #Estado susceptible.
				#Pasivo.
				continue
		sus = 0
		inf = 0
		rec = 0
		for v in self.vertices:
			elem = v.elemento
			if elem.s == 0:
				sus += 1
			elif elem.s == 1:
				inf += 1
			else:
				rec += 1
		return (sus, inf, rec)

# Fin SIR.py
