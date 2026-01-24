package P020RotateArray;

import java.util.Arrays;

public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        int rotations = n % data.length;

        Object[] rotatedData = new Object[data.length];

        if (rotations == 0) {
            return data;
        } else if (n > 0) {
            System.arraycopy(data, data.length - rotations, rotatedData, 0, rotations);
            System.arraycopy(data, 0, rotatedData, rotations, data.length - rotations);
        } else {
            System.arraycopy(data, -rotations, rotatedData, 0, data.length + rotations);
            System.arraycopy(data, 0, rotatedData, rotatedData.length + rotations, -rotations);
        }

        return rotatedData;
    }

    public static void main(String[] args) {
        Rotator rotator = new Rotator();

        // Result: [5, 1, 2, 3, 4]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 1)));

        // Result: [4, 5, 1, 2, 3]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 2)));

        // Result: [3, 4, 5, 1, 2]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 3)));

        // Result: [2, 3, 4, 5, 1]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 4)));

        // Result: [1, 2, 3, 4, 5]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 5)));

        // Result: [5, 1, 2, 3, 4]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 6)));

        // Result: [2, 3, 4, 5, 1]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -1)));

        // Result: [3, 4, 5, 1, 2]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -2)));

        // Result: [4, 5, 1, 2, 3]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -3)));

        // Result: [5, 1, 2, 3, 4]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -4)));

        // Result: [1, 2, 3, 4, 5]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -5)));

        // Result: [2, 3, 4, 5, 1]
        System.out.println(Arrays.toString(rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -6)));
    }
}
