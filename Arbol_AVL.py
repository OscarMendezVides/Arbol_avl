class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        self.raiz = self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo_actual):
        if not nodo_actual:
            return Nodo(valor)
        elif valor < nodo_actual.valor:
            nodo_actual.izquierda = self._agregar(valor, nodo_actual.izquierda)
        else:
            nodo_actual.derecha = self._agregar(valor, nodo_actual.derecha)

        nodo_actual.altura = 1 + max(self._altura(nodo_actual.izquierda), self._altura(nodo_actual.derecha))

        balance = self._get_balance(nodo_actual)

        if balance > 1 and valor < nodo_actual.izquierda.valor:
            return self._rotacion_derecha(nodo_actual)

        if balance < -1 and valor > nodo_actual.derecha.valor:
            return self._rotacion_izquierda(nodo_actual)

        if balance > 1 and valor > nodo_actual.izquierda.valor:
            nodo_actual.izquierda = self._rotacion_izquierda(nodo_actual.izquierda)
            return self._rotacion_derecha(nodo_actual)

        if balance < -1 and valor < nodo_actual.derecha.valor:
            nodo_actual.derecha = self._rotacion_derecha(nodo_actual.derecha)
            return self._rotacion_izquierda(nodo_actual)

        return nodo_actual

    def _altura(self, nodo):
        if not nodo:
            return 0

        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0

        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotacion_izquierda(self, nodo):
        temp = nodo.derecha
        temp2 = temp.izquierda

        temp.izquierda = nodo
        nodo.derecha = temp2

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        temp.altura = 1 + max(self._altura(temp.izquierda), self._altura(temp.derecha))

        return temp

    def _rotacion_derecha(self, nodo):
        temp = nodo.izquierda
        temp2 = temp.derecha

        temp.derecha = nodo
        nodo.izquierda = temp2

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        temp.altura = 1 + max(self._altura(temp.izquierda), self._altura(temp.derecha))

        return temp

    def preorden(self):
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if not nodo:
            return

        print(nodo.valor, end=" ")
        self._preorden(nodo.izquierda)
        self._preorden(nodo.derecha)

    def inorden(self):
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if not nodo:
            return

        self._inorden(nodo.izquierda)
       
