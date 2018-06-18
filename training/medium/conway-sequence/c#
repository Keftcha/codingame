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
        int r = int.Parse(Console.ReadLine());
        int l = int.Parse(Console.ReadLine());

        List<string> liste = new List<string>();
        liste.Add(r.ToString());

        for (int idx = 1; idx < l; idx += 1)
        {
            List<string> liste_suivante = new List<string>();
            int pr = 0;
            int pb = 0;
            while (pb < liste.Count)
            {
                while (pr < liste.Count && liste[pr] == liste[pb]) {pr += 1;}
                liste_suivante.Add((pr - pb).ToString());
                liste_suivante.Add(liste[pb].ToString());
                pb = pr;
            }
            liste = liste_suivante;
        }
        Console.WriteLine(String.Join(" ", liste));
    }
}
