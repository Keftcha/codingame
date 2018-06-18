using System;
class Solution
{
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string T = Console.ReadLine().ToUpper();

        string ROW = null;

        for (int i = 0; i < H; i++)
        {
            ROW = Console.ReadLine();
            foreach (char lettre in T)
            {
                int code = lettre - 65;
                if (code < 0 || code > 25) {code = 26;}
                for (int idx = 0; idx < L; idx += 1)
                {
                    Console.Write(ROW[(code * L) + idx]);
                }
            }
            Console.WriteLine();
        }
    }
}
