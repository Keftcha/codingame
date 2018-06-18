using System;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]); // number of columns.
        int H = int.Parse(inputs[1]); // number of rows.
        List<string[]> terrain = new List<string[]>();
        for (int i = 0; i < H; i++)
        {
            string LINE = Console.ReadLine();
            string[] line = LINE.Split(' ');
            terrain.Add(line);
        }
        int EX = int.Parse(Console.ReadLine());

        while (true)
        {
            inputs = Console.ReadLine().Split(' ');
            int XI = int.Parse(inputs[0]);
            int YI = int.Parse(inputs[1]);
            string pos = inputs[2];

            int x = XI;
            int y = YI;

            if ((string)terrain[y][x] == (string)"1" || (string)terrain[y][x]
== (string)"3" || (string)terrain[y][x] == (string)"7" || (string)terrain[y][x]
== (string)"8" || (string)terrain[y][x] == (string)"9" || (string)terrain[y][x]
== (string)"12" || (string)terrain[y][x] == (string)"13")
            {y += 1;}
            else if (pos == "TOP" && ((string)terrain[y][x] == (string)"4" ||
(string)terrain[y][x] == (string)"10"))
            {x -= 1;}
            else if (pos == "TOP" && ((string)terrain[y][x] == (string)"5" ||
(string)terrain[y][x] == (string)"11"))
            {x += 1;}
            else if (pos == "LEFT" && ((string)terrain[y][x] == (string)"2" ||
(string)terrain[y][x] == (string)"6"))
            {x += 1;}
            else if (pos == "LEFT" && ((string)terrain[y][x] == (string)"5"))
            {y += 1;}
            else if (pos == "RIGHT" && ((string)terrain[y][x] == (string)"2" ||
(string)terrain[y][x] == (string)"6"))
            {x -= 1;}
            else if (pos == "RIGHT" && ((string)terrain[y][x] == (string)"2" ||
(string)terrain[y][x] == (string)"6"))
            {x -= 1;}
            else if (pos == "RIGHT" && ((string)terrain [y][x] == (string)"4"))
            {y += 1;}

            Console.WriteLine(x + " " + y);
        }
    }
}
