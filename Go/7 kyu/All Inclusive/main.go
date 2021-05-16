package main

import "fmt"

func ContainAllRots(strng string, arr []string) bool {
	rots := make([]string, 0)
	for i := 0; i < len(strng); i++ {
		rots = append(rots, strng[i:]+strng[:i])
	}

	for _, rot := range rots {
		flag := false
		for _, item := range arr {
			if item == rot {
				flag = true
				break
			}
		}
		if !flag {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(ContainAllRots("bsjq", []string{"bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"}) == true)
	fmt.Println(ContainAllRots("XjYABhR", []string{"TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"}) == false)
	fmt.Println(ContainAllRots("", []string{}) == true)
}
