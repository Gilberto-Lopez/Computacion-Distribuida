/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package networks;

import java.util.Random;
import java.io.*;
import static java.lang.Math.*;
import java.util.ArrayList;

/**
 *
 * @author andres
 */
public class Network {

    private Node [] nodos;

    Random r;

    int maxDegree;
    int minDegree;

    public Network() {
        r = new Random();
    }

    public Node[] getNodos(){
        return this.nodos;
    }

    public void createScaleFreeNetwork(int nodeNumber) {
        this.nodos = new Node [nodeNumber];
        
        Node n1 = new Node(0);
        Node n2 = new Node(1);
        
        n1.vecs.add(n2);
        n2.vecs.add(n1);
        
        nodos[0] = n1;
        nodos[1] = n2;
        
        int totalDegree = 2;

        int totalNodes = 2;
        
        for (int i = 2; i < nodeNumber; i++) {

            Node nNode = new Node(i);

            while (nNode.vecs.isEmpty()) {
                System.out.println("Conectando nodo " + i);
                for (int j = 0; j < totalNodes; j++) {
                    
                        Node cand = nodos[j];
                    
                        double pr = (cand.vecs.size() * 1.0) / totalDegree;
                        double ran = r.nextFloat();
                        if (ran < pr) {
                            nNode.vecs.add(cand);
                            cand.vecs.add(nNode);
                            totalDegree+=2;
                        }
                    
                }
            }
            nodos[i] = nNode;
            totalNodes++;
        }
    }

    public void createErdosRennyNetwork(int nodeNumber, double connectivity) {
        this.nodos = new Node[nodeNumber];

        for (int i = 0; i < nodeNumber; i++)
            nodos[i] = new Node(i);
        
        for (int i = 1; i < nodeNumber; i++) {
            System.out.println("Conectando nodo " + i);
            Node nNode = nodos[i];
            for (int j = 0; j < i; j++) {
                double ran = r.nextDouble();

                if (ran <= connectivity) {

                    Node cand  = nodos[j];

                    nNode.vecs.add(cand);
                    cand.vecs.add(nNode);
                }
            }
        }
    }

    public int[] getDegreeDistribution() {

        calcDegreeMaxMin();

        int[] dist = new int[maxDegree - minDegree + 1];

        for (int i = 0; i < nodos.length; i++) {

            int idegree = nodos[i].vecs.size();
            
            dist[idegree - minDegree]++;
        }
        return dist;
    }

    public void calcDegreeMaxMin() {

        maxDegree = 0;
        minDegree = Integer.MAX_VALUE;

        for (int i = 0; i < nodos.length; i++) {

            maxDegree = max(maxDegree, nodos[i].vecs.size());
            minDegree = min(minDegree, nodos[i].vecs.size());
        }
    }

    public int getMaxDegree() {
        return maxDegree;
    }

    public int getMinDegree() {
        return minDegree;
    }

    public double[] calcClusteringCoefficient() {

        double[] clCoefficient = new double[nodos.length];

        for (int i = 0; i < nodos.length; i++) {

            Node n = nodos[i];
            ArrayList<Node> vecs = n.vecs;
            
            int posibles = vecs.size() * (vecs.size() - 1);
            posibles = posibles == 0? 1: posibles;

            int existentes = 0;

            for (int j = 0; j < vecs.size(); j++) {
                
                Node v = vecs.get(j);
                
                for(int k = 0; k < vecs.size(); k++){
                    Node v2 = vecs.get(k);
                    
                    if(v.connectedWith(v2)){
                        existentes++;
                    }
                }
            }
            clCoefficient[i] = (existentes * 1.0) / posibles;
            
        }
        return clCoefficient;
    }

    public int[] calcClusteringDistribution() {
        return null;
    }

    public void saveNetwork(String file) {
        try {
            PrintWriter pw = new PrintWriter(new FileWriter(file + "_aristas.csv"), true);
            pw.println("Source,Target,Type");

            for (int i = 0; i < nodos.length; i++) {
                ArrayList<Node> ady = nodos[i].vecs;
                int id = nodos[i].id;
                
                for(int j = 0; j < ady.size(); j++){
                    
                    Node n = ady.get(j);
                    
                    if(n.id > id){                    
                        pw.println(id + "," + n.id + ",Undirected");
                    }

                }

                    
                
            }

            pw.close();

            PrintWriter pwNodos = new PrintWriter(new FileWriter(file + "_nodos.csv"), true);

            pwNodos.println("id,label");

            for (int i = 0; i < nodos.length; i++) {
                pwNodos.println(nodos[i].id + "," + nodos[i].id);
            }

            pwNodos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void saveDegreeDistribution(String file) {

        try {

            PrintWriter pw = new PrintWriter(new FileWriter(file), true);

            int[] dist = getDegreeDistribution();

            for (int i = 0; i < dist.length; i++) {
                pw.println((minDegree + i) + "," + dist[i]);
            }
            pw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void saveClusteringDistribution() {

    }

    
    class Node{
        int id;
        
        public ArrayList<Node> vecs;
        public SIR.Agente a;
        
        public Node(int id){
            this.id = id;
            vecs = new ArrayList<>();
            a = null;
        }
        
        public boolean equals(Node n){
            return this.id == n.id;
        }
        
        public boolean connectedWith(Node n){
            int idN = n.id;
            
            boolean res = false;
            
            for(int i = 0; i < vecs.size(); i++){
                Node cand = vecs.get(i);
                
                if(cand.id == idN){
                    res = true;
                    break;
                }
            }
            return res;
        }
    }
}
