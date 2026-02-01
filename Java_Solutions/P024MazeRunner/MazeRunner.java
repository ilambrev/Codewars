package P024MazeRunner;

public class MazeRunner {
    private static final int SAFE_PLACE_TO_WALK = 0;
    private static final int WALL = 1;
    private static final int START_POINT = 2;
    private static final int FINISH_POINT = 3;

    public static String walk(int[][] maze, String[] directions) {
        int[] startPointCoordinates = findPointCoordinates(maze, START_POINT);

        int row = startPointCoordinates[0];
        int col = startPointCoordinates[1];

        for (String direction : directions) {
            switch (direction) {
                case "N" -> row--;
                case "E" -> col++;
                case "W" -> col--;
                case "S" -> row++;
            }

            if (row < 0 || row > maze.length - 1 || col < 0 || col > maze[0].length - 1) {
                return "Dead";
            }

            if (maze[row][col] == SAFE_PLACE_TO_WALK) {
                continue;
            }

            if (maze[row][col] == FINISH_POINT) {
                return "Finish";
            }

            if (maze[row][col] == WALL) {
                return "Dead";
            }
        }

        return "Lost";
    }

    public static int[] findPointCoordinates(int[][] maze, int pointValue) {
        int[] pointCoordinates = {-1, -1};

        for (int i = 0; i < maze.length; i++) {
            for (int j = 0; j < maze[i].length; j++) {
                if (maze[i][j] == pointValue) {
                    return new int[]{i, j};
                }
            }
        }

        return pointCoordinates;
    }

    public static void main(String[] args) {
        int[][] maze = {
                {1, 1, 1, 1, 1, 1, 1},
                {1, 0, 0, 0, 0, 0, 3},
                {1, 0, 1, 0, 1, 0, 1},
                {0, 0, 1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1, 0, 1},
                {1, 0, 0, 0, 0, 0, 1},
                {1, 2, 1, 0, 1, 0, 1}};

        // Expected Result: "Finish"
        String[] directions1 = {"N", "N", "N", "N", "N", "E", "E", "E", "E", "E"};

        // Expected Result: "Finish"
        String[] directions2 = {"N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"};

        // Expected Result: "Finish"
        String[] directions3 = {"N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"};

        // Expected Result: "Dead"
        String[] directions4 = {"N", "N", "N", "W", "W"};

        // Expected Result: "Dead"
        String[] directions5 = {"N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"};

        // Expected Result: "Lost"
        String[] directions6 = {"N", "E", "E", "E", "E"};

        System.out.println(walk(maze, directions1));
        System.out.println(walk(maze, directions2));
        System.out.println(walk(maze, directions3));
        System.out.println(walk(maze, directions4));
        System.out.println(walk(maze, directions5));
        System.out.println(walk(maze, directions6));
    }
}
