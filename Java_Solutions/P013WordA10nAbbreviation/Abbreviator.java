import java.util.ArrayList;
import java.util.List;

public class Abbreviator {

    public String abbreviate(String string) {
        List<String> words = new ArrayList<>();
        List<String> symbols = new ArrayList<>();
        StringBuilder word = new StringBuilder();
        StringBuilder symbol = new StringBuilder();
        boolean isWord = true;

        for (int i = 0; i < string.length(); i++) {
            char currentChar = string.charAt(i);

            if (currentChar >= 'a' && currentChar <= 'z' ||
                    currentChar >= 'A' && currentChar <= 'Z') {
                if (!isWord) {
                    symbols.add(symbol.toString());
                    word.setLength(0);
                    isWord = true;
                }

                word.append(currentChar);

                if (i == string.length() - 1) {
                    words.add(word.toString());
                }
            } else {
                if (isWord) {
                    words.add(word.toString());
                    symbol.setLength(0);
                    isWord = false;
                }

                symbol.append(currentChar);

                if (i == string.length() - 1) {
                    symbols.add(symbol.toString());
                }
            }
        }

        for (int i = 0; i < words.size(); i++) {
            if (words.get(i).length() > 3) {
                String w = words.get(i);
                String abreviation = w.charAt(0) + String.valueOf(w.length() - 2) + w.charAt(w.length() - 1);
                words.set(i, abreviation);
            }
        }

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < words.size(); i++) {
            result.append(words.get(i));

            if (i < symbols.size()) {
                result.append(symbols.get(i));
            }
        }

        return result.toString();
    }
}