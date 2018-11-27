package sorting;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class FraudulentActivityNotifications {

    // Complete the activityNotifications function below.
    public static int activityNotifications(int[] expenditure, int d) {
        int n = expenditure.length;
        if (n == d) {
            return 0;
        }
        int alert = 0;
        int removedDay = -1;
        int[] prevDays = Arrays.copyOfRange(expenditure, 0, 5);
        double prevMed = med(prevDays);
        for (int i = d; i < n; i++) {
            int e = expenditure[i];
            if (e == 0) {
                continue;
            }

            int newDay = expenditure[i - 1];
            if (newDay == removedDay) {
                continue;
            }

            double m = -1;
            if (d % 2 != 0) {
                if (removedDay < prevMed && newDay < prevMed) {
                    m = prevMed;
                } else if (removedDay > prevMed && newDay > prevMed) {
                    m = prevMed;
                }
            } else {
                if (d > 5) {
                    int mid = n / 2;
                    int left = expenditure[mid - 1];
                    int right = expenditure[mid];
                    if (removedDay < left && newDay < left) {
                        m = prevMed;
                    } else if (removedDay > right && newDay > right) {
                        m = prevMed;
                    }
                }
            }
            int[] days = Arrays.copyOfRange(expenditure, i - d, i);
            if (m == -1) {
                m = med(days);
            }

            if (e >= m * 2) {
                alert++;
            }
            removedDay = expenditure[i-d];
            prevMed = m;
            prevDays = days;
        }
        return alert;
    }

    private static double med(int[] a) {
        int n = a.length;
        if (n == 1) {
            return a[0];
        }
        if (n == 2) {
            return (a[0] + a[1]) / 2.0;
        }
        Arrays.sort(a);
        int mid = n / 2;
        if (n % 2 == 0) {
            return (a[mid - 1] + a[mid]) / 2.0;
        }
        return a[mid];
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);

        int d = Integer.parseInt(nd[1]);

        int[] expenditure = new int[n];

        String[] expenditureItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int expenditureItem = Integer.parseInt(expenditureItems[i]);
            expenditure[i] = expenditureItem;
        }

        int result = activityNotifications(expenditure, d);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }

}
