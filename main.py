import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# num_items = len(names)
# random_name_gen = random.randint(0, num_items - 1)
# select_member_payment = names[random_name_gen]


select_member_payment = random.choice(names)
print(select_member_payment + " will pay for the bill")