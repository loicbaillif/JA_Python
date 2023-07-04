# Theory: Loop control statement
# https://hyperskill.org/learn/step/6302
# Author: JetBrains Academy

print("***** Theory: Loop control statement *****")

print("\n*** 1) break")
pets = ["dog", "cat", "bonobo"]
for pet in pets:
    print(pet)
    if pet == "cat":
        print("Loop break")
        break


print("\n***** End of theory *****")
