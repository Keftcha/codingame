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
        int N = int.Parse(Console.ReadLine()); // Number of elements which make
up the association table.
        int Q = int.Parse(Console.ReadLine()); // Number Q of file names to be
analyzed.

        Dictionary<string, string> dico_types = new Dictionary<string,
string>();
        List<string> liste_fichiers = new List<string>();

        for (int i = 0; i < N; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            string EXT = inputs[0]; // file extension
            string MT = inputs[1]; // MIME type.

            dico_types.Add(EXT.ToLower(), MT);
        }


        for (int i = 0; i < Q; i++)
        {
            string FNAME = Console.ReadLine(); // One file name per line.
            liste_fichiers.Add(FNAME.ToLower());
        }

        List<string[]> new_list = new List<string[]>();
        for (int idx = 0; idx < liste_fichiers.Count; idx += 1)
        {
            string point = ".".ToString();
            string[] file = liste_fichiers[idx].Split('.');
            new_list.Add(file);
        }
        // On a la liste de tout les fichiers.

        foreach( string[] nom_fichier in new_list)
        {
        //Console.WriteLine(nom_fichier[nom_fichier.Count() - 1]);
            if (nom_fichier.Count() > 1)
            {
                if (dico_types.ContainsKey(nom_fichier[nom_fichier.Count()
-1])) Console.WriteLine(dico_types[nom_fichier[nom_fichier.Count() -1]]);
                else Console.WriteLine("UNKNOWN");
            }
            else Console.WriteLine("UNKNOWN");
        }

    }
}
