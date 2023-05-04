class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {

        int sum = 0;
        int currentOddNumber = n * n - (n - 1);

        if (n > 0) {
            for (int i = 1; i <= n; i++) {
                sum += currentOddNumber;
                currentOddNumber += 2;
            }
        }

        return sum;
    }
}