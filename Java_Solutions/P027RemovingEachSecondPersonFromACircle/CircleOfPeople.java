package P027RemovingEachSecondPersonFromACircle;

import java.util.*;

public class CircleOfPeople {
    public static List<String> crossingOut(List<String> list) {
        if (list == null || list.isEmpty()) {
            return Collections.emptyList();
        }

        Queue<String> queue = new ArrayDeque<>(list);
        List<String> eliminatedPlayers = new ArrayList<>(list.size());

        while (queue.size() > 1) {
            queue.add(queue.poll());
            eliminatedPlayers.add(queue.poll());
        }

        return eliminatedPlayers;
    }

    public static void main(String[] args) {
        List<String> list = new ArrayList<>(Arrays.asList("Bob", "Lorna", "Desiree", "Melissa", "Josh"));

        // Expected Result: [Lorna, Melissa, Bob, Josh]
        System.out.println(crossingOut(list));
    }
}
