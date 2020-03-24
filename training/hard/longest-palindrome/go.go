package main

import (
	"fmt"
	"strings"
)

func isPalin(str []string, b, e int) bool {
	for ; b < e; b, e = b+1, e-1 {
		if str[b] != str[e] {
			return false
		}
	}
	return true
}

func palinsMaxLength(str []string) [][2]int {
	var palinsIdx [][2]int

	sub := 0
	for ; len(palinsIdx) == 0; sub += 1 {
		palinsIdx = findPalins(str, len(str)-sub)
	}
	return palinsIdx
}

func findPalins(str []string, length int) [][2]int {
	palinsIdx := make([][2]int, 0)

	for idx := 0; idx+length-1 < len(str); idx += 1 {
		if isPalin(str, idx, idx+length-1) {
			palinsIdx = append(palinsIdx, [2]int{idx, idx + length})
		}
	}
	return palinsIdx
}

func main() {
	var s string
	fmt.Scan(&s)
	str := strings.Split(s, "")

	for _, elem := range palinsMaxLength(str) {
		fmt.Println(strings.Join(str[elem[0]:elem[1]], ""))
	}
}
