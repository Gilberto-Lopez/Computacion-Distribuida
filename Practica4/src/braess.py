#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Para argumentos en la línea de comandos.
import sys
from random import randint

class RedTrafico(object):
	"""
	Clase para modelar una red de tráfico. Las redes tienen rutas,
	las cuales tienen pesos y una cierta cantidad de conductores
	viajando por ellas.
	"""

	class Conductor(object):
		"""
		Clase para modelar conductores. Cada conductor sabe la
		ruta por la que viaja en la red de tráfico.
		"""

		def __init__(self, ruta):
			"""
			Construye un nuevo conductor para la red de tráfico.
			"""
			#Ruta actual. Debe ser inicializada a una ruta
			#válida.
			self.r = ruta

		def cambia_ruta(self, nueva):
			"""
			Cambia la ruta del conductor a la ruta "nueva".
			"""
			self.r = nueva

		@property
		def ruta(self):
			"""
			Nos da la ruta en que viaja actualmente el conductor.
			"""
			return self.r

	def encuentra_equilibrio(self):
		"""
		Encuentra el equilibrio de Nash en la red de tráfico.
		"""
		equilibrio = False
		rs = len(self.rutas)
		while not equilibrio:
			#Si ya no cambia en alguna iteración del while
			#hemos encontrado el equilibrio.
			equilibrio = True
			for conductor in self.conductores:
				for i in range(rs):
					cr = conductor.ruta
					#Costo de viajar en la ruta i.
					nuevo_costo = self.costos[i]()
					#Costo de seguir viajando en la misma ruta.
					viejo_costo = self.costos[cr]()
					if nuevo_costo < viejo_costo:
						#Es mejor cambiar de ruta.
						self.rutas[cr] -= 1
						self.rutas[i] += 1
						conductor.cambia_ruta(i)
						#Como cambiamos de ruta no estamos en
						#equilibrio.
						equilibrio = False

class RedUno(RedTrafico):
	"""
	Primera red de tráfico: RedUno.png
	"""

	def __init__(self, autos):
		"""
		Crea la primera Red vista en clase, con los
		mismos pesos en las aristas.
		"""
		self.conductores = []
		self.rutas = [0, 0]
		for i in range(autos):
			#Creamos un conductor y lo asignamos aleatoriamente
			#a una ruta.
			r = randint(0,1) #{0,1}
			c = RedTrafico.Conductor(r)
			self.conductores.append(c)
			self.rutas[r] += 1
		self.costos = [lambda : self.rutas[0]/100.0 + 45,
			lambda : 45 + self.rutas[1]/100.0]

class RedBraess(RedTrafico):
	"""
	Segunda red de tráfico: RedBraess.png
	Paradoja de Braess.
	"""

	def __init__(self, autos):
		"""
		Crea la Red Braess vista en clase, con los
		mismos pesos en las aristas.
		"""
		self.conductores = []
		self.rutas = [0, 0, 0]
		for i in range(autos):
			#Creamos un conductor y lo asignamos aleatoriamente
			#a una ruta.
			r = randint(0,2) #{0,1,2}
			c = RedTrafico.Conductor(r)
			self.conductores.append(c)
			self.rutas[r] += 1
		self.costos = [lambda : (self.rutas[0]+self.rutas[1])/100.0 + 45,
			lambda : (self.rutas[0]+self.rutas[1])/100.0 + (self.rutas[1]+self.rutas[2])/100.0,
			lambda : 45 + (self.rutas[1]+self.rutas[2])/100.0]

def print_rutas_pesos(red):
	#Imprime los resultados en pantalla
	for i in range(len(red.rutas)):
		print("Ruta " + str(i) + ":\n" +
			"\tConductores: " + str(red.rutas[i]) + "\n"
			"\tCosto: " + str(red.costos[i]()) + "\n")

#RedUno con 4000 automóviles.
ejemplo1 = RedUno(4000)

#RedBraess con 4000 automóviles.
ejemplo2 = RedBraess(4000)

#Encontramos los equilibrios de Nash.
ejemplo1.encuentra_equilibrio()
ejemplo2.encuentra_equilibrio()

#Imprimimos el resultado de la RedUno.
print("*** Red Uno. Equilibrio de Nash:\n" +
	"Conductores totales: 4000.\n")
print_rutas_pesos(ejemplo1)

print("\n")

#Imprimimos el resultado de la RedBraess.
print("*** Red Braess. Equilibrio de Nash:\n" +
	"Conductores totales: 4000.\n")
print_rutas_pesos(ejemplo2)

#while True:
#	autos = input("Cantidad de automóviles en la red (0 para salir): ")
#	if autos == 0:
#		break
#
#	ejemplo1 = RedUno(autos)
#
#	ejemplo2 = RedBraess(autos)
#
#	#Encontramos los equilibrios de Nash.
#	ejemplo1.encuentra_equilibrio()
#	ejemplo2.encuentra_equilibrio()
#
#	#Imprimimos el resultado de la RedUno.
#	print("*** Red Uno. Equilibrio de Nash:\n" +
#		"Conductores totales: " + str(autos) + ".\n")
#	print_rutas_pesos(ejemplo1)
#
#	print("\n")
#
#	#Imprimimos el resultado de la RedBraess.
#	print("*** Red Braess. Equilibrio de Nash:\n" +
#		"Conductores totales: " + str(autos) + ".\n")
#	print_rutas_pesos(ejemplo2)
