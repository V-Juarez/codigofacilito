package main 

import "fmt"



func main() {	// bloque 1


	var curso = "Curso Profesional de Go!" 
	var version = 5

	{		// bloque 2
		fmt.Println(curso)


		{	// bloque 3
			var version = 5

			fmt.Println(version)
			fmt.Println(curso)
		}

		fmt.Println(version)
	}

	fmt.Println(curso)
}