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

	var L int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &L)

	var H int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &H)

	scanner.Scan()
	T := strings.ToLower(scanner.Text())

	for i := 0; i < H; i++ {
		scanner.Scan()
		ROW := scanner.Text()
		for _, letter := range T {
			idx := int(letter) - 97
			if idx < 0 || 25 < idx {
				idx = 26
			}

			fmt.Print(ROW[idx*L : (idx+1)*L])
		}
		fmt.Println()
	}
}
