package main


import "fmt"

func main() {

	var numero = 10

	for ok := true; ok; ok = numero < 10 {   //while

		fmt.Println(numero)
		numero ++
	}
}

