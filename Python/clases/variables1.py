class Circulo:
    def __init__(self, radio):
        self.radio = radio

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(circulo_a.radio)
print(circulo_b.radio)