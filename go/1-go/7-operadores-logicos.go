package main

import "fmt"

func main() {

	/* 
	Operadores logicos
	&&
	||
	!
	*/

	// resultado := 20 == 20 && 30 == 30
	// resultado := 20 == 20 || 30 != 30 || 20 > 40
								// true					true			true				false
	resultado := 15 == 15 && 60 < 100 && (90 < 100 || 100 == 90)



	fmt.Println(resultado)
}