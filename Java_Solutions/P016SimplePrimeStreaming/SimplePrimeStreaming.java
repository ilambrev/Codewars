public class SimplePrimeStreaming {

    public static String solve(int a, int b) {
        StringBuilder primeStream = new StringBuilder();
        primeStream.append(2);

        int counter = 3;

        while (primeStream.length() < a + b) {
            boolean isNumberPrime = true;

            for (int i = 2; i < counter; i++) {
                if (counter % i == 0) {
                    isNumberPrime = false;
                    break;
                }
            }

            if (isNumberPrime) {
                primeStream.append(counter);
            }

            counter++;
        }

        return primeStream.substring(a, a + b);
    }
}