class pila:
    

    def __init__(self):
        self.pila = []


    def push(self, num):
        self.pila.append(num)

    def pop(self):
        try:
            return self.pila.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")

    def show(self):
        for elementos in self.pila:
            print(elementos)

    def buscar(self):
        pass

    def esvacia(self):
        return self.pila == []



