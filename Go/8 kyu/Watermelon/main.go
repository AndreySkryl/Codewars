package main

import "fmt"

func Divide(weight int) bool {
	return weight >= 4 && weight%2 == 0
}

func main() {
	fmt.Println(Divide(2) == false) // # 2 = 1 + 1
	fmt.Println(Divide(3) == false) // # 3 = 1 + 2
	fmt.Println(Divide(4) == true)  // # 4 = 2 + 2
	fmt.Println(Divide(5) == false) // # 5 = 2 + 3
	fmt.Println(Divide(6) == true)  // # 6 = 2 + 4
}
