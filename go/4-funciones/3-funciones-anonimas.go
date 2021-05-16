package main

import "fmt"

func main() {


	miFuncion  := func (username string) string {
		message := fmt.Sprintf("Hola %s, te saludamos desde una funcion sin nombre", username)

		return message
		// fmt.Println("Hola", username, "desde una funcion sin nombre!")
	} 
	
	
	mensajeFinal := miFuncion("Cody 1")
	fmt.Println(mensajeFinal)
	// miFuncion("Cody 2")
	// miFuncion("Cody 4")
	// miFuncion("Cody 3")
	// miFuncion("Cody 5")
}