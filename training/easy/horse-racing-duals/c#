using System;

class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int[] puissance = new int[N];
        for (int i = 0; i < N; i++)
        {
            int pi = int.Parse(Console.ReadLine());
            puissance[i] = pi;
        }

        Array.Sort(puissance);
        int difference = 98;
        for (int idx = 0; idx < N - 1; idx += 1) {if (difference >
(Math.Abs(puissance[idx] - puissance[idx + 1]))) {difference =
Math.Abs(puissance[idx] - puissance[idx+1]);}}

        Console.WriteLine(difference);
    }
}
