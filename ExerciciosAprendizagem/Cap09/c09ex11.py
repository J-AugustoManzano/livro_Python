class TipoArea():

    def area(self, x=0.0, y=0.0, z=0.0):
        if (isinstance(x, float) and y == 0.0 and z == 0.0):
            return x ** 2
        elif (isinstance(x, float) and isinstance(y, float) and z == 0.0):
            return x ** 2 * 3.14159 * y
        elif (isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            return x * y * z
        
calculo = TipoArea()

print("Área: Quadrado .. = {0:7.2f}".format(calculo.area(5.0)))
print("Área: Cubo ...... = {0:7.2f}".format(calculo.area(5.0, 6.0, 7.0)))
print("Área: Cilindro .. = {0:7.2f}".format(calculo.area(7.0, 3.0)))

enter = input("\nPressione <Enter> para encerrar... ")
