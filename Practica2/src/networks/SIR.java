package networks;

import java.util.Random;
import java.io.*;
import java.lang.Math;
import java.util.ArrayList;

/**
* Modelo epidémico SIR.
*/
public class SIR {
	
	/* Red de agentes. */
	private Network red;
	private Random random;
	/* Cantidad de agentes susceptibles. */
	public int susceptibles;
	/* Cantidad de agentes infecciosos. */
	public int infecciosos;
	/* Cantidad de agentes recuperados. */
	public int recuperados;

	/** Tiempo que un agente pasa en el estado Recuperado. */
	//Influenza
	//public final static int TIEMPO_RECUPERADO = 14;
	//Difteria
	public final static int TIEMPO_RECUPERADO = 35;
	/** Tiempo que un agente pasa en el estado Infeccioso. */
	//Influenza
	//public final static int TIEMPO_INFECCIOSO = 10;
	//Difteria
	public final static int TIEMPO_INFECCIOSO = 21;
	/** Cantidad de angetes que inician en el estado Infeccioso. */
	public final static int INFECTADOS_INICIALES = 100;

	/**
	* Estados de los agentes:
	* -Susceptible
	* -Infeccioso
	* -Recuperado
	*/
	public enum Estado {
		SUSCEPTIBLE,
		INFECCIOSO,
		RECUPERADO
	}

	/* Agentes de la red. */
	class Agente {

		/* Resistencia a la infección. */
		public double theta;
		/* Probabilidad de interacción. */
		public double p;
		/* Estado actual. */
		public SIR.Estado e;
		/* Estado siguiente. */
		public SIR.Estado s;
		/* Tiempo en el estado actual. */
		public int t;

		public Agente (double resistencia, double interaccion){
			theta = resistencia;
			p = interaccion;
			e = s = SIR.Estado.SUSCEPTIBLE;
			t = 0;
		}

	}

	/**
	* Genera un nuevo modelo con agentes con una red libre de escala.
	* La cantidad de agentes infecciosos al iniciar es por default INFECTADOS_INICIALES.
	* @param agentes La cantidad de agentes en el modelo.
	* @param scaleFree <strong>true</strong> genera un modelo a partir de una red libre de escala,
	*	<strong>false</strong> a partir de una gráfica aleatoria.
	*/
	public SIR (int agentes, boolean scaleFree) {
		random = new Random();
		red = new Network();
		if (scaleFree)
			red.createScaleFreeNetwork(agentes);
		else
			red.createErdosRennyNetwork(agentes, 0.3);
		recuperados = 0;
		infecciosos = SIR.INFECTADOS_INICIALES;
		susceptibles = agentes - infecciosos;
		for(Network.Node v : red.getNodos())
			v.a = new Agente(random.nextDouble(), random.nextDouble());
		int i = 0;
		while (i < infecciosos) {
			int r = random.nextInt(agentes);
			Network.Node n = red.getNodos()[r];
			if (n.a.e == Estado.SUSCEPTIBLE) {
				n.a.e = n.a.s = Estado.INFECCIOSO;
				i++;
			}
		}
	}

	/**
	* Actuliza los estados de los agentes de la red un una unidad de tiempo.
	* Regresa una tupla (s,i,r) donde:
	* s : El número de agentes susceptibles.
	* i : El número de agentes infecciosos.
	* r : El número de agentes recuperados.
	*/
	public void actualiza () {
		//Actualizamos estados.
		for (Network.Node v : red.getNodos())
			if (v.a.e != v.a.s) {
				v.a.e = v.a.s;
				v.a.t = 0;
				switch (v.a.s) {
					case INFECCIOSO: //Susceptible -> Infeccioso
						susceptibles--;
						infecciosos++;
						break;
					case RECUPERADO: //Infeccioso -> Recuperado
						infecciosos--;
						recuperados++;
						break;
					case SUSCEPTIBLE: //Recuperado -> Susceptible
						recuperados--;
						susceptibles++;
				}
			}
		for (Network.Node v : red.getNodos()) {
			Agente ag = v.a;
			if (ag.e == Estado.INFECCIOSO){ //Estado infeccioso.
				for (Network.Node vecino : v.vecs) {
					Agente vag = vecino.a;
					double r = random.nextDouble();
					if (r <= ag.p) { //Interactúa con el vecino.
						double g = random.nextDouble();
						if (vag.e == Estado.SUSCEPTIBLE && g > vag.theta) { //Infecta al vecino
							vag.s = Estado.INFECCIOSO;
						}
					}
				}
				ag.t++;
				if (ag.t > TIEMPO_INFECCIOSO) //Pasa a recuperado.
					ag.s = Estado.RECUPERADO;
			} else if (ag.e == Estado.RECUPERADO) { //Estado recuperado.
				ag.t++;
				if (ag.t > TIEMPO_RECUPERADO) //Pasa a ser susceptible.
					ag.s = Estado.SUSCEPTIBLE;
			}
			/*
			else { //Estado susceptible.
				//Pasivo.
				continue
			}
			*/
		}
	}

}