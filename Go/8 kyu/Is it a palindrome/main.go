package main

import (
	"fmt"
	"strings"
)

func reverse(str string) string {
	rune_str := []rune(str)
	var output strings.Builder
	for i := len(rune_str) - 1; i >= 0; i-- {
		output.WriteRune(rune_str[i])
	}

	return output.String()
}

func IsPalindrome(str string) bool {
	str = strings.ToLower(str)
	return str == reverse(str)
}

func main() {
	fmt.Println(IsPalindrome("a") == true)
	fmt.Println(IsPalindrome("aba") == true)
	fmt.Println(IsPalindrome("Abba") == true)
	fmt.Println(IsPalindrome("hello") == false)
}
