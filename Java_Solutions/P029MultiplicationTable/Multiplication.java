package P029MultiplicationTable;

import java.util.Arrays;

public class Multiplication {
    public static int[][] multiplicationTable(int n) {
        int[][] table = new int[n][n];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                table[i - 1][j - 1] = i * j;
            }
        }

        return table;
    }

    public static void main(String[] args) {
        int n1 = 3;
        int n2 = 1;

        // Expected Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        System.out.println(Arrays.deepToString(multiplicationTable(n1)));

        // Expected Result: [[1]]
        System.out.println(Arrays.deepToString(multiplicationTable(n2)));
    }
}
