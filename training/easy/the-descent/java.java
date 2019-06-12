import java.util.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        

        while (true) {
            List<Integer> mountains = new ArrayList<Integer>();
            
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                mountains.add(mountainH);
            }

            Integer max = Collections.max(mountains);

            System.out.println(mountains.indexOf(max)); // The index of the mountain to fire on.
        }
    }
}
