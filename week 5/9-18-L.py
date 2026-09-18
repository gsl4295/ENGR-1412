"""
all my lab work is just done on the side, since
i have an IDE already and i like working in it.
you can take a look at the rest of my Python work
at my GitHub repo https://github.com/gsl4295/ENGR-1412
"""

import math

def problem3_lab5():
    age = int(input())
    weight = int(input())
    heart_rate = int(input())
    minutes = int(input())

    calories_burned = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * minutes / 8.368
    print(f"Calories: {calories_burned:.2f} calories\n")

def problem4_lab5():
    x = float(input())
    y = float(input())
    z = float(input())
    print(f"{math.pow(x, z):.2f} {math.pow(x, math.pow(y, z)):.2f} {math.fabs(x - y):.2f} {math.sqrt(math.pow(x, z)):.2f}\n")

def problem5_lab5():
    f0 = int(input())
    r = math.pow(2, (1/12))
    for n in range(0, 4):
        print(f"{f0 * math.pow(r, n):.2f} Hz")

def problem6_lab5():
    user_int = int(input("Enter integer (32 - 126):\n"))
    user_float = float(input("Enter float:\n"))
    user_char = str(input("Enter character:\n"))
    user_str = str(input("Enter string:\n"))
    print(f"{user_int} {user_float} {user_char} {user_str}")
    print(f"{user_str} {user_char} {user_float} {user_int}")
    print(f"{user_int} converted to a character is {chr(user_int)}\n")

def problem7_lab5():
    first_food_item = str(input(f"Enter food item name:\n"))
    first_item_price = float(input("Enter item price:\n"))
    first_item_quantity = int(input("Enter item quantity:\n"))
    first_item_total_cost = first_item_price * first_item_quantity
    print("\nRECEIPT")
    print(f"{first_item_quantity} {first_food_item} @ ${first_item_price:.2f} = ${first_item_total_cost:.2f}")
    print(f"Total cost: ${first_item_total_cost:.2f}\n\n")

    second_food_item = str(input(f"Enter second food item name:\n"))
    second_item_price = float(input("Enter item price:\n"))
    second_item_quantity = int(input("Enter item quantity:\n"))
    second_item_total_cost = second_item_price * second_item_quantity
    print("\nRECEIPT")
    print(f"{first_item_quantity} {first_food_item} @ ${first_item_price:.2f} = ${first_item_total_cost:.2f}")
    print(f"{second_item_quantity} {second_food_item} @ ${second_item_price:.2f} = ${second_item_total_cost:.2f}")

    subtotal = first_item_total_cost + second_item_total_cost
    gratuity = subtotal * 0.15
    print(f"Total cost: ${subtotal:.2f}\n")
    print(f"15% gratuity: ${gratuity:.2f}")
    print(f"Total with tip: ${subtotal + gratuity:.2f}")

def problem8_lab5():
    nickels = int(input()) * 0.05
    dimes = int(input()) * 0.10
    quarters = int(input()) * 0.25
    print(f"Amount: ${nickels + dimes + quarters:.2f}")
