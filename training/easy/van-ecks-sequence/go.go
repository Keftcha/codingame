package main

import "fmt"

func lastElem(nbs map[int]int) int {
	var lst int // Value of the last elem
	idx := 0    // Index of the last element

	// The key is the value in list, the value is the idx in list
	for key, value := range nbs {
		if idx <= value {
			lst, idx = key, value
		}
	}

	return lst
}

func main() {
	var A1 int
	fmt.Scan(&A1)

	var N int
	fmt.Scan(&N)

	// The key is the value in list, the value is the idx in list
	// Do that for performances
	numbers := map[int]int{}
	next := A1

	for idx := 0; idx < N; idx++ {
		// Check if the next number is present or not
		indexOfLast, present := numbers[next]

		// Add the next number, so the next change
		numbers[next] = idx

		// Find the next element
		if !present {
			next = 0
		} else {
			next = idx - indexOfLast
		}
	}

	fmt.Println(lastElem(numbers))
}
