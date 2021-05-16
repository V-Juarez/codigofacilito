package main

import "fmt"

func main() {

	// var (
	// 	nombre bool
	// 	apellido = 10
	// 	pais string
	// )
	/* 	var nombre string
		var apellido string
		var pais string */

		// multipes variables
		// var nombre, apellido, pais string
		// var nombre, apellido, pais = "Eduardo", "Garcia", "Mexico"

		nombre, apellido, pais := "Eduardo", "Garcia", "Mexico"
		edad, altura := 26, 1.80 

		fmt.Println(nombre, apellido, pais, edad, altura)

}