package P022BackwardsReadPrimes;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class BackWardsPrime {
    public static String backwardsPrime(long start, long end) {
        List<Long> backwardPrimes = new ArrayList<>();

        for (long i = start; i <= end; i++) {
            if (isPrime(i) && isBackwardPrime(i)) {
                backwardPrimes.add(i);
            }
        }

        return backwardPrimes.stream()
                .sorted()
                .map(String::valueOf)
                .collect(Collectors.joining(" "));
    }

    private static boolean isBackwardPrime(long number) {
        long backwardNumber = Long.parseLong(Stream.of(String.valueOf(number))
                .map(string -> new StringBuilder(string).reverse())
                .collect(Collectors.joining()));

        if (number == backwardNumber || String.valueOf(backwardNumber).length() < 2) {
            return false;
        }

        return isPrime(backwardNumber);
    }

    private static boolean isPrime(long number) {
        for (long i = 2; i <= 1 + number / 2; i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        // Result: 13 17 31 37 71 73 79 97
        System.out.println(backwardsPrime(1, 100));

        // Result: 9923 9931 9941 9967
        System.out.println(backwardsPrime(9900, 10000));
    }
}
