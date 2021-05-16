package main

import "fmt"

import "./CodigoFacilito"

func main() {

	curso := CodigoFacilito.Curso { Titulo: "Curso Profesional de Go!!" }

	fmt.Println(curso.ObtenerTitulo())
}

