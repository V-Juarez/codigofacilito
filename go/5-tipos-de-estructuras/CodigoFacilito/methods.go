package CodigoFacilito

func (self *Curso) getTitulo() string {
	return self.Titulo
}

func (self *Curso) OtenerTitulo() string {
	return self.getTitulo()
}