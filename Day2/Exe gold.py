birthdays = {
    "Hajar": "2000/12/09",
    "Rajae": "2001/10/19",

}

print("Welcome to the Birthday Look-up Program!")
print("You can look up the birthdays of the people in the list.")

name = input("Enter a person's name to find their birthday: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don't have {name}'s birthday in the list.")
#Exercice2
print("Welcome to the Birthday Look-up Program!")
print("Here are the names in our database:")
for name in birthdays.keys():
    print("-", name)

name = input("Enter a person's name to find their birthday: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")