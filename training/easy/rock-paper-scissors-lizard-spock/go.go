package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Player struct {
	number        int
	sign          string
	opponentsName []string
}

func battle(p1, p2 Player) Player {
	// Add opponent
	p1.opponentsName = append(p1.opponentsName, strconv.Itoa(p2.number))
	p2.opponentsName = append(p2.opponentsName, strconv.Itoa(p1.number))

	// Find the winner
	if p1.sign == "C" && p2.sign == "P" ||
		p1.sign == "P" && p2.sign == "R" ||
		p1.sign == "R" && p2.sign == "L" ||
		p1.sign == "L" && p2.sign == "S" ||
		p1.sign == "S" && p2.sign == "C" ||
		p1.sign == "C" && p2.sign == "L" ||
		p1.sign == "L" && p2.sign == "P" ||
		p1.sign == "P" && p2.sign == "S" ||
		p1.sign == "S" && p2.sign == "R" ||
		p1.sign == "R" && p2.sign == "C" ||
		// They played the same sign
		p1.sign == p2.sign && p1.number < p2.number {
		return p1
	} else {
		return p2
	}
}

func main() {
	var N int
	fmt.Scan(&N)

	players := make([]Player, N)
	for i := 0; i < N; i++ {
		var NUMPLAYER int
		var SIGNPLAYER string
		fmt.Scan(&NUMPLAYER, &SIGNPLAYER)

		players[i] = Player{number: NUMPLAYER, sign: SIGNPLAYER}
	}

	// Looking for a winner
	for len(players) > 1 {
		// Play a round
		nextRoundPlayers := make([]Player, len(players)/2)
		for idx := 0; idx < len(players); idx += 2 {
			p1, p2 := players[idx], players[idx+1]
			winner := battle(p1, p2)

			nextRoundPlayers[idx/2] = winner
		}
		players = nextRoundPlayers
	}

	winner := players[0]

	fmt.Println(winner.number)
	fmt.Println(strings.Join(winner.opponentsName, " "))
}
