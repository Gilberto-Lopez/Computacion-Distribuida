/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package networks;

import java.io.*;

/**
 *
 * @author andres
 */
public class MAin {

    public static void main(String [] argv){
        /*
        Network n = new Network();
        
        n.createScaleFreeNetwork(200000);
        //n.createErdosRennyNetwork(10000, 0.3);
        
        n.calcDegreeMaxMin();
        
        System.out.println("Minimo " + n.getMinDegree());
        System.out.println("Maximo " + n.getMaxDegree());
        
        //n.saveNetwork("NetworkScaleFree");
        //n.saveDegreeDistribution("DistribucionScaleFree.csv");
        */

        try {
            //Aleatoria
            /*
            PrintWriter out_random = new PrintWriter(new FileWriter("sir_r.dat"), true);
            
            SIR modelo_random = new SIR(30000, false); //Se come la memoria, usar 1g RAM.
            
            out_random.println("0\t" + modelo_random.susceptibles + "\t" + modelo_random.infecciosos + "\t0");
            
            for (int i = 1; i < 1000; i++) {
                modelo_random.actualiza();
                out_random.println(i + "\t" + modelo_random.susceptibles + "\t" + modelo_random.infecciosos + "\t" + modelo_random.recuperados);
            }
            
            out_random.close();
            */
            //Libre de escala
            
            PrintWriter out_scalefree = new PrintWriter(new FileWriter("sir_sfn.dat"), true);

            SIR modelo_scalefree = new SIR(100000, true);

            out_scalefree.println("0\t" + modelo_scalefree.susceptibles + "\t" + modelo_scalefree.infecciosos + "\t0");

            for (int i = 1; i < 1000; i++) {
                modelo_scalefree.actualiza();
                out_scalefree.println(i + "\t" + modelo_scalefree.susceptibles + "\t" + modelo_scalefree.infecciosos + "\t" + modelo_scalefree.recuperados);
            }
            out_scalefree.close();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
