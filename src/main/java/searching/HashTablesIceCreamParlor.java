package searching;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HashTablesIceCreamParlor {


    // Complete the whatFlavors function below.
    static void whatFlavors(int[] cost, int money) {
        Map<Integer, Integer> map = new HashMap<>();

        int index = 1;
        for (int c : cost) {
            if (map.containsKey(c)) {
                System.out.print(map.get(c) + " " + index);
                return;
            }
            map.put(money - c, index);
            index++;
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int money = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] cost = new int[n];

            String[] costItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int costItem = Integer.parseInt(costItems[i]);
                cost[i] = costItem;
            }

            whatFlavors(cost, money);
        }

        scanner.close();
    }
}
