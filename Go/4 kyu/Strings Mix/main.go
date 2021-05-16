package main

import (
	"fmt"
	"sort"
	"strings"
)

func createDict(s string) map[string]int {
	dict := map[string]int{}
	for _, v := range s {
		if 'a' <= v && v <= 'z' {
			dict[string(v)]++
		}
	}
	return dict
}

func createUnionDict(d1, d2 map[string]int) map[string][2]int {
	dict := map[string][2]int{}
	for k, v := range d1 {
		if v > 1 {
			dict[k] = [2]int{v, 1}
		}
	}
	for k, v := range d2 {
		if v > 1 {
			if _, ok := dict[k]; ok {
				if v == dict[k][0] {
					dict[k] = [2]int{v, 3}
				} else if v > dict[k][0] {
					dict[k] = [2]int{v, 2}
				}
			} else {
				dict[k] = [2]int{v, 2}
			}
		}
	}
	return dict
}

type Struct struct {
	alpha string
	count int
	str   int
}

func mapToSlice(dict map[string][2]int) []Struct {
	structs := make([]Struct, 0)
	for k, v := range dict {
		structs = append(structs, Struct{
			alpha: k,
			count: v[0],
			str:   v[1],
		})
	}
	return structs
}

func Mix(s1, s2 string) string {
	dict_1, dict_2 := createDict(s1), createDict(s2)
	dict := createUnionDict(dict_1, dict_2)
	structs := mapToSlice(dict)
	chunks := make([]string, 0)
	for _, _struct := range structs {
		_string := fmt.Sprintf("%v:%v", _struct.str, strings.Repeat(_struct.alpha, _struct.count))
		chunks = append(chunks, _string)
	}
	sort.Slice(chunks, func(i, j int) bool {
		return chunks[i] < chunks[j]
	})
	sort.SliceStable(chunks, func(i, j int) bool {
		return len(chunks[i]) > len(chunks[j])
	})

	result := strings.Join(chunks, "/")
	result = strings.ReplaceAll(result, "3", "=")

	fmt.Println("dict_1:")
	fmt.Println(dict_1)
	fmt.Println("dict_2:")
	fmt.Println(dict_2)

	fmt.Println("dict:")
	fmt.Println(dict)

	fmt.Println("structs:")
	fmt.Println(structs)

	fmt.Printf("result: %v\n", result)

	return result
}

func main() {
	fmt.Println(Mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
	fmt.Println(Mix("uuuuuu", "uuuuuu") == "=:uuuuuu")
	fmt.Println(Mix("looping is fun but dangerous", "less dangerous than coding") ==
		"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
}
