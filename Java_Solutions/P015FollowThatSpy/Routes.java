import java.util.*;

public class Routes {

    public String findRoutes(String[][] routes) {
        Map<String, String> routesMap = new HashMap<>();
        List<String> spyRoute = new ArrayList<>();

        for (String[] route : routes) {
            routesMap.put(route[0], route[1]);
        }

        Set<String> endPoints = new HashSet<>(routesMap.values());

        String startPoint = "";

        for (String point : routesMap.keySet()) {
            if (!endPoints.contains(point)) {
                startPoint = point;
                break;
            }
        }

        spyRoute.add(startPoint);

        for (int i = 0; i < routes.length; i++) {
            String nextPoint = routesMap.get(startPoint);
            spyRoute.add(nextPoint);
            startPoint = nextPoint;
        }

        return String.join(", ", spyRoute);
    }
}