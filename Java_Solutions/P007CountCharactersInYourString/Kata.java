import java.util.HashMap;
import java.util.Map;

public class Kata {
    public static Map<Character, Integer> count(String str) {
        Map<Character, Integer> chars = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {
            Character character = str.charAt(i);
            chars.putIfAbsent(character, 0);
            chars.put(character, chars.get(character) + 1);
        }

        return chars;
    }
}