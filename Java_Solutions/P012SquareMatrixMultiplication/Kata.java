public class Kata {

    public static int[][] matrixMultiplication(int[][] a, int[][] b) {
        int[][] c = new int[a.length][a[0].length];
        for (int i = 0; i < c.length; i++) {
            for (int j = 0; j < c[0].length; j++) {
                c[i][j] = calculateElement(new int[]{i, j}, a, b);
            }
        }

        return c;
    }

    static int calculateElement(int[] element, int[][] a, int[][] b) {
        int sum = 0;
        for (int i = 0; i < a[element[0]].length; i++) {
            sum += a[element[0]][i] * b[i][element[1]];
        }

        return sum;
    }
}