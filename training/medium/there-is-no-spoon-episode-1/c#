using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        int width = int.Parse(Console.ReadLine()); // the number of cells on
the X axis
        int height = int.Parse(Console.ReadLine()); // the number of cells on
the Y axis
        string[] grille = new string[height];
        for (int i = 0; i < height; i++)
        {
            string line = Console.ReadLine(); // width characters, each either
0 or .
            grille[i] = line;
        }

        int colone = 0;
        int ligne = 0;
        int nb_colone = width;
        int nb_ligne = height;

        List<Tuple<int, int>> liste_neuds = new List<Tuple<int, int>>();

        for (int nb = 0; nb < nb_ligne; nb += 1)
        {
            for (int nombre = 0; nombre < nb_colone; nombre += 1)
            {
                if (grille[nb][nombre] == "0"[0]) {liste_neuds.Add(new
Tuple<int, int>(nombre, nb));}
            }
        }

        string affiche = null;
        for (int idx = 0; idx < liste_neuds.Count; idx += 1)
        {
            affiche = "";
            Tuple<int, int> neud = liste_neuds[idx];
            affiche += neud.Item1;
            affiche += " " + neud.Item2;

            int index = idx + 1;
            bool pass = true;
            while (index < liste_neuds.Count)
            {
                if (neud.Item2 == liste_neuds[index].Item2)
                {
                    affiche += " " + liste_neuds[index].Item1;
                    affiche += " " + liste_neuds[index].Item2;
                    pass = false;
                    break;
                }
                index += 1;
            }
            if (pass) {affiche += " -1 -1";}

            int index2 = idx + 1;
            bool pass2 = true;
            while (index2 < liste_neuds.Count)
            {
                if (neud.Item1 == liste_neuds[index2].Item1)
                {
                    affiche += " " + liste_neuds[index2].Item1;
                    affiche += " " + liste_neuds[index2].Item2;
                    pass2 = false;
                    break;
                }
                index2 += 1;
            }
            if (pass2) {affiche += " -1 -1";}

            Console.WriteLine(affiche);
        }
    }
}
