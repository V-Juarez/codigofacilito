package main

import "fmt"

import "os"

func main() {

	file, err := os.Open("./example.txt")

	if err != nil {
		panic("No fue posible obtener el archivo!!")
	}

	defer func() {
		fmt.Println("Cerramos el archivo!!")
		file.Close()
	}()

	contenido := make([]byte, 254)
	longitud, _ := file.Read(contenido)

	contenidoArchivo := string(contenido[0:longitud])

	fmt.Println(contenidoArchivo)
}