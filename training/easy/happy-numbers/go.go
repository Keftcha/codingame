package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func splitInt(nb string) []uint64 {
	strDigits := strings.Split(nb, "")

	digits := make([]uint64, len(strDigits))
	for idx, dig := range strDigits {
		digits[idx], _ = strconv.ParseUint(dig, 10, 64)
	}

	return digits
}

func calc(nbs []uint64) uint64 {
	var tot uint64 = 0

	for _, elem := range nbs {
		tot += elem * elem
	}

	return tot
}

func isHappy(nb string) bool {
	digits := splitInt(nb)
	tot := calc(digits)

	if tot == 1 || tot == 7 {
		return true
	} else if tot < 10 {
		return false
	} else {
		return isHappy(strconv.FormatUint(tot, 10))
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &N)

	for i := 0; i < N; i++ {
		scanner.Scan()
		x := scanner.Text()

		if isHappy(x) {
			fmt.Printf("%s :)\n", x)
		} else {
			fmt.Printf("%s :(\n", x)
		}
	}
}
