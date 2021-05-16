package main

import "fmt"

func main() {

	slice := make([]int, 3, 3)

	slice[0] = 100
	slice[1] = 200
	slice[2] = 300 

	slice = append(slice, 400)

	fmt.Println(slice)
	fmt.Println(len(slice))
	fmt.Println(cap(slice))
}