package P021DecoderArrowPinCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Kata {
    public static int[] decArrowPinCode(String arrowStr) {
        String[][] keypad = {
                {"7", "8", "9"},
                {"4", "5", "6"},
                {"1", "2", "3"},
                {"0"}
        };

        String[] tokens = arrowStr.split("");

        int row = -1;
        int col = -1;

        for (int i = 0; i < keypad.length; i++) {
            boolean isFound = false;
            for (int j = 0; j < keypad[i].length; j++) {
                if (keypad[i][j].equals(tokens[0])) {
                    row = i;
                    col = j;
                    isFound = true;
                    break;
                }
            }
            if (isFound) {
                break;
            }
        }

        List<Integer> result = new ArrayList<>();

        result.add(Integer.parseInt(keypad[row][col]));
        boolean isMultiplier = false;

        for (int i = 1; i < tokens.length; i++) {
            if (tokens[i].equals("↑")) {
                row--;
            }
            if (tokens[i].equals("↓")) {
                row++;
            }
            if (tokens[i].equals("←")) {
                col--;
            }
            if (tokens[i].equals("→")) {
                col++;
            }
            if (row > keypad.length - 1 || row < 0 || col > keypad[row].length - 1 || col < 0) {
                result.clear();
                break;
            }
            if (tokens[i].equals("*")) {
                isMultiplier = true;
                continue;
            }
            if (isMultiplier) {
                for (int j = 1; j <= Integer.parseInt(tokens[i]); j++) {
                    result.add(Integer.parseInt(keypad[row][col]));
                }
                isMultiplier = false;
            } else {
                result.add(Integer.parseInt(keypad[row][col]));
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        // Result: [1, 2, 5, 6]
        String arrowPinCode1 = "1→↑→";

        // Result: [1, 1, 1, 0]
        String arrowPinCode2 = "1*2↓";

        // Result: [0, 0, 0, 1]
        String arrowPinCode3 = "0*2↑";

        // Result: [0, 1, 4, 7]
        String arrowPinCode4 = "0↑↑↑";

        // Result: []
        String arrowPinCode5 = "0↑↑↑↑";

        // Result: []
        String arrowPinCode6 = "8↑*5→";

        // Result: []
        String arrowPinCode7 = "0←*2←";

        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode1)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode2)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode3)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode4)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode5)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode6)));
        System.out.println(Arrays.toString(Kata.decArrowPinCode(arrowPinCode7)));
    }
}
