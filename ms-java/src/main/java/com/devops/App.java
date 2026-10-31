package com.devops;

public class App {
    public static void main(String[] args) {
        System.out.println("Microservicio Java DevOps ejecutándose correctamente.");
    }

    public int multiplicar(int a, int b) {
        return a * b;
    }

    public boolean esPositivo(int numero) {
        return numero >= 0;
    }
}