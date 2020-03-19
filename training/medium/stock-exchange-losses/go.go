package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var n int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &n)

	pertes := 0
	vmax := -1
	vmin := -1

	scanner.Scan()
	inputs := strings.Split(scanner.Text(), " ")
	for i := 0; i < n; i++ {
		v, _ := strconv.Atoi(inputs[i])

		if vmax == -1 || vmax < v {
			vmax = v
			vmin = v
			continue
		}
		if vmin <= v {
			continue
		}
		vmin = v
		pertes = int(math.Min(float64(pertes), float64(vmin-vmax)))
	}

	fmt.Println(pertes)
}
