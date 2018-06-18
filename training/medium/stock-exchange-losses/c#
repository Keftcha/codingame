using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');
        int[] valeur = new int[n];
        for (int i = 0; i < n; i++)
        {
            int v = int.Parse(inputs[i]);
            valeur[i] = v;
        }

        int pertes = 0;
        int vmax = -1;
        int vmin = -1;

        foreach (int nb in valeur)
        {
            if (vmax == -1 || vmax < nb)
            {
                vmax = nb;
                vmin = nb;
                continue;
            }
            if (vmin <= nb) {continue;}
            vmin = nb;
            int diff = vmin - vmax;
            if (diff < pertes) {pertes = diff;}
        }

        Console.WriteLine(pertes);
    }
}
