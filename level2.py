import random

sides = ['Bread,', 'Pasta Salade,', 'Chips & Salsa,', 'Fries,', 'Chips,']
main_dishes = ['Chicken Tenders,', 'Hamburger,', 'Gyro,', 'Italien Beef,', 'Pizza,']
desserts = ['Ice cream', 'Brownie', 'Cookies', 'Cheese Cake', "Chocolate Cake"]

Menu = random.choice(sides) + " " + random.choice(main_dishes) + " " + random.choice(desserts)
group = Menu*5
print(Menu)
