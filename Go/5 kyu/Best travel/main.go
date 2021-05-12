package main

import "fmt"

func ChooseBestSum(t, k int, ls []int) int {
	// TODO
	return 0
}

func main() {
	var ts = []int{50, 55, 56, 57, 58}
	fmt.Println(ChooseBestSum(163, 3, ts) == 163)

	ts = []int{50}
	fmt.Println(ChooseBestSum(163, 3, ts) == -1)

	ts = []int{91, 74, 73, 85, 73, 81, 87}
	fmt.Println(ChooseBestSum(230, 3, ts) == 228)
	fmt.Println(ChooseBestSum(331, 2, ts) == 178)
	fmt.Println(ChooseBestSum(331, 4, ts) == 331)
	fmt.Println(ChooseBestSum(331, 5, ts) == -1)
}
