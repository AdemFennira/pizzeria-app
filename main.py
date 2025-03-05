from carte_pizzeria import CartePizzeria
from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

if __name__ == "__main__":
    carte = CartePizzeria()
    
    pizza1 = Pizza("Margherita", ["Tomate", "Mozzarella", "Basilic"], 8.5)
    pizza2 = Pizza("Pepperoni", ["Tomate", "Mozzarella", "Pepperoni"], 10)

    carte.add_pizza(pizza1)
    carte.add_pizza(pizza2)

    print("Nombre de pizzas:", carte.nb_pizzas())  # 2
    print("Carte vide ?", carte.is_empty())  # False

    carte.remove_pizza("Margherita")
    print("Nombre de pizzas après suppression:", carte.nb_pizzas())  # 1

    try:
        carte.remove_pizza("Quatre Fromages")
    except CartePizzeriaException as e:
        print("Erreur:", e)  # La pizza 'Quatre Fromages' n'existe pas
