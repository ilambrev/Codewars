import java.util.Arrays;

public class Kata {
    public static String high(String s) {
        int highScore = 0;
        String word = "";

        String[] words = s.split("\\s+");

        if (s.length() > 0) {
            for (String string : words) {
                int scores = calcScores(string);

                if (scores > highScore) {
                    highScore = scores;
                    word = string;
                }
            }
        }

        return word;
    }

    static int calcScores(String word) {
        return Arrays.stream(word.split("")).mapToInt(letter -> (int) letter.charAt(0) - 96).sum();
    }
}