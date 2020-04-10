package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	currentValue     int    // The food amount
	cummulativeValue int    // The cumulative amount of food from the 0 0 place
	position         [2]int // The X and Y position of the node
	childrens        []Node // Because we only can go down of right there is only two child
	parent           *Node  // This the parent node
}

func (n *Node) addChildrens(lake [][]int) int {
	var bottomNode Node
	if n.position[1]+1 < len(lake) { // The last line don't have bottom nodes
		bottomNode = Node{
			currentValue:     lake[n.position[1]+1][n.position[0]],
			cummulativeValue: n.cummulativeValue + lake[n.position[1]+1][n.position[0]],
			position:         [2]int{n.position[0], n.position[1] + 1},
			childrens:        []Node{},
			parent:           n,
		}
	}

	var rightNode Node
	if n.position[0]+1 < len(lake[0]) { // The last column don't have a right node
		rightNode = Node{
			currentValue:     lake[n.position[1]][n.position[0]+1],
			cummulativeValue: n.cummulativeValue + lake[n.position[1]][n.position[0]+1],
			position:         [2]int{n.position[0] + 1, n.position[1]},
			childrens:        []Node{},
			parent:           n,
		}
	}

	n.childrens = []Node{bottomNode, rightNode}

	if bottomNode.cummulativeValue < rightNode.cummulativeValue {
		return rightNode.cummulativeValue
	} else if bottomNode.cummulativeValue > rightNode.cummulativeValue {
		return bottomNode.cummulativeValue
	} else { // There is no child
		return n.cummulativeValue
	}
}

func (n *Node) recursivlyAddChildrens(lake [][]int) int {
	maxValue := n.addChildrens(lake)

	// Add childrens of our childrens
	for _, child := range n.childrens {
		if child.currentValue != 0 {
			if value := child.recursivlyAddChildrens(lake); maxValue < value {
				maxValue = value
			}
		}
	}
	return maxValue
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	var W, H int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &W, &H)

	lake := make([][]int, H)
	for i := 0; i < H; i++ {
		scanner.Scan()
		inputs := strings.Split(scanner.Text(), " ")

		line := make([]int, W)
		for j := 0; j < W; j++ {
			food, _ := strconv.Atoi(inputs[j])
			line[j] = food
		}
		lake[i] = line
	}

	root := Node{
		currentValue:     lake[0][0],
		cummulativeValue: lake[0][0],
		position:         [2]int{0, 0},
		childrens:        []Node{},
		parent:           nil,
	}

	// Build tree and return the maximum cummulative value
	// when building to don't travail again the tree
	maxFoodAmount := root.recursivlyAddChildrens(lake)

	fmt.Println(maxFoodAmount)
}
