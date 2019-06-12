import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        List<Integer> temps = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
            temps.add(t);
        }
        
        if (n > 0) {
            int closest = temps.get(0);
            for (int idx = 1; idx < temps.size(); idx += 1) {
                if (Math.abs(closest) == Math.abs(temps.get(idx))) {
                    closest = Math.max(closest, temps.get(idx));
                } else if (Math.abs(closest) > Math.abs(temps.get(idx))) {
                    closest = temps.get(idx);
                }
            }
            System.out.println(closest);
        } else {
            System.out.println(n);
        }
    }
}
