	package main

import "fmt"

func main() {

	// else if
	// 10 - 8/9 - 6/7 -5

	var calificacion int

	fmt.Print("Ingresa una calificacion: ")
	fmt.Scanf("%d", &calificacion)

/* 	switch {
	case calificacion == 10:
		fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
	case calificacion == 8 || calificacion == 9:
		fmt.Println("Aprobaste la materia")
	case calificacion == 6 || calificacion == 7:
		fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
	case calificacion >= 0 && calificacion <= 5:
		fmt.Println("No aprebaste la materia")
	default:
			fmt.Println("Calificacion no valida")
	} */

	switch calificacion {
	  case 10:
	  	fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
	  case 8, 9:
	  	fmt.Println("Aprobaste la materia")
	  case 6, 7:
	  	fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
	  case 1, 2, 3, 4, 5:
	  	fmt.Println("No aprebaste la materia")
	  default:
	  	fmt.Println("Calificacion no valida")
	}

}