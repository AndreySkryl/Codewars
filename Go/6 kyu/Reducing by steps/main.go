package main

import (
	"fmt"
	"math"
)

func Gcdi(x, y int) int {
	if x == 0 {
		return int(math.Abs(float64(y)))
	}
	return int(math.Abs(float64(Gcdi(y%x, x))))
}
func Som(x, y int) int {
	return x + y
}
func Maxi(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}
func Mini(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}
func Lcmu(x, y int) int {
	return int(math.Abs(float64((x * y) / Gcdi(x, y))))
}

type FParam func(int, int) int

func OperArray(f FParam, arr []int, init int) []int {
	result := []int{}
	current := init
	for _, elem := range arr {
		current = f(current, elem)
		result = append(result, current)
	}
	return result
}

func testEq(a, b []int) bool {
	// If one is nil, the other must also be nil.
	if (a == nil) != (b == nil) {
		return false
	}

	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func main() {
	var dta, sol = []int{}, []int{}
	fmt.Println("should handle basic cases gcdi")
	dta = []int{18, 69, -90, -78, 65, 40}
	sol = []int{18, 3, 3, 3, 1, 1}
	fmt.Println(testEq(OperArray(Gcdi, dta, dta[0]), sol))

	fmt.Println("should handle basic cases som")
	dta = []int{357, 112, 28, -52, 644, 119}
	sol = []int{357, 469, 497, 445, 1089, 1208}
	fmt.Println(testEq(OperArray(Som, dta, 0), sol))

	fmt.Println("should handle basic cases maxi")
	dta = []int{10, -32, 190, 300, -42, -38, 50, 405, -46, 225, -31}
	sol = []int{10, 10, 190, 300, 300, 300, 300, 405, 405, 405, 405}
	fmt.Println(testEq(OperArray(Maxi, dta, dta[0]), sol))

	fmt.Println("should handle basic cases lcmu")
	dta = []int{6, -72, -62, -22, -23, 80}
	sol = []int{6, 72, 2232, 24552, 564696, 5646960}
	fmt.Println(testEq(OperArray(Lcmu, dta, dta[0]), sol))

	fmt.Println("should handle basic cases mini")
	dta = []int{64, -67, -43, 12, -15, 108, 12, 104, -36}
	sol = []int{64, -67, -67, -67, -67, -67, -67, -67, -67}
	fmt.Println(testEq(OperArray(Mini, dta, dta[0]), sol))
}
