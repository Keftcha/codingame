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
        int index = 0;
        List<string> dictionaire = new List<string>();
        int N = int.Parse(Console.ReadLine());
        for (int i = 0; i < N; i++)
        {
            string W = Console.ReadLine();
            dictionaire.Add(W);
        }
        string lettres = Console.ReadLine();
        List<string> mots_possible = new List<string>();

        foreach (string mot in dictionaire)
        {
            List<char> liste = new List<char>();
            foreach (char chr in lettres) {liste.Add(chr);}
            bool pass = true;
            foreach (char lettre in mot)
            {
                if (liste.Contains(lettre))
                {
                    liste.Remove(lettre);
                    continue;
                }
                else
                {
                    pass = false;
                    break;
                }
            }
            if (pass) {mots_possible.Add(mot);}
        }

        int points = 0;
        List<string> mots = new List<string>();
        for (int idx = 0; idx < mots_possible.Count; idx += 1)
        {
            string mot = mots_possible[idx];
            int pts = 0;
            foreach (char lettre in mot)
            {
                List<char> liste1 = new List<char>() {'e', 'a', 'i', 'o', 'n',
'r', 't', 'l', 's', 'u'};
                if (liste1.Contains(lettre)) {pts += 1;}
                else if (new List<char>() {'d', 'g'}.Contains(lettre)) {pts +=
2;}
                else if (new List<char>() {'b', 'c', 'm',
'p'}.Contains(lettre)) {pts += 3;}
                else if (new List<char>() {'f', 'h', 'v', 'w',
'y'}.Contains(lettre)) {pts += 4;}
                else if (new List<char>() {'k'}.Contains(lettre)) {pts += 5;}
                else if (new List<char>() {'j', 'x'}.Contains(lettre)) {pts +=
8;}
                else if (new List<char>() {'q', 'z'}.Contains(lettre)) {pts +=
10;}
            }

            if (pts > points)
            {
                points = pts;
                index = idx;
            }
        }
        Console.WriteLine(mots_possible[index]);
    }
}
