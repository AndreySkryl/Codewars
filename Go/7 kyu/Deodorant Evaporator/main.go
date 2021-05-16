package main

import "fmt"

func Evaporator(content float64, evapPerDay int, threshold int) int {
	dayNumber := 0
	currentContent := content
	limitOfUnsedContent := content * (float64(threshold) / float64(100))
	for currentContent > limitOfUnsedContent {
		currentContent = (float64(1) - float64(evapPerDay)/float64(100)) * currentContent
		dayNumber++
	}
	return dayNumber
}

func main() {
	fmt.Println(Evaporator(10, 10, 10) == 22)
	fmt.Println(Evaporator(10, 10, 5) == 29)
	fmt.Println(Evaporator(100, 5, 5) == 59)
}
