package main

import (
	"fmt"
	"strings"
)

type Node struct {
	value string
	left  *Node
	right *Node
}

func addNode(root, node *Node) {
	if root.value == node.value {
		root.left = node.left
		root.right = node.right
		return
	}

	if root.left != nil {
		addNode(root.left, node)
	}
	if root.right != nil {
		addNode(root.right, node)
	}
}

func findNode(root *Node, value string, travel *[]string) *[]string {
	if root == nil {
		return nil
	}

	if root.value == value {
		if len(*travel) == 0 {
			return &[]string{"Root"}
		}
		return travel
	}

	toLeft := append(*travel, "Left")
	res := findNode(root.left, value, &toLeft)
	if res != nil {
		return res
	}

	toRight := append(*travel, "Right")
	return findNode(root.right, value, &toRight)
}

func main() {
	var N int
	fmt.Scan(&N)

	var V string
	fmt.Scan(&V)

	var M int
	fmt.Scan(&M)

	nodes := make([]Node, N)
	for i := 0; i < M; i++ {
		var P, L, R string
		fmt.Scan(&P, &L, &R)

		nodes[i] = Node{P, &Node{L, nil, nil}, &Node{R, nil, nil}}
	}

	root := nodes[0]

	for idx := 1; idx < len(nodes); idx++ {
		addNode(&root, &nodes[idx])
	}

	travel := make([]string, 0)

	travel = *findNode(&root, V, &travel)

	fmt.Println(strings.Join(travel, " "))
}
