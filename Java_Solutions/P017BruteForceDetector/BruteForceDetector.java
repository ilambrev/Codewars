package P017BruteForceDetector;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BruteForceDetector {
    public static List<String> detectBruteForce(String[] logs) {
        Map<String, Integer> suspiciousIPs = new HashMap<>();

        for (String log : logs) {
            String[] logTokens = log.split("\\s+");
            String ip = logTokens[0];
            String cause = logTokens[1];

            if (cause.equals("LOGIN_FAIL")) {
                suspiciousIPs.merge(ip, 1, Integer::sum);
            }

            if (cause.equals("LOGIN_SUCCESS")) {
                suspiciousIPs.computeIfPresent(ip, (k, v) -> v < 3 ? 0 : v);
            }
        }

        return suspiciousIPs.entrySet()
                .stream()
                .filter(ip -> ip.getValue() >= 3)
                .map(Map.Entry::getKey)
                .sorted()
                .toList();
    }

    public static void main(String[] args) {
        // Result: [192.168.1.1]
        String[] logs1 = {
                "192.168.1.1 LOGIN_FAIL user=admin",
                "192.168.1.1 LOGIN_FAIL user=admin",
                "192.168.1.1 LOGIN_FAIL user=admin"
        };

        // Result: []
        String[] logs2 = {
                "10.0.0.5 LOGIN_FAIL user=x",
                "10.0.0.5 LOGIN_FAIL user=x",
                "10.0.0.5 LOGIN_SUCCESS user=x",
                "10.0.0.5 LOGIN_FAIL user=x"
        };

        // Result: [1.1.1.1]
        String[] logs3 = {
                "1.1.1.1 LOGIN_FAIL user=a",
                "2.2.2.2 LOGIN_FAIL user=b",
                "1.1.1.1 LOGIN_FAIL user=a",
                "2.2.2.2 LOGIN_SUCCESS user=b",
                "1.1.1.1 LOGIN_FAIL user=a",
                "2.2.2.2 LOGIN_FAIL user=b"
        };

        // Result: [5.5.5.5]
        String[] logs4 = {
                "5.5.5.5 LOGIN_FAIL user=x",
                "5.5.5.5 LOGIN_FAIL user=x",
                "5.5.5.5 LOGIN_FAIL user=x",
                "5.5.5.5 LOGIN_SUCCESS user=x",
                "5.5.5.5 LOGIN_FAIL user=x",
                "5.5.5.5 LOGIN_FAIL user=x",
                "5.5.5.5 LOGIN_FAIL user=x"
        };

        // Result: []
        String[] logs5 = {};

        // Result: [1.1.1.1, 9.9.9.9]
        String[] logs6 = {
                "9.9.9.9 LOGIN_FAIL user=a",
                "1.1.1.1 LOGIN_FAIL user=b",
                "9.9.9.9 LOGIN_FAIL user=a",
                "1.1.1.1 LOGIN_FAIL user=b",
                "9.9.9.9 LOGIN_FAIL user=a",
                "1.1.1.1 LOGIN_FAIL user=b"
        };

        System.out.println(detectBruteForce(logs1));
        System.out.println(detectBruteForce(logs2));
        System.out.println(detectBruteForce(logs3));
        System.out.println(detectBruteForce(logs4));
        System.out.println(detectBruteForce(logs5));
        System.out.println(detectBruteForce(logs6));
    }
}
