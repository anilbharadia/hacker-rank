package strings;

import org.junit.Test;

import static org.junit.Assert.*;
import static strings.CommonChild.commonChild;

public class CommonChildTest {

    @Test
    public void test_ex() {
        assertEquals(3, commonChild("ABCD", "ABDC"));
    }

    @Test
    public void test_sample() {
        assertEquals(2, commonChild("HARRY", "SALLY"));
    }

    @Test
    public void test_sample1() {
        assertEquals(0, commonChild("AA", "BB"));
    }

    @Test
    public void test_sample2() {
        assertEquals(3, commonChild("SHINCHAN", "NOHARAAA"));
    }

    @Test
    public void test_sample3() {
        assertEquals(2, commonChild("ABCDEF", "FBDAMN"));
    }

    @Test
    public void test_c1() {
        assertEquals(7, commonChild("ABAABBABA", "ABABABBBB"));
    }

    @Test
    public void test_c2() {
        assertEquals(7, commonChild("CABAABBABA", "ABABABBBBC"));
    }

    @Test
    public void test_c2_1() {
        assertEquals(7, commonChild("ABACABBABA", "ABABABBBBC"));
    }

    @Test
    public void test_c2_2() {
        assertEquals(7, commonChild("ABACACBBABA", "ABABABBBCBC"));
    }

    @Test
    public void test_c3() {
        assertEquals(8, commonChild("ABAABBABAC", "ABABABBBBC"));
    }

    @Test
    public void test_c4() {
        assertEquals(9, commonChild("CABAABBABAC", "CABABABBBBC"));
    }

}