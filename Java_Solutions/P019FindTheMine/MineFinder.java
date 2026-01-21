package P019FindTheMine;

import java.util.Arrays;

public class MineFinder {
    public static int[] findMine(int[][] field) {
        int[] mineCoordinates = new int[2];

        for (int i = 0; i < field.length; i++) {
            for (int j = 0; j < field[i].length; j++) {
                if (field[i][j] == 1) {
                    mineCoordinates[0] = i;
                    mineCoordinates[1] = j;
                    break;
                }
            }
        }

        return mineCoordinates;
    }

    public static void main(String[] args) {
        // Result: [0, 0]
        int[][] field1 = {{1, 0}, {0, 0}};
        // Result: [0, 0]
        int[][] field2 = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        // Result: [2, 2]
        int[][] field3 = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}};

        System.out.println(Arrays.toString(findMine(field1)));
        System.out.println(Arrays.toString(findMine(field2)));
        System.out.println(Arrays.toString(findMine(field3)));
    }
}
