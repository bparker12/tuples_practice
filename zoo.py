zoos = ("lions", "tigers", "bears", "penguins", "snakes", "giraffes", "monkies", "rhinos", "eagles", "chickens")

zoo = zoos.index("eagles")

print(zoo)

animal_to_find = "tigers"

if animal_to_find in zoos:
    print(f'The {animal_to_find} are in the zoo')
else:
    print("not found")

# (first_animal, second_animal, third_animal, fourth_animal, fifth_animal) = zoos

# print(first_animal)
# print(second_animal)

animal_list = list(zoos)

animal_list.extend(["kangaroos", "jaguars", "elephant"])

zoos_tuples = tuple(animal_list)
