package main

import "fmt"

func main() {

// else if
// 10 - 8/9 - 6/7 -5

var calificacion int

fmt.Print("Ingresa una calificacion: ")
fmt.Scanf("%d", &calificacion)

/* 	if calificacion == 10 {
	fmt.Println("Felicidades, obtuviste una calificacion perfecta!")
} else {
	if calificacion == 8 || calificacion == 9 {
		fmt.Println("Aprobaste la materia")
	} else {
		if calificacion == 6 || calificacion == 7 {
			fmt.Println("Aprobaste la materai, pero necesitas estudiar mas")
		} else {
			if calificacion >= 0 && calificacion <= 5 {
				fmt.Println("No aprobaste la materia")
			} else {
				fmt.Println("Calificacion no valida")
			}
		}
	}
} */
if calificacion == 10 {
	fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
} else if calificacion == 8 || calificacion == 9 {
	fmt.Println("Aprobaste la materia")
} else if calificacion == 6 || calificacion == 7 {
	fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
} else if calificacion >= 0 && calificacion <= 5 {
	fmt.Println("No aprebaste la materia")
} else {
	fmt.Println("Calificacion no valida")
}
}