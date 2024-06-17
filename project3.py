#   CAFE MANAGEMENT SYSTEM

menu = {
    'Pizza': 340,
    'Burger': 150,
    'Pasta': 200,
    'MoMos': 100,
    'Coffee': 100,
    'Tea': 90,
    'Ice-cream':150
}

print("Welcome to our Coding Cafe")
print("Pizza: Rs340\nBurger: Rs150\nPasta: Rs 200\nMoMos: Rs100\nCoffee: Rs100\nTea: Rs90\nIce-cream: Rs150")

orders_total=0

item_1 = input("Enter the name of the item you want to order = ")

if item_1 in menu:
    orders_total += menu[item_1]
    print(f"Your {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available yet")

another_order = input("Do you want to order another item? (Yes/No)")

if another_order=="Yes":
    item_2 = input("Enter second item = ")
    if item_2 in menu:
        orders_total += menu[item_2]     
        print(f"Your {item_2} has been added to your order")

    else:
     print(f"Order item {item_2} is not available yet")

print(f"The total amount is {orders_total}")
