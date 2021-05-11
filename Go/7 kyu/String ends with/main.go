package main

import (
	"fmt"
	"strings"
)

func solution(str, ending string) bool {
	index := strings.LastIndex(str, ending)
	return index != -1
}

func main() {
	fmt.Println(solution("abc", "bc")) // returns true
	fmt.Println(solution("abc", "d"))  // returns false)
}
