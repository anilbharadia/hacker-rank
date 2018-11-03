package sorting;

import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static sorting.BubbleSort.countSwaps;

public class BubbleSortTest {

    ByteArrayOutputStream out;
    String LS = System.lineSeparator();


    @Before
    public void setup() {
        out = new ByteArrayOutputStream();
        System.setOut(new PrintStream(out));
    }

    @Test
    public void testExample() {
        countSwaps(new int[]{6, 4, 1});
        assertEquals(buildExpected(3, 1, 6), out.toString());
    }

    @Test
    public void test0() {
        countSwaps(new int[]{1, 2, 3});
        assertEquals(buildExpected(0, 1, 3), out.toString());
    }

    @Test
    public void test1() {
        countSwaps(new int[]{3, 2, 1});
        assertEquals(buildExpected(3, 1, 3), out.toString());
    }

    @Test
    public void test2() {
        countSwaps(new int[]{4, 2, 3, 1});
        assertEquals(buildExpected(5, 1, 4), out.toString());
    }

    private String buildExpected(final int swaps, final int first, final int last) {
        return "Array is sorted in " + swaps + " swaps." + LS +
                "First Element: " + first + LS +
                "Last Element: " + last;
    }

}