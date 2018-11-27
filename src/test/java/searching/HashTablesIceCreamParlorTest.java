package searching;

import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;
import static searching.HashTablesIceCreamParlor.whatFlavors;

public class HashTablesIceCreamParlorTest {

    private OutputStream os = new ByteArrayOutputStream();
    private PrintStream out = new PrintStream(os);

    @Before
    public void setup() {
        System.setOut(out);
    }

    @Test
    public void test_ex1() {
        whatFlavors(new int[] {1, 4, 5, 3, 2}, 4);
        assertEquals("1 4", os.toString());
    }

    @Test
    public void test_ex2() {
        whatFlavors(new int[] {2, 2, 4, 3}, 4);
        assertEquals("1 2", os.toString());
    }

    @Test
    public void test_ex0() {
        whatFlavors(new int[] {2, 1, 3, 5, 6}, 5);
        assertEquals("1 3", os.toString());
    }
}