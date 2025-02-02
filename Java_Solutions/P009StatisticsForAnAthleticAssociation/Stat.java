import java.util.Arrays;

public class Stat {
    public static String stat(String strg) {
        int[] runnersStatsInSeconds = Arrays.stream(strg.split(",\\s+"))
                .mapToInt(Stat::parseStatsToSeconds)
                .toArray();
        int rangeInSeconds = countRange(runnersStatsInSeconds);
        int averageInSeconds = countAverage(runnersStatsInSeconds);
        int medianInSeconds = countMedian(runnersStatsInSeconds);

        return String.format("Range: %s Average: %s Median: %s",
                parseSecondsToString(rangeInSeconds),
                parseSecondsToString(averageInSeconds),
                parseSecondsToString(medianInSeconds));
    }

    static int countRange(int[] runnersStatsInSeconds) {
        int[] sortedStats = sortStats(runnersStatsInSeconds);

        return sortedStats[sortedStats.length - 1] - sortedStats[0];
    }

    static int countAverage(int[] runnersStatsInSeconds) {
        int statsSumInSeconds = Arrays.stream(runnersStatsInSeconds)
                .sum();

        return statsSumInSeconds / runnersStatsInSeconds.length;
    }

    static int countMedian(int[] runnersStatsInSeconds) {
        int[] sortedStats = sortStats(runnersStatsInSeconds);
        int statsNum = sortedStats.length;

        return statsNum % 2 != 0 ? sortedStats[statsNum / 2] :
                (sortedStats[statsNum / 2] + sortedStats[statsNum / 2 - 1]) / 2;
    }

    static int[] sortStats(int[] runnersStatsInSeconds) {
        return Arrays.stream(runnersStatsInSeconds)
                .sorted()
                .toArray();
    }

    static int parseStatsToSeconds(String stat) {
        int[] partsOfStat = Arrays.stream(stat.split("\\|"))
                .mapToInt(Integer::parseInt)
                .toArray();

        return partsOfStat[0] * 3600 + partsOfStat[1] * 60 + partsOfStat[2];
    }

    static String parseSecondsToString(int seconds) {
        int h = seconds / 3600;
        int m = (seconds - (h * 3600)) / 60;
        int s = seconds - (h * 3600 + m * 60);

        return String.format("%02d|%02d|%02d", h, m, s);
    }
}