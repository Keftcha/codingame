import java.util.*;
import java.time.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        Duration duration = Duration.parse("PT24H60M60S");
        String[] drt = new String[]{};

        for (int i = 0; i < N; i++) {
            String[] t = in.next().split(":");
            Duration time = Duration.parse("PT"+t[0]+"H"+t[1]+"M"+t[2]+"S");
            int cmpr = duration.compareTo(time);
            if (cmpr > 0) {
                duration = time;
                drt = t;
            }
        }
        System.out.println(String.join(":", drt));
    }
}
