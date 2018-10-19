import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    // Complete the climbingLeaderboard function below.
    static int[] climbingLeaderboard(int[] scores, int[] alices) {

        List<Integer> leaderboard = Arrays.stream(scores)
                .boxed()
                .distinct()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());



        List<Integer> aliceScores = Arrays.stream(alices)
                .boxed()
                .distinct()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());
        int rank = 1;
        int leaderboardIndex = 0;
        Map<Integer, Integer> aliceScoreRankMap = new HashMap<>();
        for (int alice : aliceScores) {
            for (; leaderboardIndex < leaderboard.size(); leaderboardIndex++) {
                if (alice >= leaderboard.get(leaderboardIndex)) {
                    break;
                }
                rank++;
            }
            aliceScoreRankMap.put(alice, rank);
        }

        int[] aliceRanks = new int[alices.length];

        int i = 0;
        for (int alice : alices) {
            aliceRanks[i++] = aliceScoreRankMap.get(alice);
        }

        return aliceRanks;
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int scoresCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] scores = new int[scoresCount];

        String[] scoresItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < scoresCount; i++) {
            int scoresItem = Integer.parseInt(scoresItems[i]);
            scores[i] = scoresItem;
        }

        int aliceCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] alice = new int[aliceCount];

        String[] aliceItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < aliceCount; i++) {
            int aliceItem = Integer.parseInt(aliceItems[i]);
            alice[i] = aliceItem;
        }

        int[] result = climbingLeaderboard(scores, alice);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }

}
