package P025RoundAndRound;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class RoundAndRound {
    public static double roundTo2DecimalPlaces(double number) {
        return BigDecimal.valueOf(number).setScale(2, RoundingMode.HALF_UP).doubleValue();
    }

    public static void main(String[] args) {
        // Expected Result: 2D
        System.out.println(roundTo2DecimalPlaces(2D));

        // Expected Result: 7.48D
        System.out.println(roundTo2DecimalPlaces(7.477D));

        // Expected Result: -5D
        System.out.println(roundTo2DecimalPlaces(-4.999D));

        // Expected Result: 18.12D
        System.out.println(roundTo2DecimalPlaces(18.123D));

        // Expected Result: 0D
        System.out.println(roundTo2DecimalPlaces(0D));

        // Expected Result: 1.46D
        System.out.println(roundTo2DecimalPlaces(1.455D));

        // Expected Result: -1.46D
        System.out.println(roundTo2DecimalPlaces(-1.455D));

        // Expected Result: 1.06D
        System.out.println(roundTo2DecimalPlaces(1.055D));

        // Expected Result: -1.06D
        System.out.println(roundTo2DecimalPlaces(-1.055D));

        // Expected Result: 16.77D
        System.out.println(roundTo2DecimalPlaces(16.765D));

        // Expected Result: -16.77D
        System.out.println(roundTo2DecimalPlaces(-16.765D));

        // Expected Result: 1.03D
        System.out.println(roundTo2DecimalPlaces(1.025D));

        // Expected Result: -1.03D
        System.out.println(roundTo2DecimalPlaces(-1.025D));

        // Expected Result: 16.36D
        System.out.println(roundTo2DecimalPlaces(16.355D));

        // Expected Result: -16.35D
        System.out.println(roundTo2DecimalPlaces(-16.345D));

        // Expected Result: -1.19D
        System.out.println(roundTo2DecimalPlaces(-1.1949999999999999D));

        // Expected Result: -1.20D
        System.out.println(roundTo2DecimalPlaces(-1.1950000000000001D));

        // Expected Result: 1.19D
        System.out.println(roundTo2DecimalPlaces(1.1949999999999999D));

        // Expected Result: 1.20D
        System.out.println(roundTo2DecimalPlaces(1.1950000000000001D));

        // Expected Result: -1.18D
        System.out.println(roundTo2DecimalPlaces(-1.1849999999999999D));

        // Expected Result: -1.19D
        System.out.println(roundTo2DecimalPlaces(-1.1850000000000001D));

        // Expected Result: 1.18D
        System.out.println(roundTo2DecimalPlaces(1.1849999999999999D));

        // Expected Result: 1.19D
        System.out.println(roundTo2DecimalPlaces(1.1850000000000001D));
    }
}
