package main

import "fmt"

func MultiplicationTable(size int) [][]int {
	arr2d := make([][]int, size)
	for i := range arr2d {
		arr2d[i] = make([]int, size)
	}

	for row := 0; row < size; row++ {
		for column := 0; column < size; column++ {
			arr2d[row][column] = (row + 1) * (column + 1)
		}
	}

	return arr2d
}

func main() {
	fmt.Println(MultiplicationTable(1))
	fmt.Println(MultiplicationTable(2))
	fmt.Println(MultiplicationTable(3))
}
