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

        Dictionary<int, int> dico = new Dictionary<int, int>();

        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int nbFloors = int.Parse(inputs[0]); // number of floors
        int width = int.Parse(inputs[1]); // width of the area
        int nbRounds = int.Parse(inputs[2]); // maximum number of rounds
        int exitFloor = int.Parse(inputs[3]); // floor on which the exit is
found
        int exitPos = int.Parse(inputs[4]); // position of the exit on its
floor
        int nbTotalClones = int.Parse(inputs[5]); // number of generated clones
        int nbAdditionalElevators = int.Parse(inputs[6]); // ignore (always
zero)
        int nbElevators = int.Parse(inputs[7]); // number of elevators
        for (int i = 0; i < nbElevators; i++)
        {
            inputs = Console.ReadLine().Split(' ');
            int elevatorFloor = int.Parse(inputs[0]); // floor on which this
elevator is found
            int elevatorPos = int.Parse(inputs[1]); // position of the elevator
on its floor
            dico[elevatorFloor] = elevatorPos;
        }

        while (true)
        {
            inputs = Console.ReadLine().Split(' ');
            int cloneFloor = int.Parse(inputs[0]); // floor of the leading
clone
            int clonePos = int.Parse(inputs[1]); // position of the leading
clone on its floor
            string direction = inputs[2]; // direction of the leading clone:
LEFT or RIGHT

            int valeur;
            valeur = exitPos;
            if (dico.ContainsKey(cloneFloor)) {valeur = dico[cloneFloor];}

            string instruction = "WAIT";
            if ((clonePos < valeur && direction == "LEFT") || (clonePos >
valeur && direction == "RIGHT")) instruction = "BLOCK";

            Console.WriteLine(instruction); // action: WAIT or BLOCK
        }
    }
}
