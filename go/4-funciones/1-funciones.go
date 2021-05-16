package main

import "fmt"

func saluda(username string) {
	fmt.Println("Hola", username)
}

func main() {

	saluda("Cody")
}