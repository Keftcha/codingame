package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	up         = [2]int{0, -1} // Going up mean decrement x
	down       = [2]int{0, 1}  // Going down mean increment x
	left       = [2]int{-1, 0} // Going left mean decrement y
	right      = [2]int{1, 0}  // Going right mean increment y
	directions = [4][2]int{up, right, down, left}
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var w, h int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &w, &h)

	var n int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &n)

	// Wall bricks coordinates (use key of map as a set, value will be the rune)
	walls := make(map[[2]int]rune)
	// Default robot direction is up (index 0 in the directions list)
	robotDirection := 0
	// The robot place
	var robotPlace [2]int

	// May the robot will do loop
	var robotLoopInitPlace [2]int
	loopLength := 0
	justInitializedLoop := false

	for i := 0; i < h; i++ {
		scanner.Scan()
		line := scanner.Text()

		for idx, char := range line {
			// Save wall location
			if char == rune('#') {
				walls[[2]int{idx, i}] = char
			}
			// Robot initiale place
			if char == rune('O') {
				robotPlace[0], robotPlace[1] = idx, i
			}
		}
	}

	for ; n > 0; n-- {
		// The robot next place, we must check this place
		nextRobotPlace := [2]int{
			robotPlace[0] + directions[robotDirection][0],
			robotPlace[1] + directions[robotDirection][1],
		}

		// Check if there is a wall in front of the robot
		_, wallAhead := walls[nextRobotPlace]
		// Check if the robot is still on the fiels
		inField := 0 <= nextRobotPlace[0] && nextRobotPlace[0] < w && 0 <= nextRobotPlace[1] && nextRobotPlace[1] < h

		// Increment the loopLength each step
		loopLength++

		// If there is a border or there is a wall, we need to turn right
		if wallAhead || !inField {
			// Start the robot loop at the first wall encounter
			if robotLoopInitPlace == [2]int{} {
				robotLoopInitPlace[0] = robotPlace[0]
				robotLoopInitPlace[1] = robotPlace[1]
				// Re-initialize the loopLenght
				loopLength = 1
				// Precize we just initialise the loop
				justInitializedLoop = true
			} else {
				justInitializedLoop = false
			}

			robotDirection++
			robotDirection %= len(directions)
		}

		// The new robot real place
		robotPlace[0] = robotPlace[0] + directions[robotDirection][0]
		robotPlace[1] = robotPlace[1] + directions[robotDirection][1]

		// Check if the robot have made a loop
		if robotPlace == robotLoopInitPlace && !justInitializedLoop {
			n %= loopLength
		}

	}
	fmt.Printf("%d %d", robotPlace[0], robotPlace[1])
}
