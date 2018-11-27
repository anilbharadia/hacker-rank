package sorting;

import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.*;
import static sorting.FraudulentActivityNotifications.activityNotifications;

public class FraudulentActivityNotificationsTest {

    @Test
    public void testEx() {
        assertEquals(2, activityNotifications(new int[] {2, 3, 4, 2, 3, 6, 8, 4, 5}, 5));
    }

    @Test
    public void test_1() {
        assertEquals(0, activityNotifications(new int[] {1, 2, 3, 4, 4}, 4));
    }

    @Test
    public void test_2() {
        assertEquals(1, activityNotifications(new int[] {10, 20, 30, 40, 50}, 3));
    }

    @Test
    public void test_x() {
        int[] a = new int[200000];
        for (int i = 0; i < 200000; i++) {
            a[i] = 10;
        }
        assertEquals(0, activityNotifications(a, 100000));
    }

//    @Test(timeout = 1000 * 30)
    @Test()
    public void test_x1() {
        int[] a = new Random().ints(200000, 0, 200).toArray();
        assertEquals(0, activityNotifications(a, 5));
    }
}