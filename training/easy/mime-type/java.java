import java.util.*;

class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // Number of elements which make up the association table.
        int Q = in.nextInt(); // Number Q of file names to be analyzed.

        Map<String, String> mime = new HashMap<String, String>();

        for (int i = 0; i < N; i++) {
            String EXT = in.next(); // file extension
            String MT = in.next(); // MIME type.
            mime.put(EXT.toLowerCase(), MT);
        }
        in.nextLine();
        for (int i = 0; i < Q; i++) {
            String FNAME = in.nextLine(); // One file name per line.
            String[] splt_file = FNAME.split("\\.", -1);
            String ext = splt_file[splt_file.length-1].toLowerCase();

            System.out.println(
                mime.containsKey(ext) && splt_file.length > 1 ? mime.get(ext) : "UNKNOWN"
            );
        }
    }
}
