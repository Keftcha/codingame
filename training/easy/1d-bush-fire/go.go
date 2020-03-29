package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func quotientAndReminder(divident, divisor int) (quotient, reminder int) {
	reminder = divident % divisor
	quotient = (divident - reminder) / divisor
	return
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &N)

	for i := 0; i < N; i++ {
		scanner.Scan()
		line := strings.Split(scanner.Text(), "")
		waterDrops := 0

		for idx := 0; idx < len(line); idx += 1 {
			if line[idx] == "." {
				continue
			}
			// We are on a begin of a fire
			if line[idx] == "f" {
				// There tree fire (or two with the patterne f.f)
				if idx+2 < len(line) && line[idx+2] == "f" {
					waterDrops += 1
					idx += 2
				} else
				// There is two fire
				if idx+1 < len(line) && line[idx+1] == "f" {
					waterDrops += 1
					idx += 1
				} else {
					waterDrops += 1
				}
			}
		}
		fmt.Println(waterDrops)
	}
}
