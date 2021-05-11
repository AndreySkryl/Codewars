package main

import (
	"fmt"
	"strconv"
)

func PrinterError(s string) string {
	rune_s := []rune(s)
	count_of_errors := 0
	for i := range rune_s {
		if !(rune('a') <= rune_s[i] && rune_s[i] <= rune('m')) {
			count_of_errors++
		}
	}
	return strconv.Itoa(count_of_errors) + "/" + strconv.Itoa(len(rune_s))
}

func main() {
	s := "aaabbbbhaijjjm"
	fmt.Println(PrinterError(s)) // => "0/14"

	s = "aaaxbbbbyyhwawiwjjjwwm"
	fmt.Println(PrinterError(s)) // => "8/22"
}
