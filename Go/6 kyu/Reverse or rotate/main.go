package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func getChunks(s string, sz int) []string {
	chunks := make([]string, 0)
	for i := 0; i < len(s); i += sz {
		chunk := strings.Builder{}
		for k := 0; k < sz && i+k < len(s); k++ {
			chunk.WriteString(string(s[i+k]))
		}
		if len(chunk.String()) == sz {
			chunks = append(chunks, chunk.String())
		}
	}
	return chunks
}

func reverse(chunk string) string {
	reversedChunk := strings.Builder{}
	for i := len(chunk) - 1; i >= 0; i-- {
		reversedChunk.WriteString(string(chunk[i]))
	}
	return reversedChunk.String()
}

func rotateOnLeft(chunk string, step int) string {
	return chunk[step:] + chunk[:step]
}

func isSumOfTheCubesOfDigitsIsDivisibleBy2(digits string) bool {
	var summa int
	for _, digit := range digits {
		iDigit, _ := strconv.Atoi(string(digit))
		summa += int(math.Pow(float64(iDigit), 3))
	}
	return summa%2 == 0
}

func getModifiedChunks(chunks []string) []string {
	modifiedChunks := make([]string, len(chunks))
	for _, chunk := range chunks {
		if isSumOfTheCubesOfDigitsIsDivisibleBy2(chunk) {
			modifiedChunks = append(modifiedChunks, reverse(chunk))
		} else {
			modifiedChunks = append(modifiedChunks, rotateOnLeft(chunk, 1))
		}
	}
	return modifiedChunks
}

func Revrot(s string, sz int) string {
	if sz <= 0 || len(s) == 0 || len(s) < sz {
		return ""
	}

	chunks := getChunks(s, sz)
	modifiedChunks := getModifiedChunks(chunks)
	return strings.Join(modifiedChunks, "")
}

func main() {
	fmt.Println(Revrot("123456987654", 6) == "234561876549")
	fmt.Println(Revrot("123456987653", 6) == "234561356789")
	fmt.Println(Revrot("66443875", 4) == "44668753")
	fmt.Println(Revrot("66443875", 8) == "64438756")
	fmt.Println(Revrot("664438769", 8) == "67834466")
	fmt.Println(Revrot("123456779", 8) == "23456771")
	fmt.Println(Revrot("", 8) == "")
	fmt.Println(Revrot("123456779", 0) == "")
	fmt.Println(Revrot("563000655734469485", 4) == "0365065073456944")
}
