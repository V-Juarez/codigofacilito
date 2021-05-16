package main

import "fmt"

func funcion1() {
	fmt.Println("Hola, soy la primer funcion!!!")
}

func funcion2() {
	fmt.Println("Hola, soy la segunda funcion!!!")
}

func main() {

	fmt.Println("Hola, nos encontramos en la funcion main!!")

	defer funcion1()
	funcion2()
	// 
}