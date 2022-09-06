class Quadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return self.lado*self.lado
    
    def perimetro(self):
        return self.lado*4

cm = Quadrado(15)
area = cm.area()
per = cm.perimetro()

print(area)
print(per)
