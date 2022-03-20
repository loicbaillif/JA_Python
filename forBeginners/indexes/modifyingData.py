# ****** INDEXES - Exercise : Modifying Data ******

# Lists, unlike strings, are mutable. We can use that to modify their data 
# with indexes.

# There is a list planets with the names of the Solar system planets. However, 
# instead of the 5th planet, there's an X. Replace it with the real name of
# the 5th planet. Do not forget, the first letter must be a capital one!

# Note that the list planets has already been defined, 
# you just need to change one element. Mind its index!

planets = ["Mercury", "Venus", "Earth", "Mars", "X", 
"Saturn", "Uranus", "Neptun"]

planets[4] = "Jupiter"