package main

import (
	"fmt"
	"strings"
)

func main() {
	var width, height int
	fmt.Scan(&width, &height)

	grid := make([][]string, 0, height)

	for i := 0; i < height; i++ {
		var line string
		fmt.Scan(&line)

		grid = append(grid, strings.Split(line, ""))
	}

	// count hash in each column
	hashNumbers := make([]int, 0, width)
	for x := 0; x < width; x += 1 {

		n := 0
		for y := 0; y < height; y += 1 {
			if grid[y][x] == "#" {
				n += 1
			}
		}
		hashNumbers = append(hashNumbers, n)
	}

	// display the new grid
	for y := 0; y < height; y += 1 {
		for x := 0; x < width; x += 1 {
			if height-hashNumbers[x] > y {
				fmt.Print(".")
			} else {
				fmt.Print("#")
			}
		}
		fmt.Println()
	}
}
