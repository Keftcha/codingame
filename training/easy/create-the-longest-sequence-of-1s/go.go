package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	scanner.Scan()
	var b []string = strings.Split(scanner.Text(), "0")

	maxOne := 1
	for idx := 0; idx+1 < len(b); idx += 1 {
		if length := len(b[idx]) + len(b[idx+1]) + 1; maxOne < length {
			maxOne = length
		}
	}

	fmt.Println(maxOne)
}
