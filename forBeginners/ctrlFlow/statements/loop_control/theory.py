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

count = 0
while True:
    print(f"I am infinite loop ... iteration {count}")
    count += 1
    if count == 11:
        break

numbers = [1, 2, 3, 4]
for elt in numbers:
    if elt == 5:
        print("I've got 5 on it")
        break
else:
    print("5 was not listed")


print("\n*** 2) continue")
for pet in pets:
    if pet == "cat":
        continue
    print(f"\t. {pet}")

for pet in pets:
    if pet != "dog":
        print(pet)


print("\n***** End of theory *****")
