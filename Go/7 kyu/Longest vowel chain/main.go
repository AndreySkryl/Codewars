package main

import (
	"fmt"
	"sort"
	"strings"
)

func Solve(s string) int {
	vowels := strings.FieldsFunc(s, func(x rune) bool { return !strings.Contains("aeiou", string(x)) })
	sort.Slice(vowels, func(i, j int) bool { return len(vowels[i]) > len(vowels[j]) })
	return len(vowels[0])
}

func main() {
	fmt.Println(Solve("codewarriors") == 2)
	fmt.Println(Solve("suoidea") == 3)
	fmt.Println(Solve("ultrarevolutionariees") == 3)
	fmt.Println(Solve("strengthlessnesses") == 1)
	fmt.Println(Solve("cuboideonavicuare") == 2)
	fmt.Println(Solve("chrononhotonthuooaos") == 5)
	fmt.Println(Solve("iiihoovaeaaaoougjyaw") == 8)
}
