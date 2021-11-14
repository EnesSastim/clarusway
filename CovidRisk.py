age = input("Are you a cigarette addict older than 75 years old?(y/n) ")
chronic = input("Do you have a severe chronic disease?(y/n) ")
immune = input("Is your immune system too weak?(y/n) ")

if age.lower() == "y" or "true":
    age = True
else:
    age = False

if chronic.lower() == "y" or "true":
    chronic = True
else:
    chronic = False

if immune.lower() == "y" or "true":
    immune = True
else:
    immune = False

print("\n############################\n")

risk = (age or chronic or immune)

if risk == True:
    print('\033[96m'+'\033[1m'+"There is a risk of death.")
else:
    print('\033[96m'+'\033[1m'+"There is not a risk of death.")
