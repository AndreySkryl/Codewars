package main

import (
	"fmt"
	"math"
	"reflect"
)

func isPrime(n int) bool {
	for i := 2; i <= int(math.Ceil(math.Sqrt(float64(n)))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func Gap(g, m, n int) []int {
	primes := make([]int, 0, 10)
	val := m
	for i := 0; i < n-m+1; i++ {
		if isPrime(val) {
			primes = append(primes, val)
		}
		val++
	}

	if len(primes) == 1 {
		return nil
	}

	for i := 0; i < len(primes)-1; i++ {
		if primes[i+1]-primes[i] == g {
			return []int{primes[i], primes[i+1]}
		}
	}
	return nil
}

func main() {
	fmt.Println(reflect.DeepEqual(Gap(2, 100, 110), []int{101, 103}))
	fmt.Println(reflect.DeepEqual(Gap(4, 100, 110), []int{103, 107}))
	fmt.Println(reflect.DeepEqual(Gap(6, 100, 110), nil))
	fmt.Println(reflect.DeepEqual(Gap(8, 300, 400), []int{359, 367}))
	fmt.Println(reflect.DeepEqual(Gap(10, 300, 400), []int{337, 347}))
}
