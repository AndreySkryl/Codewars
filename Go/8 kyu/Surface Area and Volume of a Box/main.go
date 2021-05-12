package main

import "fmt"

func GetSize(w, h, d int) [2]int {
	return [2]int{2*w*h + 2*w*d + 2*h*d, w * h * d}
}

func main() {
	fmt.Println(GetSize(4, 2, 6) == [2]int{88, 48})
	fmt.Println(GetSize(1, 1, 1) == [2]int{6, 1})
	fmt.Println(GetSize(1, 2, 1) == [2]int{10, 2})
	fmt.Println(GetSize(1, 2, 2) == [2]int{16, 4})
	fmt.Println(GetSize(10, 10, 10) == [2]int{600, 1000})
}
