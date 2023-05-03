import java.util.Arrays;

public class StringSplit {
    public static String[] solution(String s) {

        boolean isNumberOfCharactersOdd = s.length() % 2 != 0;

        int arraySize = isNumberOfCharactersOdd ? s.length() / 2 + 1 : s.length() / 2;

        String[] pairs = new String[arraySize];

        for (int i = 0; i < pairs.length; i++) {

            if (i == pairs.length - 1 && isNumberOfCharactersOdd) {
                pairs[i] = s.substring(i * 2) + "_";
            } else {
                pairs[i] = s.substring(i * 2, i * 2 + 2);
            }
        }

        return pairs;
    }
}