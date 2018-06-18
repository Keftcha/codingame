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
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]);
        int lightY = int.Parse(inputs[1]);
        int initialTX = int.Parse(inputs[2]);
        int initialTY = int.Parse(inputs[3]);
        int idx_x = 0;
        int idx_y = 0;

        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine());
            List<string> direction = new List<string>();
            int deplacement_x = Math.Abs(lightX - initialTX);
            int deplacement_y = Math.Abs(lightY - initialTY);

            if (idx_y < deplacement_y)
            {
                if (initialTY < lightY) direction.Add("S");
                if (initialTY > lightY) direction.Add("N");
                idx_y += 1;
            }
            if (idx_x < deplacement_x)
            {
                if (initialTX < lightX) direction.Add("E");
                if (initialTX > lightX) direction.Add("W");
                idx_x += 1;
            }

            Console.WriteLine(string.Join("", direction));
        }
    }
}
