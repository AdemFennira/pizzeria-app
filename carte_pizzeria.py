from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        """Retourne True si la carte est vide, sinon False."""
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        """Retourne le nombre de pizzas dans la carte."""
        return len(self.pizzas)

    def add_pizza(self, pizza):
        """Ajoute une pizza à la carte."""
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        """Retire la pizza du nom donné, lève une exception si elle n'existe pas."""
        for pizza in self.pizzas:
            if pizza.nom == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")