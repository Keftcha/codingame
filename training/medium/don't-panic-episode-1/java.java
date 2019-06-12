import java.util.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int nbFloors = in.nextInt(); // number of floors
        int width = in.nextInt(); // width of the area
        int nbRounds = in.nextInt(); // maximum number of rounds
        int exitFloor = in.nextInt(); // floor on which the exit is found
        int exitPos = in.nextInt(); // position of the exit on its floor
        int nbTotalClones = in.nextInt(); // number of generated clones
        int nbAdditionalElevators = in.nextInt(); // ignore (always zero)
        int nbElevators = in.nextInt(); // number of elevators
        Map<Integer, Integer> dico = new Hashtable<Integer, Integer>();
        for (int i = 0; i < nbElevators; i++) {
            int elevatorFloor = in.nextInt(); // floor on which this elevator is found
            int elevatorPos = in.nextInt(); // position of the elevator on its 
            dico.put(elevatorFloor, elevatorPos);
        }

        while (true) {
            Integer cloneFloor = in.nextInt(); // floor of the leading clone
            Integer clonePos = in.nextInt(); // position of the leading clone on its floor
            String direction = in.next(); // direction of the leading clone: LEFT or RIGHT
            
            Integer value = dico.get(cloneFloor);
            if (value == null){
                value = exitPos;
            }
            
            String instruction = new String();
            if ((clonePos > value && direction.equals("RIGHT")) || (clonePos < value && direction.equals("LEFT"))){
                instruction = "BLOCK";
            } else {
                instruction = "WAIT";
            }
            
            System.out.println(instruction); // action: WAIT or BLOCK
        }
    }
}
