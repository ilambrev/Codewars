package P023IPAddressToNumber;

public class IpTranslator {
    public static long ipToNum(String ip) {
        String[] octets = ip.split("\\.");
        StringBuilder sb = new StringBuilder();
        for (String octet : octets) {
            String binaryOctet = Integer.toBinaryString(Integer.parseInt(octet));
            if (binaryOctet.length() < 8) {
                sb.append("0".repeat(8 - binaryOctet.length()));
            }
            sb.append(binaryOctet);
        }

        return Long.parseLong(sb.toString(), 2);
    }

    public static String numToIp(long num) {
        String binaryString = Long.toBinaryString(num);
        if (binaryString.length() < 32) {
            binaryString = "0".repeat(32 - binaryString.length()) + binaryString;
        }
        String[] octets = new String[4];
        for (int i = 0; i < 4; i++) {
            octets[i] = String.valueOf(Integer.parseInt(binaryString.substring(i * 8, i * 8 + 8), 2));
        }

        return String.join(".", octets);
    }

    public static void main(String[] args) {
        String ip1 = "192.168.1.1";
        String ip2 = "10.0.0.0";
        String ip3 = "176.16.0.1";
        String ip4 = "255.255.255.255";
        String ip5 = "0.0.0.0";
        String ip6 = "0.152.13.172";

        // Expected Result: 3232235777L
        System.out.println(ipToNum(ip1));

        // Expected Result: 167772160L
        System.out.println(ipToNum(ip2));

        // Expected Result: 2953838593L
        System.out.println(ipToNum(ip3));

        // Expected Result: (1L << 32) - 1
        System.out.println(ipToNum(ip4));

        // Expected Result: 0L
        System.out.println(ipToNum(ip5));

        // Expected Result: 9964972L
        System.out.println(ipToNum(ip6));

        long num1 = 3232235777L;
        long num2 = 167772160L;
        long num3 = 2953838593L;
        long num4 = 0L;
        long num5 = (1L << 32) - 1;
        long num6 = 9964972L;

        // Expected Result: "192.168.1.1"
        System.out.println(numToIp(num1));

        // Expected Result: "10.0.0.0"
        System.out.println(numToIp(num2));

        // Expected Result: "176.16.0.1"
        System.out.println(numToIp(num3));

        // Expected Result: "0.0.0.0"
        System.out.println(numToIp(num4));

        // Expected Result: "255.255.255.255"
        System.out.println(numToIp(num5));

        // Expected Result: "0.152.13.172"
        System.out.println(numToIp(num6));
    }
}
