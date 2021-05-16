package main 

import "fmt"

func main() {

	numeros := []int {1, 2, 3, 4, 5, 6}

	numeros[0] = 100
	numeros[5] = 600

	inicio := numeros[0:3]
	final := numeros[3:6]

	fmt.Println(numeros)
	fmt.Println(inicio)
	fmt.Println(final)
}