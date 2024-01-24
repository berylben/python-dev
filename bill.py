# write  code that will choose in random who will pay for the bill
import random
# names of people separated by a comma
name_string = input("give the names separated by a comma:")
names = name_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay for the bill today")

