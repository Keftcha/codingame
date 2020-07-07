package main

import (
	"fmt"
	"math"
)

func remove(slice []int, idx int) []int {
	return append(slice[:idx], slice[idx+1:]...)
}

func insertAt(idx int, elem int, slice []int) []int {
	tail := make([]int, len(slice[idx:]))
	copy(tail, slice[idx:])

	s := append(slice[:idx], elem)
	return append(s, tail...)
}

func main() {
	var L int
	fmt.Scan(&L)

	var N int
	fmt.Scan(&N)

	ranges := []int{0, L}

	for i := 0; i < N; i++ {
		var st, ed int
		fmt.Scan(&st, &ed)

		// Indexes of the start and end of painted section
		stIdx := -1
		edIdx := -1

		// Considere we are in a non painted section
		for idx := 0; idx+1 < len(ranges); idx++ {
			// Find the index of the start
			if (ranges[idx] < st && st < ranges[idx+1]) || ranges[idx+1] == st {
				stIdx = idx + 1
			} else if ranges[idx] == st {
				stIdx = idx
			}

			// Find the index of the end
			if (ranges[idx] < ed && ed < ranges[idx+1]) || ranges[idx+1] == ed {
				edIdx = idx + 1
			} else if ranges[idx] == ed {
				edIdx = idx
			}
		}

		// Adapt numbers idx when they aren't in the list
		if edIdx == -1 && stIdx != -1 {
			edIdx = len(ranges)
		}
		stIdx = int(math.Max(float64(stIdx), 0))

		// Delete numbers under the new painted section
		deleted := 0
		for stIdx < edIdx {
			ranges = remove(ranges, stIdx)
			deleted++
			edIdx--
		}

		// Remove the end of tha painted zone if it the beginning of an other painted zone
		if edIdx >= 0 && len(ranges) > 0 && ranges[edIdx] == ed {
			ranges = remove(ranges, edIdx)
			deleted++
		}

		// Insert the end and the start if needed
		// xxIdx%2 == 1 mean we are un a un-painted section
		stAdded := stIdx >= 0 && stIdx%2 == 1
		edAdded := edIdx >= 0 && ((!stAdded && edIdx%2 == 0 && deleted%2 == 1) || (stAdded && edIdx%2 == 1 && deleted%2 == 0))

		if edAdded {
			ranges = insertAt(edIdx, ed, ranges)
		}
		if stAdded {
			ranges = insertAt(stIdx, st, ranges)
		}
	}

	// Display result
	if len(ranges) == 0 {
		fmt.Println("All painted")
	} else {
		for idx := 0; idx < len(ranges); idx += 2 {
			fmt.Printf("%d %d\n", ranges[idx], ranges[idx+1])
		}
	}
}
