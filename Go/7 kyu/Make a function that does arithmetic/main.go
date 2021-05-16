package main

func Arithmetic(a int, b int, operator string) int {
	res := 0
	switch operator {
	case "add":
		res = a + b
	case "subtract":
		res = a - b
	case "multiply":
		res = a * b
	case "divide":
		res = a / b
	}
	return res
}
