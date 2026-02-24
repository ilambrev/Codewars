package P028SumsOfParts;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SumParts {
    public static int[] sumParts(int[] ls) {
        int sum = Arrays.stream(ls).sum();

        List<Integer> result = new ArrayList<>();
        result.add(sum);

        for (int i = 1; i <= ls.length; i++) {
            sum -= ls[i - 1];
            result.add(sum);
        }

        return result.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }

    public static void main(String[] args) {
        int[] ls1 = new int[0];
        int[] ls2 = {0, 1, 3, 6, 10};
        int[] ls3 = {1, 2, 3, 4, 5, 6};
        int[] ls4 = {744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358};

        // Expected Result: [0]
        System.out.println(Arrays.toString(sumParts(ls1)));

        // Expected Result: [20, 20, 19, 16, 10, 0]
        System.out.println(Arrays.toString(sumParts(ls2)));

        // Expected Result: [21, 20, 18, 15, 11, 6, 0]
        System.out.println(Arrays.toString(sumParts(ls3)));

        // Expected Result: [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
        System.out.println(Arrays.toString(sumParts(ls4)));
    }
}
