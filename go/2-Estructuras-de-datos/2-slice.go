package main

import "fmt"

func main() {

	numeros := [] int {1, 2, 3, 4 }

	numeros = append(numeros, 5)
	numeros = append(numeros, 6)
	numeros = append(numeros, 7)
	numeros = append(numeros, 8)
	numeros = append(numeros, 9)
	numeros = append(numeros, 10)

	nuevoSlice := numeros[0:5]
	tercerSlice := numeros[0:3]

	numeros[0] = 100

	fmt.Println(numeros)
	fmt.Println(nuevoSlice)
	fmt.Println(tercerSlice)
}