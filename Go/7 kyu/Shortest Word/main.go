package main

import (
	"fmt"
	"strings"
)

func FindShort(s string) int {
	words := strings.Split(s, " ")
	min_len_of_words := len(words[0])
	for _, word := range words {
		if min_len_of_words > len(word) {
			min_len_of_words = len(word)
		}
	}
	return min_len_of_words
}

func main() {
	fmt.Println(FindShort("bitcoin take over the world maybe who knows perhaps") == 3)
	fmt.Println(FindShort("turns out random test cases are easier than writing out basic ones") == 3)
	fmt.Println(FindShort("Let's travel abroad shall we") == 2)
}
