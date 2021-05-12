package main

import "fmt"

func TwoSum(numbers []int, target int) [2]int {
	for i := range numbers {
		for j := range numbers {
			if i != j && numbers[i]+numbers[j] == target {
				return [2]int{i, j}
			}
		}
	}
	return [2]int{0, 0}
}

func main() {
	fmt.Println(TwoSum([]int{1, 2, 3}, 4) == [2]int{0, 2})
	fmt.Println(TwoSum([]int{1234, 5678, 9012}, 14690) == [2]int{1, 2})
	fmt.Println(TwoSum([]int{2, 2, 3}, 4) == [2]int{0, 1})
}
