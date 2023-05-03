import java.util.LinkedHashMap;
import java.util.Map;

public class DuplicateEncoder {
    static String encode(String word){

        Map<Character, Integer> characters = new LinkedHashMap<>();

        for (int i = 0; i < word.length(); i++) {
            char currentChar = word.toLowerCase().charAt(i);
            characters.putIfAbsent(currentChar, 0);
            int charOldCount = characters.get(currentChar);
            characters.put(currentChar, charOldCount + 1);
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < word.length(); i++) {
            char currentChar = word.toLowerCase().charAt(i);
            if(characters.get(currentChar) == 1) {
                sb.append("(");
            } else {
                sb.append(")");
            }
        }

        word = sb.toString();

        return word;
    }
}