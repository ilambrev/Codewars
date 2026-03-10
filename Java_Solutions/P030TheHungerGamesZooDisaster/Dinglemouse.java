package P030TheHungerGamesZooDisaster;

import java.util.*;

public class Dinglemouse {
    public static String[] whoEatsWho(final String zoo) {
        List<String> zooAsList = new ArrayList<>(Arrays.asList(zoo.split(",")));
        Map<String, Set<String>> animalsFood = animalsFoodInit();
        List<String> result = new ArrayList<>();
        result.add(zoo);

        int i = 0;

        while (i < zooAsList.size()) {
            String animal = zooAsList.get(i);

            if (i == 0 && i < zooAsList.size() - 1 && animalsFood.containsKey(animal) &&
                    animalsFood.get(animal).contains(zooAsList.get(i + 1))) {
                result.add(zooAsList.get(i) + " eats " + zooAsList.get(i + 1));
                zooAsList.remove(i + 1);
            } else if (i > 0 && animalsFood.containsKey(animal) && animalsFood.get(animal).contains(zooAsList.get(i - 1))) {
                result.add(zooAsList.get(i) + " eats " + zooAsList.get(i - 1));
                zooAsList.remove(i - 1);
                i = Math.max(i - 2, 0);
            } else if (i > 0 && i < zooAsList.size() - 1 && animalsFood.containsKey(animal) &&
                    animalsFood.get(animal).contains(zooAsList.get(i + 1))) {
                result.add(zooAsList.get(i) + " eats " + zooAsList.get(i + 1));
                zooAsList.remove(i + 1);
            } else {
                i++;
            }
        }

        result.add(String.join(",", zooAsList));

        return result.toArray(String[]::new);
    }

    private static Map<String, Set<String>> animalsFoodInit() {
        Map<String, Set<String>> animalsFood = new HashMap<>();
        animalsFood.put("antelope", new HashSet<>(List.of("grass")));
        animalsFood.put("big-fish", new HashSet<>(List.of("little-fish")));
        animalsFood.put("bug", new HashSet<>(List.of("leaves")));
        animalsFood.put("bear", new HashSet<>(List.of("big-fish", "bug", "chicken", "cow", "leaves", "sheep")));
        animalsFood.put("chicken", new HashSet<>(List.of("bug")));
        animalsFood.put("cow", new HashSet<>(List.of("grass")));
        animalsFood.put("fox", new HashSet<>(List.of("chicken", "sheep")));
        animalsFood.put("giraffe", new HashSet<>(List.of("leaves")));
        animalsFood.put("lion", new HashSet<>(List.of("antelope", "cow")));
        animalsFood.put("panda", new HashSet<>(List.of("leaves")));
        animalsFood.put("sheep", new HashSet<>(List.of("grass")));

        return animalsFood;
    }

    public static void main(String[] args) {
        String zoo = "fox,bug,chicken,grass,sheep";

        System.out.println(Arrays.toString(whoEatsWho(zoo)));
    }
}
