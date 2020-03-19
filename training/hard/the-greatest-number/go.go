package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func contain(slc []string, str string) bool {
	for _, elem := range slc {
		if elem == str {
			return true
		}
	}
	return false
}

func reverse(slc []string) []string {
	slic := make([]string, len(slc))
	for idx, elem := range slc {
		slic[len(slc)-idx-1] = elem
	}
	return slic
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &N)

	scanner.Scan()
	input := strings.Split(scanner.Text(), " ")

	sort.Strings(input)

	if contain(input, "-") { // we want a negative number
		if contain(input, ".") { // place the dot
			input = []string{
				input[0],
				input[2],
				input[1],
				strings.Join(input[3:N], ""),
			}
		}
	} else { // we want a positive number
		input = reverse(input)
		if contain(input, ".") { // place the dot
			lastDigit := input[N-2]
			input = input[:N-2]
			if lastDigit != "0" { // at the end there is a 0, it's useless, we remove it
				input = append(input, ".", lastDigit)
			}
		}
	}

	number := fmt.Sprint(strings.Join(input, ""))
	if nb, _ := strconv.ParseFloat(number, 64); nb == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(number)
	}
}
