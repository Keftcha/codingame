import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        String[] input = in.nextLine().split(" ");
        Arrays.sort(input);
        
        if (Arrays.asList(input).contains("-")) {
            if (Arrays.asList(input).contains(".")) {
                input = new String[] {
                    input[0],
                    input[2],
                    ".",
                    String.join("", Arrays.copyOfRange(input, 3, input.length-1)),
                    input[input.length-1]
                };
            }
        } else {
            Collections.reverse(Arrays.asList(input));
            if (Arrays.asList(input).contains(".")) {
                String lastDigit = input[input.length-2];
                input = new String[] {
                    String.join("", Arrays.copyOfRange(input, 0, input.length-2)),
                };
                if (!lastDigit.equals("0")) {
                    input = new String[] {
                        String.join("", input),
                        ".",
                        lastDigit
                    };
                }
            }
        }
        String number = String.join("", input);
        System.out.println(Float.parseFloat(number) == 0 ? 0 : number);
    }
}
