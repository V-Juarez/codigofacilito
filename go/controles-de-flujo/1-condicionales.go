package main

import "fmt"

func main() {

	var edad int
	fmt.Print("Ingresa tu edad: ")
	fmt.Scanf("%d", &edad)

	if edad >= 18 {
		fmt.Println("El usuario es mayor de edad")
	} else {
		fmt.Println("El usuario es menor de edad!")
	}
}