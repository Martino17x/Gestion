class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def imprimir(self):
        print(self.nombre)
        print(self.precio)
        print(self.stock)

