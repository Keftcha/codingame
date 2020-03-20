import java.util.*;

class Solution {

    static List<String> getLongestPalindromes(String src) {
        List<String> palindromes;
        int i = 0;
        
        do {
            palindromes = getLongestPalindromes(src, src.length() - i);
            i += 1;
        } while (palindromes.size() == 0);
        return palindromes;
    }
    
    static List<String> getLongestPalindromes(String src, int length) {
        List<String> palindromes = new ArrayList<String>();
        
        for (int i = 0; i < src.length() + 1 - length; i += 1) {
            if (isPalindrome(src, length, i)) {
                palindromes.add(src.substring(i, i + length));
            }
        }
        return palindromes;
    }
    
    static Boolean isPalindrome(String src, int length, int start) {
        for (int i = 0; i < length/2; i += 1) {
            if (src.charAt(start+i) != src.charAt(start + length - i - 1)) return false;
        }
        return true;
    }
    
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        List<String> longestPalindromes = getLongestPalindromes(s);
        
        for (String palin : longestPalindromes) {
            System.out.println(palin);
        }
    }
}
