#Interger data type

black_tea_grams = 14
ginger_tea_grams = 3

total_tea_grams = black_tea_grams + ginger_tea_grams
print(total_tea_grams , "Grams of tea in total")

remaing_tea_grams = black_tea_grams - ginger_tea_grams
print(remaing_tea_grams, "Grams of tea remaining after making ginger tea")


milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(milk_per_serving, "Liters of milk per serving")

total_tea_bags = 7
pots = 2
bags_per_pot = total_tea_bags // pots
print(bags_per_pot, "Tea bags per pot")

total_codamom_pods = 10
pods_per_cup = 3
leftover_pods = total_codamom_pods % pods_per_cup
print(leftover_pods, "Codamom pods left after making tea")

total_tea_bags = 7
pots = 2
bags_per_pot = total_tea_bags / pots
print(bags_per_pot, "Tea bags per pot (float division)")  


base_flovor_strength = 2
scale_factor = 3
powerful_flovor_strength = base_flovor_strength ** scale_factor
print(f"Scaled flavor strength {powerful_flovor_strength}")

total_tea_leaves_harvested = 10000000000000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested:,} grams")