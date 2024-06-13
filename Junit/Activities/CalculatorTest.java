package examples;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class CalculatorTest {
    Calculator calc = new Calculator();

    @Test
    public void addTest() {
        int actualResult = calc.add(10, 5);
        Assertions.assertEquals(15, actualResult);
    }

    @Test
    public void multiplyTest() {
        int actualResult = calc.multiply(10, 10);
        Assertions.assertEquals(100, actualResult);
    }
}