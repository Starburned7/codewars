def get_order(order):
    correct_order = []
    menu = {
        "burger" : "Burger",
        "fries" : "Fries",
        "chicken": "Chicken",
        "pizza" : "Pizza",
        "sandwich": "Sandwich",
        "onionrings" : "Onionrings",
        "milkshake" : "Milkshake",
        "coke" : "Coke"}
    for item in menu:
        count = order.count(item)
        if item in order:
            correct_order.extend([menu[item]] * count)

    result = " ".join(correct_order)
    return result


get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")