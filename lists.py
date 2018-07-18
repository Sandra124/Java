import random
first_name = ['John', 'Sam', 'Vicky', 'Sadie', 'Lizbeth', 'Victor']
last_name = ['Harp', 'Slay', 'Coats', 'Mounos', 'Hood', 'Hunt']

full_name = random.choice(first_name)+ " " + random.choice(last_name)
group = full_name*6
print(full_name)
