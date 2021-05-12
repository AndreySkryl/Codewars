package main

import "fmt"

func WordsToMarks(s string) int {
	res := 0
	for _, c := range s {
		res += int(c) - int('a') + 1
	}
	return res
}

func main() {
	fmt.Println(WordsToMarks("attitude") == 100)
	fmt.Println(WordsToMarks("friends") == 75)
	fmt.Println(WordsToMarks("family") == 66)
	fmt.Println(WordsToMarks("selfness") == 99)
	fmt.Println(WordsToMarks("knowledge") == 96)
}
