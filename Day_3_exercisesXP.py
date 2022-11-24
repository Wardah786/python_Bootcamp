keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for items in zip(keys, values):
    print(items)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def cinemax_total_cost(family_dict):
    """cinemax total cost"""
    total_cost = 0
    for member_age in family_dict.values():
        if member_age < 3:
            pass
        elif 3 <= member_age <= 12:
            total_cost += 10
        else:
            total_cost += 15
    return total_cost

print(f"Total cost of tickets: {cinemax_total_cost(family)}")


# Exercise 3
brand = {
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color':{'France': 'blue',
               'Spain': 'red',
               'US': ['pink', 'green']},

}

brand['number_stores'] = 2
clients = brand['type_of_clothes']
print(f"Zara's clients are {', '.join(clients)}")

brand['country_creation'] = 'Spain'
print(brand)

brand['international_competitors'].append("Desigual")
print(brand['international_competitors'])

del brand['creation_date']
print(brand['international_competitors'][3])
print(brand['major_color']['US'])

# Exercise 4
disney_users_A = {}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# res = {val: idx + 1 for idx, val in enumerate(users)}
# print(users + " : " + str(res))
for value in users:
    print(str(users.index(value)) + ". " + str(value))


# print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
dis_users_B = {}
for key in users:
    print(str(users.index(key)) + ". " + str(key))













