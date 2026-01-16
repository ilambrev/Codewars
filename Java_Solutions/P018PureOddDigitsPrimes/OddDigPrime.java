package P018PureOddDigitsPrimes;

import java.util.Arrays;
import java.util.stream.LongStream;

public class OddDigPrime {
    public static long[] onlyOddDigPrimes(long n) {
        long[] purePrimes = getPurePrimes(n);

        return new long[]{
                purePrimes.length,
                purePrimes[purePrimes.length - 1],
                getNextSmallestPurePrime(n)
        };
    }

    private static long getNextSmallestPurePrime(long n) {
        long currentNum = n + 1;

        while (!isPurePrime(currentNum)) {
            currentNum++;
        }

        return currentNum;
    }

    private static long[] getPurePrimes(long n) {
        return LongStream.range(2, n)
                .filter(OddDigPrime::isPurePrime)
                .toArray();
    }

    private static boolean isPurePrime(long number) {
        return isPrime(number) && Arrays.stream(String.valueOf(number).split(""))
                .map(Integer::parseInt)
                .filter(d -> d % 2 == 0)
                .toList().isEmpty();
    }

    private static boolean isPrime(long number) {
        for (long i = 2L; i <= (number / 2); i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        // Result: [7, 19, 31]
        System.out.println(Arrays.toString(onlyOddDigPrimes(20)));
        // Result: [9, 37, 53]
        System.out.println(Arrays.toString(onlyOddDigPrimes(40)));
        // Result: [10, 53, 59]
        System.out.println(Arrays.toString(onlyOddDigPrimes(55)));
        // Result: [11, 59, 71]
        System.out.println(Arrays.toString(onlyOddDigPrimes(60)));
        // Result: [15, 97, 113]
        System.out.println(Arrays.toString(onlyOddDigPrimes(100)));
    }
}
