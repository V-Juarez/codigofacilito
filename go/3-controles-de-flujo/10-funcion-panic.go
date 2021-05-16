package main

import "fmt"

func main() { 

	//  panic
	var dividendo, divisor int

	fmt.Print("Ingresa un valor para el vividendo: ")
	fmt.Scanf("%d", &dividendo)

	fmt.Print("Ingresa un valor para el divisor: ")
	fmt.Scanf("%d", &divisor)

	if divisor == 0 {
		panic("No es posible dividir sobre 0")
	}

	resultado := dividendo / divisor

	fmt.Println(resultado)
}