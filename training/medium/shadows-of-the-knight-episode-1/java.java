import java.util.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int[] batman = new int[]{in.nextInt(), in.nextInt()};
        int[][] bombInterval = new int[][]{{0, W}, {0, H}};


        while (true) {
            String bombDir = in.next();

            if (bombDir.contains("U")) {
                bombInterval[1][1] = batman[1] - 1;
            } else if (bombDir.contains("D")) {
                bombInterval[1][0] = batman[1] + 1;
            }

            if (bombDir.contains("R")) {
                bombInterval[0][0] = batman[0] + 1;
            } else if (bombDir.contains("L")) {
                bombInterval[0][1] = batman[0] - 1;
            }

            batman = new int[]{
                bombInterval[0][0] + Math.round(
                    (bombInterval[0][1] - bombInterval[0][0]) / 2
                ),
                bombInterval[1][0] + Math.round(
                    (bombInterval[1][1] - bombInterval[1][0]) / 2
                )
            };

            System.out.println(String.format("%d %d", batman[0], batman[1]));
        }
    }
}
