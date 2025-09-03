import java.util.*;

public class Solution {
    static Comparator<PlayerRecord> playerComparator() {
        return Comparator.comparing(PlayerRecord::getScore).reversed()
                .thenComparing(PlayerRecord::getName);
    }

    public static List<PlayerRecord> topScores(List<PlayerRecord> records, int nTop) {
        if (nTop <= 0) {
            return new ArrayList<>();
        }

        Map<String, Integer> highPlayersResults = new HashMap<>();

        for (PlayerRecord record : records) {
            highPlayersResults.putIfAbsent(record.getName(), 0);

            if (highPlayersResults.get(record.getName()) < record.getScore()) {
                highPlayersResults.put(record.getName(), record.getScore());
            }
        }

        List<PlayerRecord> orderedResults = highPlayersResults
                .entrySet()
                .stream()
                .map(p -> new PlayerRecord(p.getKey(), p.getValue()))
                .sorted(playerComparator())
                .toList();

        if (orderedResults.size() > nTop) {
            List<PlayerRecord> firstNResults = new ArrayList<>();

            for (int i = 0; i < nTop; i++) {
                firstNResults.add(orderedResults.get(i));
            }

            return firstNResults;
        }

        return orderedResults;
    }
}


class PlayerRecord {
    private final String name;
    private final int score;

    public PlayerRecord(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() { return name; }
    public int getScore() { return score; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof PlayerRecord)) return false;
        PlayerRecord other = (PlayerRecord) o;
        return score == other.score &&
                Objects.equals(name, other.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, score);
    }

    @Override
    public String toString() {
        return "[" + name + ", " + score + "]";
    }
}