package main

import (
    "fmt"
    "sort"
)

type Sock struct {
	size  int
	color string
}

type Socks []Sock

func (s Sock) equal(sck Sock) bool {
	return s.size == sck.size && s.color == sck.color
}

func (s Sock) display() {
	fmt.Printf("%d %s\n", s.size, s.color)
}

func (s Sock) in(scks Socks) (bool, int) {
	for idx, sck := range scks {
		if sck.equal(s) {
			return true, idx
		}
	}
	return false, 0
}

func (s Socks) Len() int {
    return len(s)
}

func (s Socks) Less(a, b int) bool {
    i, j := s[a], s[b]
    // Sort by size
    if i.size < j.size {
        return true
    } else if j.size < i.size {
        return false
    } else { // The size is the same, we sort by color
        colors := []string{i.color, j.color}
        sort.Strings(colors)
        
        if i.color == colors[0] {
            return true
        } else {
            return false
        }
    }
}

func (s Socks) Swap(a, b int) {
    s[a], s[b] = s[b], s[a]
}

func main() {
	var n int
	fmt.Scan(&n)

	socks := make(Socks, 0)

	for i := 0; i < n; i++ {
		var clotheType string
		var clotheSize int
		var clotheColor string
		fmt.Scan(&clotheType, &clotheSize, &clotheColor)

		// Is this a sock
		if clotheType == "sock" {
			s := Sock{
				size:  clotheSize,
				color: clotheColor,
			}

			// We already have the sock
			if ok, idx := s.in(socks); ok {
				// remove the paired sock
				socks = append(socks[:idx], socks[idx+1:]...)
			} else {
				// add the new socke to the orphan socks list
				socks = append(socks, s)
			}
		}
	}

	fmt.Println(len(socks))
	sort.Sort(socks)
	for _, sck := range socks {
		sck.display()
	}
}
