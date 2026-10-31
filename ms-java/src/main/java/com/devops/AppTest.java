package com.devops;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    @Test
    public void testMultiplicar() {
        App app = new App();
        int resultado = app.multiplicar(4, 5);
        assertEquals(20, resultado, "La multiplicación de 4 x 5 debe ser 20");
    }

    @Test
    public void testEsPositivo() {
        App app = new App();
        assertTrue(app.esPositivo(10), "El número 10 debe evaluarse como positivo");
        assertFalse(app.esPositivo(-5), "El número -5 no debe evaluarse como positivo");
    }
}