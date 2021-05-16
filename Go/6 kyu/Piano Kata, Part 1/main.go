package main

import "fmt"

func BlackOrWhiteKey(keyPressCount int) string {
	// TODO
	if keyPressCount > 88 {
		keyPressCount = keyPressCount % 88
	}

	str := "wbwwbwbwwbwb"
	keyPressCount = (keyPressCount - 1) % len(str)
	if str[keyPressCount] == 'w' {
		return "white"
	}
	return "black"
}

func main() {
	fmt.Println(1, BlackOrWhiteKey(1) == ("white"))
	fmt.Println(5, BlackOrWhiteKey(5) == ("black"))
	fmt.Println(12, BlackOrWhiteKey(12) == ("black"))
	fmt.Println(42, BlackOrWhiteKey(42) == ("white"))
	fmt.Println(88, BlackOrWhiteKey(88) == ("white"))
	fmt.Println(89, BlackOrWhiteKey(89) == ("white"))
	fmt.Println(92, BlackOrWhiteKey(92) == ("white"))
	fmt.Println(100, BlackOrWhiteKey(100) == ("black"))
	fmt.Println(111, BlackOrWhiteKey(111) == ("white"))
	fmt.Println(200, BlackOrWhiteKey(200) == ("black"))
	fmt.Println(2017, BlackOrWhiteKey(2017) == ("white"))
}
