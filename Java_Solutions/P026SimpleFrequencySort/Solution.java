package P026SimpleFrequencySort;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static int[] sortByFrequency(int[] array) {
        Map<Integer, Integer> numbers = new HashMap<>();

        for (int num : array) {
            numbers.putIfAbsent(num, 0);
            numbers.put(num, numbers.get(num) + 1);
        }

        return numbers.entrySet().stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed()
                        .thenComparing(Map.Entry.comparingByKey()))
                .map(n -> {
                    int[] a = new int[n.getValue()];
                    Arrays.fill(a, n.getKey());
                    return a;
                }).flatMapToInt(Arrays::stream)
                .toArray();
    }

    public static void main(String[] args) {
        // Expected Result: [3, 3, 3, 5, 5, 7, 7, 2, 9]
        int[] array1 = {2, 3, 5, 3, 7, 9, 5, 3, 7};

        // Expected Result: [1, 1, 1, 0, 0, 6, 6, 8, 8, 2, 3, 5, 9]
        int[] array2 = {1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1};

        // Expected Result: [9, 9, 9, 9, 4, 4, 5, 5, 6, 6]
        int[] array3 = {5, 9, 6, 9, 6, 5, 9, 9, 4, 4};

        // Expected Result: [1, 1, 2, 2, 3, 3, 4, 4, 5, 8]
        int[] array4 = {4, 4, 2, 5, 1, 1, 3, 3, 2, 8};

        // Expected Result: [0, 0, 4, 4, 9, 9, 3, 5, 7, 8]
        int[] array5 = {4, 9, 5, 0, 7, 3, 8, 4, 9, 0};

        System.out.println(Arrays.toString(sortByFrequency(array1)));
        System.out.println(Arrays.toString(sortByFrequency(array2)));
        System.out.println(Arrays.toString(sortByFrequency(array3)));
        System.out.println(Arrays.toString(sortByFrequency(array4)));
        System.out.println(Arrays.toString(sortByFrequency(array5)));
    }
}
