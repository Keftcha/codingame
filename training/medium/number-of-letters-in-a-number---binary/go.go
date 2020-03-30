package main

import (
	"fmt"
	"math"
)

func main() {
	var start, n int
	fmt.Scan(&start, &n)

	for idx := 0.0; idx < math.Min(float64(n), 6.0); idx += 1 {
		b := fmt.Sprintf("%b", start)

		start = 0
		for _, elem := range b {
			if elem == '1' {
				start += 3
			} else { // It's a zero
				start += 4
			}
		}
	}
	fmt.Println(start)
}
