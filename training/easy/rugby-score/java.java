import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int score = in.nextInt();

        int nbEssais = 0;
        while (score >= nbEssais * 5){
            int nbTransformation = 0;
            while (score >= nbTransformation * 2) {
                int nbPenalite = 0;
                while (score >= nbPenalite) {
                    int reste = score - nbEssais * 5;
                    reste -= nbTransformation * 2;
                    reste -= nbPenalite * 3;
                    if (reste == 0 && nbEssais >= nbTransformation) {
                        System.out.println(String.format("%d %d %d", nbEssais, nbTransformation, nbPenalite));
                    }
                    nbPenalite += 1;
                }
                nbTransformation += 1;
            }
            nbEssais += 1;
        }
    }
}
