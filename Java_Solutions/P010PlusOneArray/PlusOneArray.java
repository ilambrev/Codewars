import java.math.BigInteger;
import java.util.Arrays;
import java.util.stream.Collectors;

public class PlusOneArray {
    public static int[] upArray(final int[] arr) {
        if (arr != null && arr.length > 0 && Arrays.stream(arr)
                .filter(n -> n < 0 || n > 9)
                .toArray().length == 0) {

            String numAsString = Arrays.stream(arr)
                    .mapToObj(String::valueOf)
                    .collect(Collectors.joining(""));

            BigInteger newNum = new BigInteger(numAsString);

            String newNumAsString = newNum.add(BigInteger.ONE).toString();

            if (newNumAsString.length() < numAsString.length()) {
                newNumAsString = "0".repeat(numAsString.length() - newNumAsString.length()) + newNumAsString;
            }

            return Arrays.stream(newNumAsString.split(""))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        return null;
    }
}