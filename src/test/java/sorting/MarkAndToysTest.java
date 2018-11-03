package sorting;

import org.junit.Test;

import static org.junit.Assert.*;
import static sorting.MarkAndToys.maximumToys;

public class MarkAndToysTest {

    @Test
    public void testEx() {
        assertEquals(3, maximumToys(new int[] {1,2,3,4}, 7));
    }

    @Test
    public void test0() {
        assertEquals(4, maximumToys(new int[] {1, 12, 5, 111, 200, 1000, 10}, 50));
    }

    @Test
    public void test2() {
        assertEquals(3, maximumToys(new int[] {3, 7, 2, 9, 4}, 15));
    }

}