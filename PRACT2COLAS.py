class DLDqueue:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
            self.anterior = None

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def insertar_primero(self, obj):
        nuevo_nodo = self.Nodo(obj)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def insertar_ultimo(self, obj):
        nuevo_nodo = self.Nodo(obj)
        if not self.cola:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

    def eliminar_primero(self):
        if not self.cabeza:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.tamaño -= 1
        return dato

    def eliminar_ultimo(self):
        if not self.cola:
            return None
        dato = self.cola.dato
        self.cola = self.cola.anterior
        if self.cola:
            self.cola.siguiente = None
        else:
            self.cabeza = None
        self.tamaño -= 1
        return dato

    def obtener_tamaño(self):
        return self.tamaño

    def esta_vacia(self):
        return self.tamaño == 0
class DQPila:
    def __init__(self):
        self.datos = DLDqueue()

    def apilar(self, obj):
        """Inserta un objeto en la parte superior de la pila."""
        self.datos.insertar_primero(obj)

    def desapilar(self):
        """Elimina y devuelve el objeto en la parte superior de la pila."""
        return self.datos.eliminar_primero()

    def tamaño(self):
        """Devuelve el número de elementos en la pila."""
        return self.datos.obtener_tamaño()

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return self.datos.esta_vacia()

    def __str__(self):
        resultado = []
        nodo = self.datos.cabeza
        while nodo:
            resultado.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Pila: [" + " <- ".join(resultado) + "]"


class DQCola:
    def __init__(self):
        self.datos = DLDqueue()

    def encolar(self, obj):
        """Inserta un objeto al final de la cola."""
        self.datos.insertar_ultimo(obj)

    def desencolar(self):
        """Elimina y devuelve el objeto al frente de la cola."""
        return self.datos.eliminar_primero()

    def tamaño(self):
        """Devuelve el número de elementos en la cola."""
        return self.datos.obtener_tamaño()

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return self.datos.esta_vacia()

    def __str__(self):
        resultado = []
        nodo = self.datos.cabeza
        while nodo:
            resultado.append(str(nodo.dato))
            nodo = nodo.siguiente
        return "Cola: [" + " -> ".join(resultado) + "]"



def prueba_pila():
    print("Probando DQPila (implementación de la pila)...")
    pila = DQPila()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    print(pila)
    print(f"Desapilado: {pila.desapilar()}")
    print(pila)
    print(f"Tamaño: {pila.tamaño()}")
    print(f"Está vacía: {pila.esta_vacia()}")
    print("-" * 30)


def prueba_cola():
    print("Probando DQCola (implementación de la cola)...")
    cola = DQCola()
    cola.encolar(100)
    cola.encolar(200)
    cola.encolar(300)
    print(cola)
    print(f"Desencolado: {cola.desencolar()}")
    print(cola)
    print(f"Tamaño: {cola.tamaño()}")
    print(f"Está vacía: {cola.esta_vacia()}")
    print("-" * 30)


prueba_pila()
prueba_cola()