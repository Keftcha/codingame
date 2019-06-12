using System;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');
        int[] temp = new int[n];
        for (int i = 0; i < n; i++)
        {
            int t = int.Parse(inputs[i]);
            temp[i] = t;
        }

        if (n == 0) {Console.WriteLine(n);}
        else
        {
            int value = temp[0];
            for (int idx = 1; idx < n; idx += 1)
            {
                if (Math.Abs(value) == Math.Abs(temp[idx])) {value =
Math.Max(value, temp[idx]);}
                else if (Math.Abs(value) > Math.Abs(temp[idx])) {value =
temp[idx];}
            }
            Console.WriteLine(value);
        }
    }
}
