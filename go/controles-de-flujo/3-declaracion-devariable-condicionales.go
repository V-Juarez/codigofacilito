package main

import "fmt"

func main() {

	if nombre, edad := "Cody", 7; nombre == "Cody " {
		fmt.Println("Hola", nombre, "te damos la bienvenido al curso de Go!")
	} else {
		fmt.Println("Los valores son: ", nombre, edad)
	}
	
}