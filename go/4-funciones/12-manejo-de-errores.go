package main

import "fmt"
import "errors"

func division(dividendo, divisor int) (int, error) {

	if divisor == 0 {
		return 0, errors.New("No es posible dividir sobre 0.")
	} else {
		return dividendo / divisor, nil
	}
}

func main() {

	if resultado, err := division(10, 0); err != nil {
		// fmt.Println(err)
		panic(err)
	} else {
		fmt.Println("El resutlado es: ", resultado)
	}
	// 
}