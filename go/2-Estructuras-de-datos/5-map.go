package main

import "fmt"

func main() {

/* 	dias := make(map[int]string)

	dias[0] = "Domingo"
	dias[1] = "Lunes"
	dias[2] = "Mates"
	dias[3] = "Miercoles"
	dias[4] = "Jueves"
	dias[5] = "Viernes"
	dias[6] = "Sabado"

	dias[4] = "JUEVES"
	
	fmt.Println(dias)
	fmt.Println(dias[4]) */
	// fmt.Println(cap(slice))

// Calidifaciones

	usuarios := make(map[string] []int)

	usuarios["Eduardo"] = []int { 10, 9, 8, 10, 5}

	fmt.Println(usuarios)
}