package main 


import "fmt"

func main() {
	
	usuarios := make(map[string]string)

	usuarios["eduardo"] = "eduardo@codigofacilito.com"

	correo := usuarios["eduardo"]

	fmt.Println(correo)
}