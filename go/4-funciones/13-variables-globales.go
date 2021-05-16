package main

import "fmt"

var username string  // ""

func funcion1() {
	username = "Funcion1"
	fmt.Println("Funcion1: ", username)
}

func funcion2() {
	username = "Funcion2"

	fmt.Println("Funcion2: ", username)
	
}

func main() {

	username = "Cody"
	
	funcion1()
	funcion2()

	fmt.Println(username)
}