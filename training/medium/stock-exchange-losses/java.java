import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        int pertes = 0;
        int vmax = -1;
        int vmin = -1;
        
        for (int i = 0; i < n; i++) {
            int v = in.nextInt();
            
            if (vmax == -1 || vmax < v) {
                vmax = v;
                vmin = v;
                continue;
            }
            if (vmin <= v){continue;}
            vmin = v;
            pertes = Math.min(pertes, vmin - vmax);
        }

        System.out.println(pertes);
    }
}
