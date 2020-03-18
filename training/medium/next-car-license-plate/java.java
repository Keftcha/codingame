import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String x = in.nextLine();
        String[] plaque = x.split("-");
        int[] plq = new int[5];
        plq[0] = (int) plaque[0].charAt(0);
        plq[1] = (int) plaque[0].charAt(1);
        plq[2] = Integer.parseInt(plaque[1]);
        plq[3] = (int) plaque[2].charAt(0);
        plq[4] = (int) plaque[2].charAt(1);

        int n = in.nextInt();

        if (n > 17558424) {
            int a = Math.floorDiv(n, 17558424);
            plq[0] += a;
            n -= a * 17558424;
        }

        if (n > 675324) {
            int a = Math.floorDiv(n, 675324);
            for (int idx = 0; idx < a; idx += 1) {
                plq[1] += 1;
                if (plq[1] > 90) {
                    plq[0] += 1;
                    plq[1] = 65;
                }
            }
            n -= a * 675324;
        }

        if (n > 25974) {
            int a = Math.floorDiv(n, 25974);
            for (int idx = 0; idx < a; idx += 1) {
                plq[3] += 1;
                if (plq[3] > 90) {
                    plq[1] += 1;
                    plq[3] = 65;
                }
            }
            n = n - a * 25974;
        }

        if (n > 999) {
            int a = Math.floorDiv(n, 999);
            for (int idx = 0; idx < a; idx += 1) {
                plq[4] += 1;
                if (plq[4] > 90) {
                    plq[3] += 1;
                    plq[4] = 65;
                }
            }
            n -= a * 999;
        }

        for (int idx = 0; idx < n; idx += 1) {
            plq[2] += 1;
            if (plq[2] > 999) {
                plq[4] += 1;
                plq[2] = 1;
            }
            if (plq[4] > 90) {
                plq[3] += 1;
                plq[4] = 65;
            }
            if (plq[3] > 90) {
                plq[2] += 1;
                plq[3] = 65;
            }
            if (plq[1] > 90) {
                plq[0] += 1;
                plq[1] = 65;
            }
        }

        System.out.println(
            String.format(
                "%s%s-%03d-%s%s",
                ((char) plq[0]),
                ((char) plq[1]),
                plq[2],
                ((char) plq[3]),
                ((char) plq[4])
            )
        );
    }
}
