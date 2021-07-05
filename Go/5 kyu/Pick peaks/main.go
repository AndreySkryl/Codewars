package main

import "fmt"

type PosPeaks struct {
	Pos   []int
	Peaks []int
}

func PickPeaks(array []int) PosPeaks {
	var (
		result           = PosPeaks{Pos: make([]int, 0), Peaks: make([]int, 0)}
		state, pos, peak int
	)

	if len(array) > 0 {
		peak = array[0]
	}

	for i, value := range array {
		if peak < value || (0 < i && array[i-1] < value) {
			pos, peak = i, value
			state = 1
		} else if peak > value && state == 1 && i != 0 && i != len(array) {
			result.Pos = append(result.Pos, pos)
			result.Peaks = append(result.Peaks, peak)
			state = -1
		}
	}
	return result
}

func main() {
	tests := []struct {
		expectedPoses []int
		expectedPeaks []int
		input         []int
	}{
		{
			expectedPoses: []int{3, 7, 10},
			expectedPeaks: []int{6, 3, 2},
			input:         []int{3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1},
		},
		{
			expectedPoses: []int{2, 4},
			expectedPeaks: []int{3, 2},
			input:         []int{2, 1, 3, 1, 2, 2, 2, 2, 1},
		},
		{
			expectedPoses: []int{2},
			expectedPeaks: []int{3},
			input:         []int{2, 1, 3, 1, 2, 2, 2, 2},
		},
		{
			expectedPoses: []int{},
			expectedPeaks: []int{},
			input:         []int{},
		},
	}
	for _, test := range tests {
		fmt.Println(test)
		fmt.Println(PickPeaks(test.input))
		fmt.Println("-------------")
	}
}
