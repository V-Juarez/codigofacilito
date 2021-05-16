package main

import "fmt"

func main() {

	// breack - continue
	for i := 1; i <= 10; i ++ {

			if i == 5 {
				continue
			}

			if i == 8 {
				break
			}

		fmt.Println(i)
	}
}